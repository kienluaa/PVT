#!/usr/bin/env python3
"""Build data.js for the PVT shipping dashboard.

Downloads public CSVs (yieldchaser/Shipping on GitHub, updated daily via GitHub Actions)
and writes window.SHIP = {...} into data.js next to this script.
Usage: python3 build.py [outdir]
"""
import io, json, sys, os, datetime as dt, urllib.request
import pandas as pd

RAW = "https://raw.githubusercontent.com/yieldchaser/Shipping/main/data/"
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

INDICES = [  # key, file, name, group, relevance to PVT
    ("BSI", "indices/suprama_historical.csv", "Baltic Supramax", "dry", "7 Supramax + 1 Ultramax"),
    ("BHSI", "indices/handysize_historical.csv", "Baltic Handysize", "dry", "5 Handysize"),
    ("BDI", "indices/bdiy_historical.csv", "Baltic Dry Index", "dry", "Tổng thể hàng rời"),
    ("BCI", "indices/cape_historical.csv", "Baltic Capesize", "dry", "Tham khảo"),
    ("BPI", "indices/panama_historical.csv", "Baltic Panamax", "dry", "Tham khảo"),
    ("BDTI", "indices/dirtytanker_historical.csv", "Baltic Dirty Tanker", "tanker", "4 tàu dầu thô (Aframax)"),
    ("BCTI", "indices/cleantanker_historical.csv", "Baltic Clean Tanker", "tanker", "8 tàu dầu SP/MR"),
]
START = "2008-01-01"


def get(path):
    req = urllib.request.Request(RAW + path, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return pd.read_csv(io.BytesIO(r.read()))


def num(s):
    return pd.to_numeric(s.astype(str).str.replace(",", "").str.strip(), errors="coerce")


def stats(s):
    s = s.dropna()
    last = float(s.iloc[-1]); d = s.index[-1]
    def ago(days):
        p = s[s.index <= d - pd.Timedelta(days=days)]
        return float(p.iloc[-1]) if len(p) else None
    def pct(a):
        return None if not a else round((last / a - 1) * 100, 2)
    w5 = s[s.index > d - pd.Timedelta(days=365 * 5)]
    return {
        "last": last, "date": d.strftime("%Y-%m-%d"),
        "prev": float(s.iloc[-2]) if len(s) > 1 else None,
        "d1": pct(float(s.iloc[-2])) if len(s) > 1 else None,
        "w1": pct(ago(7)), "m1": pct(ago(30)), "y1": pct(ago(365)),
        "ytd": pct(float(s[s.index < pd.Timestamp(d.year, 1, 1)].iloc[-1])) if (s.index < pd.Timestamp(d.year, 1, 1)).any() else None,
        "pctl5y": round(float((w5 < last).mean() * 100), 1),
        "min5y": float(w5.min()), "max5y": float(w5.max()), "avg5y": round(float(w5.mean()), 1),
        "ma20": round(float(s.iloc[-20:].mean()), 1),
    }


def series(s):
    s = s.dropna()
    return {"d": [x.strftime("%Y-%m-%d") for x in s.index], "v": [round(float(x), 2) for x in s.values]}


out = {"built": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"), "indices": {}, "tc": {}, "val": {}, "choke": {}, "errors": []}

for key, f, name, grp, rel in INDICES:
    try:
        df = get(f)
        df["Date"] = pd.to_datetime(df["Date"], format="mixed")
        s = num(df["Index"]); s.index = df["Date"]
        s = s[~s.index.duplicated(keep="last")].sort_index()
        s = s[s.index >= START]
        out["indices"][key] = {"name": name, "group": grp, "rel": rel, "stats": stats(s), **series(s)}
    except Exception as e:
        out["errors"].append(f"{key}: {e}")

# Time-charter rates ($/day), weekly
TC = {
    "supramax_1y_avg": "Supramax 1 năm", "supramax_2y_avg": "Supramax 2 năm",
    "handysize_1y_avg": "Handysize 1 năm", "handysize_2y_avg": "Handysize 2 năm",
    "aframax_1y": "Aframax 1 năm", "aframax_3y": "Aframax 3 năm",
    "mr_1y": "MR 1 năm", "mr_3y": "MR 3 năm",
    "lr2_1y": "LR2 1 năm", "handytanker_1y": "Handy tanker 1 năm",
    "vlcc_1y": "VLCC 1 năm", "suezmax_1y": "Suezmax 1 năm",
}
try:
    t = get("derived/time_charter_rates.csv"); t["date"] = pd.to_datetime(t["date"])
    t = t[t["date"] >= "2015-01-01"].sort_values("date")
    for c, label in TC.items():
        if c in t:
            s = t.set_index("date")[c].dropna(); s = s[~s.index.duplicated(keep="last")]
            if len(s):
                out["tc"][c] = {"name": label, "stats": stats(s), **series(s)}
except Exception as e:
    out["errors"].append(f"TC: {e}")

# Vessel values (US$ m)
VAL = [
    ("S&P", "WET-10", "MR", "MR 10 tuổi"), ("S&P", "WET-10", "Aframax / LR2", "Aframax/LR2 10 tuổi"),
    ("S&P", "WET-5", "MR", "MR 5 tuổi"),
    ("S&P", "DRY-15-JP", "Ultramax (Japanese)", "Ultramax 15 tuổi (Nhật)"),
    ("S&P", "DRY-15-JP", "Handysize (Japanese)", "Handysize 15 tuổi (Nhật)"),
    ("NEWBUILDING", None, "Product", "Đóng mới MR"), ("NEWBUILDING", None, "Ultramax", "Đóng mới Ultramax"),
    ("NEWBUILDING", None, "Aframax", "Đóng mới Aframax"),
]
try:
    v = get("derived/vessel_valuations.csv"); v["date"] = pd.to_datetime(v["date"])
    v = v[v["date"] >= "2015-01-01"]
    for cat, ten, cls, label in VAL:
        m = (v.category == cat) & (v.vessel_class == cls)
        if ten: m &= (v.tenor_type == ten)
        s = v[m].set_index("date")["valuation_usd_m"].sort_index(); s = s[~s.index.duplicated(keep="last")]
        if len(s):
            out["val"][label] = {"stats": stats(s), **series(s)}
except Exception as e:
    out["errors"].append(f"VAL: {e}")

# Chokepoint transits (IMF PortWatch), 7-day average, since 2022
CH = ["Strait of Hormuz", "Bab el-Mandeb Strait", "Suez Canal", "Cape of Good Hope", "Malacca Strait", "Panama Canal"]
try:
    c = get("congestion/chokepoint_transits_daily.csv"); c["date"] = pd.to_datetime(c["date"])
    c = c[(c["date"] >= "2022-01-01") & c.portname.isin(CH)]
    for p in CH:
        g = c[c.portname == p].set_index("date").sort_index()
        for col, tag in (("n_tanker", "tanker"), ("n_total", "total")):
            s = g[col].fillna(0).rolling(7).mean().dropna().round(1)
            raw = g[col].fillna(0)
            out["choke"].setdefault(p, {})[tag] = {**series(s), "last7": float(s.iloc[-1]), "date": s.index[-1].strftime("%Y-%m-%d"),
                                                   "avg2023": round(float(raw["2023"].mean()), 1) if len(raw["2023"]) else None}
except Exception as e:
    out["errors"].append(f"CHOKE: {e}")


# ---------- Tier-1/2 extras ----------
def ser_from(df, dcol, vcol, start="2015-01-01", dayfirst=False):
    d = df[[dcol, vcol]].dropna().copy(); d[dcol] = pd.to_datetime(d[dcol], format="%d-%m-%Y") if dayfirst else pd.to_datetime(d[dcol])
    s = d.set_index(dcol)[vcol].astype(float).sort_index(); s = s[~s.index.duplicated(keep="last")]
    return s[s.index >= start]

out["bunker"] = {}; out["fwd"] = {}; out["scrap"] = {}; out["lpg"] = {}; out["ports"] = {}; out["misc"] = {}
# Bunker: Singapore VLSFO long history (weekly, from EU ETS file) + daily since Aug-2026
try:
    b = get("bunkers/bunker_prices_daily.csv"); b["date"] = pd.to_datetime(b["date"])
    e = get("derived/eu_ets_carbon_daily.csv"); e["date"] = pd.to_datetime(e["date"])
    for port, grade, label in [("singapore", "VLSFO", "VLSFO Singapore"), ("singapore", "MGO", "MGO Singapore"),
                               ("fujairah", "VLSFO", "VLSFO Fujairah"), ("rotterdam", "VLSFO", "VLSFO Rotterdam"),
                               ("singapore", "IFO380", "HSFO 380 Singapore")]:
        s = b[(b.port == port) & (b.fuel_grade == grade)].set_index("date")["price_usd_mt"].astype(float).sort_index()
        if port == "singapore" and grade in ("VLSFO", "IFO380"):
            col = "singapore_vlsfo_usd_mt" if grade == "VLSFO" else "singapore_hsfo_usd_mt"
            h = e.set_index("date")[col].dropna().astype(float)
            h = h[(h.index >= "2021-01-01") & (h.index < s.index.min())]
            s = pd.concat([h, s]).sort_index()
        s = s[~s.index.duplicated(keep="last")]
        if len(s) > 1:
            out["bunker"][label] = {"stats": stats(s), **series(s)}
    eua = e.set_index("date")["eua_carbon_price_eur_tco2"].dropna().astype(float); eua = eua[eua.index >= "2021-01-01"]
    out["misc"]["EUA"] = {"stats": stats(eua), **series(eua)}
    hi5 = e.set_index("date")["singapore_hi5_spread_usd_mt"].dropna().astype(float); hi5 = hi5[hi5.index >= "2021-01-01"]
    if len(hi5): out["misc"]["Hi5 Singapore"] = {"stats": stats(hi5), **series(hi5)}
except Exception as ex:
    out["errors"].append(f"BUNKER: {ex}")

# Dry FFA (SGX) forward curves: latest snapshot vs ~30 days earlier
def sgx_curve(path, label):
    f = get(path); f["date"] = pd.to_datetime(f["date"]); f["exp"] = pd.to_datetime(f["expiry_date"], format="%d-%m-%Y")
    last = f["date"].max()
    def snap(day):
        g = f[f["date"] == day]; g = g[g["exp"] >= day.replace(day=1)].sort_values("exp").head(27)
        return {"asof": day.strftime("%Y-%m-%d"), "m": [x.strftime("%Y-%m") for x in g["exp"]], "v": [float(x) for x in g["price"]]}
    prev_days = f.loc[f["date"] <= last - pd.Timedelta(days=28), "date"]
    cur = snap(last); prev = snap(prev_days.max()) if len(prev_days) else None
    cal = {}
    for y in sorted(set(m[:4] for m in cur["m"])):
        vals = [v for m, v in zip(cur["m"], cur["v"]) if m.startswith(y)]
        if len(vals) == 12: cal[y] = round(sum(vals) / 12)
    out["fwd"][label] = {"cur": cur, "prev": prev, "cal": cal, "unit": "$/ngày"}
for path, label in [("futures/sgx_supramax_futures.csv", "Supramax (SGX)"), ("futures/sgx_handysize_futures.csv", "Handysize (SGX)")]:
    try: sgx_curve(path, label)
    except Exception as ex: out["errors"].append(f"FFA {label}: {ex}")

def clean_curve(c):
    """Drop non-positive points and isolated spikes (>45% away from both neighbours' mean) — source glitches."""
    m, v = c["m"], c["v"]; keep = []
    for i, x in enumerate(v):
        if x is None or x != x or x <= 0: continue
        if 0 < i < len(v) - 1:
            nb = (v[i - 1] + v[i + 1]) / 2
            if nb > 0 and abs(x / nb - 1) > 0.45 and abs(v[i-1]/v[i+1]-1) < 0.45: continue
        keep.append(i)
    c["dropped"] = [m[i] for i in range(len(m)) if i not in keep]
    c["m"] = [m[i] for i in keep]; c["v"] = [v[i] for i in keep]
    return c

# Tanker forward curves (TCE $/day), latest snapshot vs previous snapshot
try:
    t = get("derived/tanker_forward_curves_history.csv"); t["snapshot_date"] = pd.to_datetime(t["snapshot_date"])
    snaps = sorted(t["snapshot_date"].unique())
    def tsnap(day):
        g = t[t["snapshot_date"] == day].sort_values("forward_month")
        return g
    cur = tsnap(snaps[-1]); prev = tsnap(snaps[-2]) if len(snaps) > 1 else None
    for col, label in [("aframax_td25", "Aframax TD25 (USG→UKC)"), ("lr1_tc5", "LR1 TC5 (MEG→Nhật)"), ("mr_triangulation", "MR tam giác Đại Tây Dương"), ("mr_tc14", "MR TC14 (USG→UKC)")]:
        if col in t:
            c = clean_curve({"asof": pd.Timestamp(snaps[-1]).strftime("%Y-%m-%d"), "m": [str(x)[:7] for x in cur["forward_month"]], "v": [float(x) for x in cur[col]]})
            pv = None
            if prev is not None:
                pv = clean_curve({"asof": pd.Timestamp(snaps[-2]).strftime("%Y-%m-%d"), "m": [str(x)[:7] for x in prev["forward_month"]], "v": [float(x) for x in prev[col]]})
            cal = {}
            for y in sorted(set(m[:4] for m in c["m"])):
                vals = [v for m, v in zip(c["m"], c["v"]) if m.startswith(y)]
                if len(vals) >= 10: cal[y] = round(sum(vals) / len(vals))
            out["fwd"][label] = {"cur": c, "prev": pv, "cal": cal, "unit": "$/ngày"}
except Exception as ex:
    out["errors"].append(f"TANKER FWD: {ex}")

# Demolition prices ($/LDT)
try:
    sc = get("derived/scrappage_prices.csv")
    for col, label in [("tanker_bangla", "Tàu dầu – Bangladesh"), ("tanker_india", "Tàu dầu – Ấn Độ"), ("dry_bangla", "Hàng rời – Bangladesh"), ("dry_pak", "Hàng rời – Pakistan")]:
        s = ser_from(sc, "date", col, "2021-01-01")
        if len(s): out["scrap"][label] = {"stats": stats(s), **series(s)}
except Exception as ex:
    out["errors"].append(f"SCRAP: {ex}")

# LPG: Baltic LPG index + TC rates by size ($/month)
try:
    bl = get("indices/blpg_historical.csv"); s = ser_from(bl.assign(Index=num(bl["Index"])), "Date", "Index", "2020-01-01", dayfirst=True)
    out["lpg"]["BLPG"] = {"name": "Baltic LPG (VLGC)", "stats": stats(s), **series(s)}
    lc = get("derived/lpg_charter_rates.csv")
    for col, label in [("vlgc_84k_tc", "VLGC 84k cbm, 1 năm"), ("mgc_38k_tc", "MGC 38k cbm, 1 năm"), ("hdy_22k_tc", "Handy LPG 22k cbm, 1 năm")]:
        s = ser_from(lc, "date", col, "2019-01-01") / 1000.0
        out["lpg"][label] = {"name": label, "stats": stats(s), **series(s)}
except Exception as ex:
    out["errors"].append(f"LPG: {ex}")

# Intermodal TC (second broker, cross-check)
try:
    im = get("derived/intermodal_tc_rates.csv"); im["date"] = pd.to_datetime(im["date"]); last = im.sort_values("date").iloc[-1]
    out["misc"]["intermodal"] = {"date": last["date"].strftime("%Y-%m-%d"), **{k: float(last[k]) for k in ["aframax_1y_tc", "aframax_3y_tc", "mr_1y_tc", "mr_3y_tc", "handy_tanker_1y_tc", "supramax_1y_tc", "handysize_1y_tc", "lr1_1y_tc"]}}
except Exception as ex:
    out["errors"].append(f"INTERMODAL: {ex}")

# Crude/product export ports (IMF PortWatch), 30-day avg exports vs 2023
try:
    pc = get("congestion/portwatch_port_congestion.csv"); pc["date"] = pd.to_datetime(pc["date"])
    PORTS = {"Ras Tanura": "Ras Tanura (Ả Rập Xê Út)", "Juaymah": "Juaymah (Ả Rập Xê Út)", "Mina Al Ahmadi": "Mina Al Ahmadi (Kuwait)",
             "Yanbu (King Fahd Port)": "Yanbu (Biển Đỏ)", "Fujairah": "Fujairah (UAE)", "Primorsk": "Primorsk (Nga, Baltic)",
             "Sikka": "Sikka (Ấn Độ)", "Singapore": "Singapore", "Houston (US-TX)": "Houston (Mỹ)", "Corpus Christi": "Corpus Christi (Mỹ)"}
    for p, label in PORTS.items():
        g = pc[pc.portname == p].set_index("date").sort_index()
        if not len(g): continue
        ex_ = g["export_tanker_kt"].fillna(0); calls = g["daily_port_calls_tanker"].fillna(0)
        s30 = calls.rolling(30).mean().dropna(); s30 = s30[s30.index >= "2023-01-01"]
        out["ports"][label] = {"date": g.index[-1].strftime("%Y-%m-%d"), "exp30": round(float(ex_.iloc[-30:].mean()), 1),
                               "exp2023": round(float(ex_["2023"].mean()), 1) if len(ex_["2023"]) else None,
                               "calls30": round(float(calls.iloc[-30:].mean()), 1), "calls2023": round(float(calls["2023"].mean()), 1) if len(calls["2023"]) else None,
                               **series(s30.round(1))}
except Exception as ex:
    out["errors"].append(f"PORTS: {ex}")

# US crude exports (EIA weekly)
try:
    ue = get("commodities/us_eia_weekly_crude_exports.csv"); s = ser_from(ue, "date", "crude_4w_avg_kbpd", "2019-01-01")
    out["misc"]["US crude exports"] = {"stats": stats(s), **series(s)}
except Exception as ex:
    out["errors"].append(f"EIA: {ex}")

# ---------- Thesis scorecard (data-driven items) ----------
def item(key, name, value, unit, asof, status, rule, why):
    return {"key": key, "name": name, "value": value, "unit": unit, "asof": asof, "status": status, "rule": rule, "why": why, "auto": True}
score = []
try:
    h = out["choke"]["Strait of Hormuz"]["tanker"]; v = h["last7"]
    score.append(item("hormuz", "Tàu dầu qua Hormuz (TB 7 ngày)", v, "lượt/ngày", h["date"],
                      "green" if v < 10 else "yellow" if v < 30 else "red", "Xanh <10 · Vàng 10–30 · Đỏ >30 (bình thường hóa; 2023: ~49)",
                      "Hormuz còn nghẽn thì quãng đường dài, cước tàu dầu cao. Mở lại là rủi ro giảm cước lớn nhất."))
except Exception: pass
for k, nm in (("BDTI", "BDTI – phân vị 5 năm"), ("BCTI", "BCTI – phân vị 5 năm"), ("BSI", "BSI – phân vị 5 năm"), ("BHSI", "BHSI – phân vị 5 năm")):
    try:
        st = out["indices"][k]["stats"]; v = st["pctl5y"]
        score.append(item(k.lower(), nm, v, "%", st["date"], "green" if v >= 60 else "yellow" if v >= 30 else "red",
                          "Xanh ≥60% · Vàng 30–60% · Đỏ <30%", {"BDTI": "Cước dầu thô chuyến (Aframax của PVT).", "BCTI": "Cước dầu sản phẩm chuyến (MR của PVT).",
                          "BSI": "Phân khúc PVT chịu cước chuyến nhiều nhất.", "BHSI": "5 tàu Handysize của PVT."}[k]))
    except Exception: pass
for k, nm in (("mr_1y", "MR định hạn 1 năm so với TB 5 năm"), ("aframax_1y", "Aframax định hạn 1 năm so với TB 5 năm"), ("supramax_1y_avg", "Supramax định hạn 1 năm so với TB 5 năm")):
    try:
        st = out["tc"][k]["stats"]; v = round((st["last"] / st["avg5y"] - 1) * 100, 1)
        score.append(item(k, nm, v, "%", st["date"], "green" if v >= 20 else "yellow" if v >= -10 else "red",
                          "Xanh ≥+20% · Vàng −10…+20% · Đỏ <−10%", "Mức giá PVT tái ký hợp đồng 6–12 tháng, tác động trực tiếp lên doanh thu năm sau."))
    except Exception: pass
try:
    f = out["fwd"]["Supramax (SGX)"]; c27 = f["cal"].get("2027"); spot = out["indices"]["BSI"]["stats"]
    tc = out["tc"]["supramax_1y_avg"]["stats"]["last"]
    if c27:
        v = round((c27 / tc - 1) * 100, 1)
        score.append(item("ffa_smx", "FFA Supramax năm 2027 so với định hạn 1 năm hiện tại", v, "%", f["cur"]["asof"],
                          "green" if v >= -10 else "yellow" if v >= -25 else "red", "Xanh ≥−10% · Vàng −10…−25% · Đỏ <−25%",
                          f"Thị trường đang định giá cước Supramax 2027 ≈ {c27:,} $/ngày. Đây là kỳ vọng cho giai đoạn tái ký."))
except Exception: pass
try:
    f = out["fwd"]["LR1 TC5 (MEG→Nhật)"]; cur = f["cur"]; first = cur["v"][1] if len(cur["v"]) > 1 else cur["v"][0]; lastv = cur["v"][-1]
    v = round((lastv / first - 1) * 100, 1)
    score.append(item("ffa_tanker", "Đường cong kỳ hạn LR1: tháng xa nhất so với tháng tới", v, "%", cur["asof"],
                      "green" if v >= -30 else "yellow" if v >= -60 else "red", "Xanh ≥−30% · Vàng −30…−60% · Đỏ <−60%",
                      "Độ dốc giảm cho biết thị trường kỳ vọng cước tàu dầu hạ nhiệt nhanh đến mức nào trong 12–15 tháng."))
except Exception: pass
try:
    s = out["val"]["MR 10 tuổi"]; st = s["stats"]; d = pd.Series(s["v"], index=pd.to_datetime(s["d"]))
    base = d[d.index <= d.index[-1] - pd.Timedelta(days=90)]
    if len(base):
        v = round((d.iloc[-1] / base.iloc[-1] - 1) * 100, 1)
        score.append(item("snp15", "Giá tàu MR 10 tuổi – thay đổi 3 tháng", v, "%", st["date"], "green" if v <= 5 else "yellow" if v <= 20 else "red",
                          "Xanh ≤+5% · Vàng +5…+20% · Đỏ >+20%", "Đại diện cho chi phí mở rộng đội tàu (PVT mua tàu cũ khoảng 15 tuổi). Tăng nhanh thì PVT mua tàu chậm lại hoặc phải mua đắt; bù lại, giá trị đội tàu hiện có cũng tăng."))
except Exception: pass
try:
    st = out["scrap"]["Tàu dầu – Bangladesh"]["stats"]; v = st["last"]
    score.append(item("scrap", "Giá phá dỡ tàu dầu (Bangladesh)", v, "$/LDT", st["date"], "green" if v >= 450 else "yellow" if v >= 350 else "red",
                      "Xanh ≥450 · Vàng 350–450 · Đỏ <350", "Mức sàn giá trị cho đội tàu già của PVT (bình quân khoảng 17 tuổi)."))
except Exception: pass
out["score"] = score

js = "window.SHIP=" + json.dumps(out, separators=(",", ":"), ensure_ascii=False) + ";"
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "data.js"), "w") as fh:
    fh.write(js)
summ = {k: v["stats"] for k, v in out["indices"].items()}
print(json.dumps({"built": out["built"], "errors": out["errors"], "indices": summ,
                  "tc_last": {k: (v["stats"]["last"], v["stats"]["date"]) for k, v in out["tc"].items()},
                  "choke_tanker7d": {k: (v["tanker"]["last7"], v["tanker"]["avg2023"], v["tanker"]["date"]) for k, v in out["choke"].items()}},
                 ensure_ascii=False, indent=1))
print("score:", [(x["key"], x["value"], x["status"]) for x in out["score"]])
print("fwd cal:", {k: v["cal"] for k, v in out["fwd"].items()})
print("data.js bytes:", len(js))

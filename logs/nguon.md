# Sổ nguồn (cập nhật 2026-10-12 lần 1)
Tên | URL liệt kê mở được | Nhịp | Bài mới nhất đã thấy | Mở thành công gần nhất | Lỗi gần nhất | Nguồn thay thế
Splash247 | https://splash247.com/feed/ ; /category/sector/tankers/feed/ ; /category/sector/dry-cargo/feed/ ; /category/sector/gas/feed/ | hằng ngày | 11/10 21:10 Baltic states push for EU-wide ban on Russian grain transit | 12/10 | bài lẻ HTTP 403 (12/10: boom refuses to peak, recycling drought, tanker war; WebFetch) | đoạn mô tả trong feed (feed chính chỉ có đoạn đầu, không có content:encoded đầy đủ); gCaptain, KI cho cùng tin
Hellenic Shipping News | https://www.hellenicshippingnews.com/feed/ (cần curl -L, trang 1 trả 301; thêm ?paged=2..7) ; danh mục https://www.hellenicshippingnews.com/category/report-analysis/weekly-shipbrokers-reports/ (curl, có link PDF) | hằng ngày + báo cáo tuần (không đăng thứ Bảy; tối Chủ nhật UTC đăng loạt bài ghi ngày thứ Hai) | 11/10 21:00 UTC (ghi 12/10) | 12/10 | không | gCaptain, MarEx
gCaptain | https://gcaptain.com/feed/ (?paged=2..3) | hằng ngày | 11/10 17:31 Republican Senator Says Trump's Russian Diesel Deal May Be Illegal | 12/10 | không | HSN, MarEx
OilPrice.com | https://oilprice.com/rss/main (curl); bài lẻ đọc bằng WebFetch (curl chỉ ra thanh giá) | hằng ngày | 09/10 Isaias 71%; Asian refiners ditch US oil; diesel crisis | 10/10 | không | —
Trading Economics BDI | https://tradingeconomics.com/commodity/baltic ; /brent-crude-oil | ngày làm việc | 09/10: 2.917 (khớp); bài tóm tắt TE vẫn lệch (3.002) | 12/10 | không | build.py
Baltic Exchange tuần theo tuyến | Affinity Tanker Weekly PDF trên HSN (bảng Baltic TCE đủ tuyến tanker, có ngay tối thứ Sáu); The Edge: tìm "Baltic Exchange shipping updates: <ngày>" (đăng Chủ nhật) | thứ Sáu | tuần 41 (09/10) tanker qua Affinity; BLPG1/3 tuần 41 chưa tìm được | 10/10 (Affinity) | balticexchange.com: trang thử thách/trống (lỗi lặp lại, bỏ qua) | Gibson, Advanced (T/C hàng rời)
Gibson Shipbrokers | https://www.gibsons.co.uk/report/<slug>/ (link từ HSN; curl trả nội dung nén, dùng WebFetch) | thứ Sáu | 09/10 Damage Control (TD14 châu Á) | 10/10 | không | HSN tóm tắt
Fearnleys Weekly | HSN "fearnleys-week-NN-2026" → PDF wp-content/uploads/2026/10/Fearnleys-Weekly-Report-_-Fearnpulse.pdf (tên file có thể trùng giữa các tuần; lấy link từ trang bài) | thứ Tư (HSN đăng ~21:00 giờ VN; có ở lần chạy sáng thứ Năm) | tuần 41 (07/10) | 08/10 | không | —
ICIS cước tàu hóa chất | HSN đăng lại (tiêu đề "...liquid chem tanker rates..." hoặc "liquid tanker rates ex-US Gulf") | thứ Sáu (HSN thứ Hai) | 28/09 (HSN ?p=1149665, chỉ tuyến Mỹ) | 10/10 (kiểm tra, không có bản mới) | icis.com trang trống/Incapsula (04/10) | HSN
NOAA ENSO | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml | thứ Năm thứ 2 của tháng (~20:00 giờ VN, sau giờ chạy sáng) | 08/10 (El Niño Advisory; kỳ tới 12/11) | 09/10 | không | —
Lloyd's List Red Sea Brief | https://www.lloydslistintelligence.com/resources/blog/red-sea-brief-<ngày> | hằng tuần (thứ Năm) | 01/10 | 04/10 | không | —
Tin PVT | https://cafef.vn/pvtrans.html (curl, -A Mozilla); WebSearch tiếng Việt theo tên tàu ra TNCK, Tiền Phong, Người Quan Sát, pvn.vn | hằng ngày | cafef 27/09; PVN/TNCK 10/10 phủ nhận NV Sunshine | 12/10 | pvtrans.com 503/SSL (bỏ qua); nongnghiepmoitruong.vn 403 (11/10) | tinnhanhchungkhoan.vn, tienphong.vn, pvn.vn
Seatrade, AGBI, zamin.uz, thehill.com | | | | | 403 | bỏ qua, dùng nguồn khác
globalsecurity.org | | | | | 402 | CBS, EA WorldView
marinelink.com | | | | | 502 (04/10) | gCaptain
Lion Shipbrokers (S&P, phá dỡ) | HSN "lion-shipbrokers-weekly-market-report-week-NN-2026" + PDF wp-content/uploads/2026/10/Lion-Weekly-Report-<ngày>-WNN.pdf | thứ Sáu | tuần 41 (09/10) | 10/10 | không | Advanced, GMS
Advanced Shipping & Trading (S&P, bảng giá tàu theo tuổi) | HSN "advanced-shipping-trading-weekly-shipping-market-report-week-NN-2026" + PDF ADVANCED-MARKET-REPORT-WEEK-NN.pdf | thứ Sáu | tuần 41 (09/10) | 10/10 | không | Lion
Affinity Tanker Weekly (Baltic TCE đủ tuyến, có TC7 châu Á) | HSN "affinity-tanker-weekly-<ngày>" + PDF Affinity-Tanker-Weekly-DD.MM.2026-HSN.pdf | thứ Sáu (HSN tối thứ Sáu giờ VN) | 09/10 | 10/10 | không | The Edge
Xclusiv | HSN "xclusiv-shipbrokers-weekly-<ngày>" + PDF wp-content/uploads/2026/10/xclusiv-2026_10_05.pdf | thứ Hai | 05/10 (tuần 40) | 06/10 | không | Lion, Advanced
The Maritime Executive | trang chủ https://maritime-executive.com/ (curl, lấy /article/<slug>) ; bài lẻ mở được (curl) | hằng ngày | 09/10 More tankers struck as IRGC expands threat (Kpler: dầu vùng Vịnh −1/3) | 10/10 | không | —
cnbc.com, cnn.com (451), malaymail.com, lloydslist.com | | | | | 403/451 (05/10) | The National, ABC/AP, Tribune
Star Asia (hàng rời châu Á, giá tàu theo tuổi, S&P, phá dỡ) | HSN "star-asia-shipbroking-weekly-market-report-week-NN-5" + PDF wp-content/uploads/2026/10/Market-Report-Week-NN.pdf (curl + pdftotext) | thứ Sáu (HSN đăng tối Chủ nhật UTC, ghi thứ Hai) | tuần 41 (09/10) | 12/10 | không | Xclusiv
Clarksons Hellas SnP | HSN "clarksons-hellas-snp-weekly-NN" + PDF Weekly-Sales-<ngày>.pdf | thứ Sáu | 09/10 | 10/10 | không | Star Asia
Veson Nautical (triển vọng quý) | HSN "shipping-market-outlook-q4-2026" | hằng quý | 06/10 (Q4 2026) | 06/10 | không | —
usnews.com (503), detroitnews.com (402), scmp.com (403) | | | | | 06/10 | Alhurra, Anews, Aaj, Epoch Times, The National
argusmedia.com | WebFetch trả nội dung trống; curl đọc được | | 15/09 propane | 06/10 (curl) | WebFetch trống | curl
Intermodal Weekly (định hạn 1 năm/3 năm, giá tàu 5 tuổi, S&P) | HSN "intermodal-weekly-market-report-week-NN-2026-brokers-insight" + PDF wp-content/uploads/2026/10/Intermodal-Report-Week-NN-2026.pdf (curl + pdftotext) | thứ Ba | tuần 40 (06/10) | 07/10 | trang HSN chỉ có đoạn đầu | Banchero
Banchero Costa Weekly (định hạn MR/LR/Supra/Handy, tuyến châu Á S10, HS5, TC11) | HSN "banchero-costa-weekly-market-report-week-NN-2026" + PDF Bancosta-Weekly-2026-NN.pdf | thứ Ba | tuần 40 (06/10) | 07/10 | trang HSN chỉ có đoạn đầu | Intermodal
VesselsValue (Weekly Vessel Valuations, giao dịch kèm định giá) | HSN "weekly-vessel-valuations-report-<ngày>" | thứ Ba | 06/10 | 07/10 | không | Xclusiv
Clarksons ClarkSea (quý) | HSN "clarksons-clarksea-index..." | hằng quý | 07/10 (Q3 2026) | 07/10 | không | —
The National | https://www.thenationalnews.com/news/gulf/ và /news/mena/ (curl, lấy href /news/.../2026/10/DD/...); blog trực tiếp đọc bằng WebFetch | hằng ngày | 11/10 | 12/10 | không | Al Jazeera, Iran International
Al Jazeera | https://www.aljazeera.com/xml/rss/all.xml (curl; nhiều mục là video) | hằng ngày | 11/10 23:20 | 12/10 | không | The National
The Moscow Times | https://www.themoscowtimes.com/rss/news (curl; lấy URL đầy đủ, đừng cắt ngắn — URL cụt trả 404) | hằng ngày | 11/10 14:58 Trump Says Russia and Ukraine Reached Energy Ceasefire | 12/10 | 404 do URL cụt (lỗi của lần chạy) | Kyiv Independent
Kyiv Independent | https://kyivindependent.com/ (curl, lấy href="/<slug>/") | hằng ngày | 11/10 22:57 (FT: Mỹ dọa dừng PURL) | 12/10 | không | Moscow Times
Safety4Sea | bài lẻ mở được (tìm bằng WebSearch allowed_domains) | hằng ngày | 06/10 | 07/10 | không | MarEx
reuters.com, apnews.com | không dùng được trong allowed_domains của WebSearch (API Error 400) | | | | 07/10 | Kyiv Independent, MarEx, The National

UKMTO | ukmto.org/recent-incidents: HTTP 403 (08/10) | hằng ngày | WARNING 158-26 (07/10) | — | 403 (08/10) | Anadolu (aa.com.tr), Middle East Eye live blog, dpa/Yahoo, MarEx
Anadolu Agency | bài lẻ aa.com.tr/en/... mở được (curl) | hằng ngày | 07/10 | 08/10 | không | dpa/Yahoo
Doanh nghiệp cùng ngành (thông cáo) | HSN đăng lại thông cáo/phân tích (SFL, Top Ships, NORDEN, Stolt) | theo sự kiện | 07/10 | 08/10 | không | Splash feed

BIMCO (phân tích thị trường) | HSN đăng lại (tiêu đề phân tích, ví dụ "LR2 demand grows...") | hằng tuần | 09/10 LR2 (Niels Rasmussen) | 09/10 | không | HSN
Signal Group Weekly Market Monitor (dòng than, hàng) | HSN đăng lại | hằng tuần | 09/10 than tháng 9 | 09/10 | không | —
FreightWaves | bài lẻ freightwaves.com/?p=<id> mở được | hằng ngày | 28/09 phí cảng USTR | 09/10 | không | —
GMS (phá dỡ) | HSN "gms-week-NN-..." + PDF Ship-recycling-market-insight-Week-NN-....pdf | thứ Sáu | tuần 41 (09/10) | 10/10 | không | Lion
Banchero Costa (phân tích dòng hàng) | HSN đăng lại (ví dụ "Tanker Market: ...") | hằng tuần | 10/10 dầu thô 9 tháng | 10/10 | không | —
straits.live (bản tin Hormuz hằng ngày: tàu chờ, PortWatch, Brent, lời IRGC) | https://straits.live/briefs/YYYY-MM-DD | hằng ngày | 11/10 (152 tàu chờ) | 12/10 | không | Euronews, The National
Euronews | bài lẻ euronews.com/YYYY/MM/DD/<slug> mở được (WebFetch) | hằng ngày | 09/10 IRGC strikes tanker | 11/10 | không | —
The New Arab, Yeni Şafak (Anadolu) | bài lẻ mở được (WebFetch); dùng thay Tasnim/Tehran Times | hằng ngày | 09/10 NV Sunshine | 11/10 | không | —
tasnimnews.ir, tehrantimes.com | | | | | HTTP 503 (11/10) | Yeni Şafak/Anadolu, New Arab
MagicPort (hồ sơ tàu, AIS) | https://magicport.ai/vessels/gas-carrier/<tên>-mmsi-<mmsi> | theo nhu cầu | NV Sunshine (đích Ras Laffan) | 11/10 | không | —
Fox Weather (bão Đại Tây Dương) | bài lẻ foxweather.com/weather-news/<slug> mở được | theo sự kiện | 09/10 Isaias vào bờ | 11/10 | mypanhandle.com, newsnationnow.com 403 (11/10) | —
Iran International (blog trực tiếp, có giờ) | https://www.iranintl.com/en/liveblog/<id> (tìm qua WebSearch) | hằng ngày | 11/10 23:08 (Petro Dolphin, Valthera, Rezaei) | 12/10 | không | JPost, Gulf News
The Jerusalem Post, Gulf News | bài lẻ mở được (WebFetch) | hằng ngày | 11–12/10 Iran bác phản hồi Mỹ | 12/10 | không | —
IANS, The Tribune (ANI) | bài lẻ mở được (WebFetch); aninews.in 403 | hằng ngày | 12/10 Petro Dolphin | 12/10 | aninews.in 403 (12/10) | Tribune
Energy Intelligence | bài lẻ energyintel.com/<id> mở được phần tóm tắt (WebFetch) | theo sự kiện | 09/10 Trung Quốc xuất xăng dầu 3,64 triệu tấn | 12/10 | không | Reuters qua báo địa phương (centraloregondaily.com), voiceofemirates.com
Signal Group (Tanker Market Monitor), PVM, Platts, Norne | HSN đăng lại (tiêu đề phân tích) | hằng tuần | 12/10 | 12/10 | không | —
Baird Maritime (tanker news roundup) | bài lẻ bairdmaritime.com mở được | vài lần/tuần | 09/10 | 12/10 | không | —
brecorder.com, benzinga.com | | | | | 403 (12/10) | JPost, Gulf News

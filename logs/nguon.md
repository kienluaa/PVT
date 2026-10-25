# Sổ nguồn (cập nhật 2026-10-25 lần 1)
Tên | URL liệt kê mở được | Nhịp | Bài mới nhất đã thấy | Mở thành công gần nhất | Lỗi gần nhất | Nguồn thay thế
Splash247 | https://splash247.com/feed/ ; /category/sector/tankers/feed/ ; /category/sector/dry-cargo/feed/ ; /category/sector/gas/feed/ | hằng ngày | 13/10 20:00 Splash Cruise launches…; Tankers 13/10 11:33 Emarat 6 LR1 | 18/10 (bài lẻ 200 hôm nay) | bài lẻ HTTP 403 (14/10: iran-threatens-ships-going-dark, emarat, two-more-ships-hit-off-bulgaria; curl + WebFetch) | đoạn mô tả trong feed; gCaptain, MarEx, The National cho cùng tin
Hellenic Shipping News | https://www.hellenicshippingnews.com/feed/ (curl -L; ?paged=2..9) ; danh mục https://www.hellenicshippingnews.com/category/report-analysis/weekly-shipbrokers-reports/ (curl) ; tìm kiếm ?s=<từ khóa> (curl) | hằng ngày + báo cáo tuần | 13/10 21:00 UTC (ghi 14/10) | 14/10 | không | gCaptain, MarEx, Baird
gCaptain | https://gcaptain.com/feed/ (?paged=2..3) | hằng ngày | 13/10 20:26 Port of LA record; 18:48 Saudi strikes Houthi | 14/10 | không | HSN, MarEx
OilPrice.com | https://oilprice.com/rss/main (curl); bài lẻ đọc bằng WebFetch (curl chỉ ra thanh giá) | hằng ngày | 12/10 19:00 | 13/10 | không | —
Trading Economics BDI | https://tradingeconomics.com/commodity/baltic ; /brent-crude-oil ; /iron-ore | ngày làm việc | 13/10: 2.801 (khớp) | 14/10 | không | build.py
Baltic Exchange tuần theo tuyến | Affinity Tanker Weekly PDF trên HSN (tanker, tối thứ Sáu); khí: HSN đăng bài Baltic tiêu đề kiểu "LNG Shipping Market Softer, But LPGs On the Rise Again" (thứ Hai, có BLPG1–3 TCE); Xclusiv (thứ Hai) có TD8, TD14 và tuyến hàng rời S3TC/S11TC/HS7TC; The Edge: tìm "Baltic Exchange shipping updates" | thứ Sáu | tuần 41 (09/10) đủ tanker, gas, dry | 13/10 | balticexchange.com: trang thử thách/trống (lỗi lặp lại, bỏ qua) | Gibson, Advanced
Gibson Shipbrokers | https://www.gibsons.co.uk/report/<slug>/ (link từ HSN; curl trả nội dung nén, dùng WebFetch) | thứ Sáu | 09/10 Damage Control (TD14 châu Á) | 10/10 | không | HSN tóm tắt
Fearnleys Weekly | HSN "fearnleys-week-NN-2026" → PDF wp-content/uploads/2026/10/Fearnleys-Weekly-Report-_-Fearnpulse.pdf (tên file có thể trùng giữa các tuần; lấy link từ trang bài) | thứ Tư (HSN đăng ~21:00 giờ VN; có ở lần chạy sáng thứ Năm) | tuần 41 (07/10) | 08/10 | không | —
ICIS cước tàu hóa chất | HSN đăng lại (tiêu đề "...liquid chem tanker rates..." hoặc "liquid tanker rates ex-US Gulf") | thứ Sáu (HSN thứ Hai) | 28/09 (HSN ?p=1149665, chỉ tuyến Mỹ) | 10/10 (kiểm tra, không có bản mới) | icis.com trang trống/Incapsula (04/10) | HSN
NOAA ENSO | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml | thứ Năm thứ 2 của tháng (~20:00 giờ VN, sau giờ chạy sáng) | 08/10 (El Niño Advisory; kỳ tới 12/11) | 09/10 | không | —
Lloyd's List Red Sea Brief | https://www.lloydslistintelligence.com/resources/blog/red-sea-brief-<ngày> | hằng tuần (thứ Năm) | 01/10 | 04/10 | không | —
Tin PVT | https://cafef.vn/pvtrans.html (curl, -A Mozilla; mã ngày trong URL dạng -18826MMDD…) ; WebSearch tiếng Việt theo tên tàu ra TNCK, Tiền Phong, Người Quan Sát, pvn.vn | hằng ngày | cafef 27/09; PVN/TNCK 10/10 phủ nhận NV Sunshine | 13/10 | pvtrans.com 503/SSL (bỏ qua) | tinnhanhchungkhoan.vn, tienphong.vn, pvn.vn
Seatrade, AGBI, zamin.uz, thehill.com | | | | | 403 | bỏ qua, dùng nguồn khác
globalsecurity.org | | | | | 402 | CBS, EA WorldView
marinelink.com | | | | | 502 (04/10) | gCaptain
Lion Shipbrokers (S&P, phá dỡ) | HSN "lion-shipbrokers-weekly-market-report-week-NN-2026" + PDF wp-content/uploads/2026/10/Lion-Weekly-Report-<ngày>-WNN.pdf | thứ Sáu | tuần 41 (09/10) | 10/10 | không | Advanced, GMS
Advanced Shipping & Trading (S&P, bảng giá tàu theo tuổi) | HSN "advanced-shipping-trading-weekly-shipping-market-report-week-NN-2026" + PDF ADVANCED-MARKET-REPORT-WEEK-NN.pdf | thứ Sáu | tuần 41 (09/10) | 10/10 | không | Lion
Affinity Tanker Weekly (Baltic TCE đủ tuyến, có TC7 châu Á) | HSN "affinity-tanker-weekly-<ngày>" + PDF Affinity-Tanker-Weekly-DD.MM.2026-HSN.pdf | thứ Sáu (HSN tối thứ Sáu giờ VN) | 09/10 | 10/10 | không | The Edge
Xclusiv | HSN "xclusiv-shipbrokers-weekly-<ngày>" + PDF wp-content/uploads/2026/10/xclusiv-2026_10_12.pdf (curl + pdftotext; bảng tuyến sản phẩm có thể lặp số, kiểm tra trước khi dùng) | thứ Hai (HSN tối Chủ nhật/thứ Hai UTC) | 12/10 (tuần 41 số liệu) | 13/10 | không | Lion, Advanced
The Maritime Executive | trang chủ https://maritime-executive.com/ (curl với UA Chrome đầy đủ, grep "/article/<slug>") ; bài lẻ mở được (curl) | hằng ngày | 13/10 Bulgaria calls for EU/NATO aid; Iran IMO protest | 14/10 | không | —
cnbc.com, cnn.com (451), malaymail.com, lloydslist.com | | | | | 403/451 (05/10) | The National, ABC/AP, Tribune
Star Asia (hàng rời châu Á, giá tàu theo tuổi, S&P, phá dỡ) | HSN "star-asia-shipbroking-weekly-market-report-week-NN-5" + PDF wp-content/uploads/2026/10/Market-Report-Week-NN.pdf (curl + pdftotext) | thứ Sáu (HSN đăng tối Chủ nhật UTC, ghi thứ Hai) | tuần 41 (09/10) | 12/10 | không | Xclusiv
Clarksons Hellas SnP | HSN "clarksons-hellas-snp-weekly-NN" + PDF Weekly-Sales-<ngày>.pdf | thứ Sáu | 09/10 | 10/10 | không | Star Asia
Veson Nautical (triển vọng quý) | HSN "shipping-market-outlook-q4-2026" | hằng quý | 06/10 (Q4 2026) | 06/10 | không | —
usnews.com (503), detroitnews.com (402), scmp.com (403) | | | | | 06/10 | Alhurra, Anews, Aaj, Epoch Times, The National
argusmedia.com | WebFetch trả nội dung trống; curl đọc được | | 15/09 propane | 06/10 (curl) | WebFetch trống | curl
Intermodal Weekly (định hạn 1 năm/3 năm, giá tàu 5 tuổi, S&P, đặt đóng, phá dỡ) | HSN "intermodal-weekly-market-report-week-NN-2026-brokers-insight" + PDF wp-content/uploads/2026/10/Intermodal-Report-Week-NN-2026.pdf (curl + pdftotext) | thứ Ba (HSN đăng ~04:00 giờ VN thứ Tư, có ở lần chạy sáng thứ Tư) | tuần 41 (13/10) | 14/10 | trang HSN chỉ có đoạn đầu | Banchero
Banchero Costa Weekly (định hạn MR1/MR2/LR2, TC11, rổ MR, S10, HS5, FFA, S&P chi tiết) | HSN "banchero-costa-weekly-market-report-week-NN-2026" + PDF Bancosta-Weekly-2026-NN.pdf | thứ Ba (có ở lần chạy sáng thứ Tư) | tuần 41 (13/10) | 14/10 | trang HSN chỉ có đoạn đầu | Intermodal
VesselsValue (Weekly Vessel Valuations, giao dịch kèm định giá) | HSN "weekly-vessel-valuations-report-<ngày>" ; trang mục /category/weekly-vessel-valuations-report/ | thứ Ba (bản 13/10 chưa đăng lúc 07:30 thứ Tư) | 06/10 | 14/10 (kiểm tra) | không | Xclusiv
Clarksons ClarkSea (quý) | HSN "clarksons-clarksea-index..." | hằng quý | 07/10 (Q3 2026) | 07/10 | không | —
The National | https://www.thenationalnews.com/news/gulf/ và /news/mena/ (curl UA Chrome, lấy href /news/.../2026/10/DD/...) | hằng ngày | 13/10 Hormuz attacks surge (≥12 tàu/tuần); Saudi–Houthi oil installations | 14/10 | không | Al Jazeera
Al Jazeera | https://www.aljazeera.com/xml/rss/all.xml (curl; nhiều mục là video/thể thao, lọc từ khóa) | hằng ngày | 13/10 19:33 Trump says Houthis trying to increase oil prices | 14/10 | không | The National
The Moscow Times | https://www.themoscowtimes.com/rss/news (curl; lấy URL đầy đủ) | hằng ngày | 13/10 18:57; 12:57 Ukraine Holds Off Refinery Attacks for Second Day | 14/10 | không | Kyiv Independent
Kyiv Independent | https://kyivindependent.com/ (curl, lấy href="https://kyivindependent.com/<slug>/") | hằng ngày | 13/10 (Trump không cáo buộc Nga; tình báo Mỹ chưa cắt) | 14/10 | không | Moscow Times
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
straits.live (bản tin Hormuz hằng ngày: tàu chờ, PortWatch, Brent, lời IRGC) | https://straits.live/briefs/YYYY-MM-DD (bản ngày D đăng ~21:30 UTC ngày D) | hằng ngày | 13/10 (141 tàu chờ) | 14/10 | không | Euronews, The National
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
Baird Maritime (tin tàu dầu, hàng rời, khí; Reuters đăng lại) | https://www.bairdmaritime.com/shipping/tankers ; /shipping/dry-cargo ; /shipping/tankers/gas (curl, lấy link bài) ; bài lẻ mở được | hằng ngày | 13/10 Vortexa Iran exports zero, LPG −48%; Urals freight India | 14/10 | không | —
brecorder.com, benzinga.com | | | | | 403 (12/10) | JPost, Gulf News
OPEC MOMR | HSN đăng lại tóm tắt ("OPEC raises 2027 oil demand outlook…"); OilPrice | hằng tháng (~13 hằng tháng) | tháng 10 (13/10) | 14/10 | không | —
tinnhanhchungkhoan.vn | trang tag PVT https://www.tinnhanhchungkhoan.vn/pvtrans-pvt-tag120180.html | | | | curl (35) Connection reset (14/10) | cafef
Cập nhật 2026-10-15:
Alibra Weekly Tanker/Dry TC Estimates | HSN "weekly-tanker-time-charter-estimates-<ngày>" (bảng là ảnh PNG/JPG trong bài: 1410tanker.png, 1410dry.png) | thứ Tư (HSN chiều thứ Tư) | 14/10 | 15/10 | không | Intermodal, Fearnleys
Fearnleys Weekly | tuần 42 PDF: wp-content/uploads/2026/10/Fearnleys-Weekly-Report-_-Fearnpulse-1.pdf (tên file đổi hậu tố -1); KHÔNG có mục tàu dầu SP và tàu hóa chất; "market brief" Brent lệch (83,97) – không dùng | thứ Tư | tuần 42 (14/10) | 15/10 | không | —
VesselsValue | bản 13/10 đăng HSN 14/10 17:00 UTC (có ở lần chạy sáng thứ Năm, không có ở sáng thứ Tư) | thứ Ba | 13/10 | 15/10 | không | —
IEA OMR | iea.org 403 (Cloudflare); HSN đăng lại văn bản ("Escalation of attacks threatens…" 15/10), TBS/AFP | hằng tháng (~14) | 14/10 | 15/10 | iea.org 403 (15/10) | HSN, tbsnews.net
A News (Anadolu) | bài lẻ anews.com.tr/middle-east/2026/10/DD/<slug> mở được (lượt tàu Hormuz, Kpler) | hằng ngày | 14/10 | 15/10 | không | —
Insurance Business (phí bảo hiểm chiến tranh) | bài lẻ insurancebusinessmag.com/us/news/breaking-news/<slug>.aspx | theo sự kiện | 14/10 (6–10% thân tàu) | 15/10 | không | straits.live/strait-of-hormuz-war-risk-insurance-rate
straits.live | /briefs/YYYY-MM-DD (bản ngày D chưa có lúc 07:00 giờ VN ngày D+1 → dùng D−1) ; /peace-talks ; /strait-of-hormuz-war-risk-insurance-rate | hằng ngày | 14/10 | 15/10 | /briefs/2026-10-15 404; /insurance 404 | —
PetroTimes (petrovietnam.petrotimes.vn) | trang chủ (curl, lấy link -7465xx.html); bài lẻ mở được | hằng ngày | 14/10 PVTrans giải chuyển đổi số; 12/10 Dung Quất mở rộng | 15/10 | root 404 nhưng lấy được link | VietNamNet, Tiền Phong
Federal Register API | https://www.federalregister.gov/api/v1/documents/<số>.json ; trang HTML chuyển sang unblock.federalregister.gov | theo sự kiện | USTR phí cảng: tạm dừng đến 9/11/2026, chưa có văn bản gia hạn (15/10) | 15/10 | trang HTML chặn | Riviera
SMM (news.metal.com) | bài lẻ (WebFetch; curl có bài trả JS rỗng) | hằng ngày | 14/10 hải quan Trung Quốc tháng 9 | 15/10 | 104156085 trống | TokenPost, OilPrice
iea.org, cnbc.com, washingtontimes.com, english.alarabiya.net, easternherald.com, spglobal.com, north-standard.com, state.gov, brownfieldagnews.com, wikifarmer.com | | | | | 403 (15/10) | HSN, TBS, yourNEWS, Kyiv Independent, Federal Register
bernama.com (connection reset), usnews.com (timeout/HTTP2 lỗi) | | | | | 15/10 | TBS, NBC
Cập nhật 2026-10-16:
Báo cáo tuần Baltic theo tuyến | The Edge "Baltic Exchange shipping updates: Oct 9, 2026" = theedgemalaysia.com/node/821285 (đăng chủ nhật 11/10, curl OK, không có TD8/TD14/TC7/TC11) | thứ Sáu | tuần 41 (09/10) | 16/10 (kiểm tra) | tuần 42 chưa ra lúc 07:00 thứ Sáu | Affinity trên HSN (tối thứ Sáu)
EIA WPSR | https://www.eia.gov/petroleum/supply/weekly/pdf/table1.pdf ; table2.pdf ; https://ir.eia.gov/wpsr/psw00.csv (bản tóm tắt wpsrsummary.pdf đã ngừng từ 23/9/2026; trang HTML nạp số bằng JS) | thứ Tư (lễ: thứ Năm) | 15/10 (tuần đến 9/10) | 16/10 | không | OilPrice
JMIC (lượt qua Hormuz) | qua gCaptain "By the Numbers…" | theo khuyến cáo | 15/10 (121 lượt 11–14/10) | 16/10 | ukmto.org bỏ qua | straits.live, hormuz.now/oil
Newsquawk | https://www.newsquawk.com/headlines/<slug> (tiêu đề có giờ UTC) | hằng ngày | 14/10 Oman | 16/10 | không | — (thay Tehran Times/Borna/AVA: connection reset/503)
The National | feed https://www.thenationalnews.com/arc/outboundfeeds/rss/?outputType=xml ; liveblog chỉ có tiêu đề | hằng ngày | 15/10 | 16/10 | không | —
Iran International | feed https://www.iranintl.com/en/feed | hằng ngày | 14/10 | 16/10 | không | —
Kyiv Independent | https://kyivindependent.com/news-archive/rss/ (15 mục) ; /tag/energy/ ; /tag/black-sea/ | hằng ngày | 15/10 22:06 GMT | 16/10 | không | Moscow Times
Baird Maritime | trang mục /shipping/dry-cargo/bulkers (curl; JSON-LD có datePublished); /feed và /stories.rss rỗng | hằng ngày | 15/10 BDI | 16/10 | RSS rỗng | TE
JTWC, NHC | https://www.metoc.navy.mil/jtwc/rss/jtwc.rss ; /jtwc/products/wpNN26web.txt, prog.txt ; https://www.nhc.noaa.gov/index-at.xml | theo bão | 15/10 21Z (29W Champi) | 16/10 | nhc gtwo_atl.xml 404 | NCHMF
NCHMF | https://www.nchmf.gov.vn/kttv/vi-VN/1/tin-du-bao-gio-manh-song-lon-va-mua-dong-tren-bien-post<số>.html | hằng ngày | 16/10 04h | 16/10 | không | —
Kênh Panama | https://pancanal.com/en/maritime-services/advisory-to-shipping/ (/en/category/advisories/ 404) | theo thông báo | A-38-2026 | 16/10 | không | —
Lịch tài chính doanh nghiệp cùng ngành | Inderes (inderes.fi/.se/releases/...), Hafnia PDF s201.q4cdn.com, odfjell.com/investors/ | — | TORM 4/11, Odfjell 4/11, Hafnia 18/11 | 16/10 | globenewswire, stocktitan 403 | —
Federal Register | /api/v1/public-inspection-documents/current.json (gọi 1 lần; /documents.json bị chặn IP) | hằng ngày | 16/10: không có văn bản USTR | 16/10 | 403 IP blocked (documents.json) | —
VTV (giá xăng dầu) | bài lẻ vtv.vn (moit.gov.vn connection reset/404) | thứ Năm hằng tuần | 15/10 | 16/10 | moit.gov.vn | baotintuc
Clarksons ClarkSea/phá dỡ (nguồn thứ hai) | shipuniverse.com, indiashippingnews.com, marineinsight.com, indexbox.io | hằng tuần | ClarkSea 84.951 (tuần đến 9/10); 273 tàu 9 tháng | 16/10 | en.portnews.ru connection reset | —
france24.com, consilium.europa.eu, fas.usda.gov, lloydslist.com, globenewswire.com | | | | | 403 (16/10) | gCaptain, MarEx, AgBull
tehrantimes.com, borna.news, avapress.com, aa.com.tr RSS | | | | | connection reset/503 (16/10) | Newsquawk, The National
pvtrans.com | | | | | SSL lỗi 60 (16/10) | cafef
brsshipbrokers.com/market-reports | | | | | 404 (16/10) | —
Optima Shipbroking (Baltic tanker theo tuyến, ngày) | https://www.optimashipbroking.com/market-report/dirty-tanker-index-summary-DD-month-2026/ và clean-tanker-index-summary-… (bản ghi ngày D chứa số Baltic ngày D−1) | ngày làm việc | 16/10 (số 15/10) | 17/10 | trang danh mục /market-report/ và bản 17/10: 404 (17/10) | Affinity, The Edge
FreightX (bảng chỉ số dry theo tuyến + FFA FIS) | https://freightx.gr/reports/ | ngày làm việc | 16/10 | 17/10 | không | The Edge
The Edge "Baltic Exchange shipping updates" | WebSearch thường chỉ ra bản tuần trước; dùng ô tìm kiếm của The Edge để ra node mới (16/10: node/822176). Bài đăng ~13:00 UTC thứ Sáu, trước giờ chốt tanker, nên số tanker và khí là của thứ Năm, số dry là của thứ Sáu | thứ Sáu | 16/10 | 17/10 | không | Affinity
Allied Weekly Market Review | Cyprus Shipping News "allied-weekly-market-review-week-NN" + PDF wp-content/uploads/2026/10/ALLIED-Weekly-Market-Report-Week-NN.pdf (http bị connection reset, dùng https) | thứ Hai (Cyprus SN đăng thứ Sáu) | tuần 41 (16/10) | 17/10 | curl (35) với http | Advanced
Best Oasis (phá dỡ) | HSN "best-oasis-weekly-recycling-market-report-<ngày>" | thứ Sáu | 16/10 | 17/10 | không | GMS
Sofia Globe, Insurance Journal (Biển Đen, Hội đồng châu Âu) | bài lẻ mở được | theo sự kiện | 16/10 | 17/10 | consilium.europa.eu 403 (16–17/10) | Kyiv Independent
DefenceWeb, SWZ Maritime | bài lẻ mở được | hằng ngày | 16/10 | 17/10 | không | —
mezha.net, spglobal.com, euromaidanpress | | | | | 403 (17/10) | Moscow Times, Kyiv Independent
OFAC Recent Actions (quyết định trừng phạt chính thức) | https://ofac.treasury.gov/recent-actions ; /recent-actions/YYYYMMDD | theo sự kiện | 16/10 GL 60A Venezuela (không có quyết định tàu bóng tối) | 18/10 | không | —
JTWC / JMA (bão Tây Thái Bình Dương) | https://www.metoc.navy.mil/jtwc/products/wp<số><năm>web.txt và ...prog.txt ; https://www.jma.go.jp/bosai/typhoon/data/TC<năm><số>/specifications.json | 6 giờ/lần khi có bão | Champi 29W cảnh báo 14 (17/10 21Z); JMA 18/10 06:45 JST | 18/10 | không | NCHMF, PAGASA
NCHMF (bão Biển Đông) | https://nchmf.gov.vn | hằng ngày | 18/10 04h không có ATNĐ/bão | 18/10 | không | —
ReCAAP ISC (cướp biển châu Á, báo cáo tuần PDF) | https://www.recaap.org/reports (lấy link PDF từ trang này, không đoán URL) | hằng tuần | tuần 06–12/10 | 18/10 | URL đoán 404 (18/10) | IMB qua MarEx
China-Global South Project (lọc dầu, xuất khẩu nhiên liệu TQ) | bài lẻ chinaglobalsouth.com/YYYY/MM/DD/<slug> mở được | hằng ngày | 17/10 crack xăng châu Á | 18/10 | không | —
Breakwave Advisors (phân tích hàng rời của BRS) | https://www.breakwaveadvisors.com/insights | hằng tuần | 16/10 bauxite Guinea | 18/10 | không | —
Optima Shipbroking (Clean Tanker Index, có TC12/TC22, rổ MR Atlantic) | optimashipbroking.com/market-report/... ; wp-json/wp/v2 | ngày làm việc | 16/10 (số 15/10); bản 17/10 404 | 18/10 | 404 bản 17/10 | Affinity
Shafaq News (an ninh Yemen/Vịnh Aden, dẫn UKMTO) | bài lẻ shafaq.com/en/... mở được | hằng ngày | 17/10 tàu LNG bị bắn (UKMTO 176-26) | 18/10 | không | gCaptain
icis.com | | | | | Incapsula 212 byte (18/10) | HSN đăng lại
Tanker Operator, bimco.org/news, comprerural, canalrural, benzinga | | | | | 403 (18/10) | HSN, MarEx
tinnhanhchungkhoan.vn | | | | | curl 35 connection reset (18/10) | cafef, petrotimes
Cập nhật 2026-10-19:
UKMTO | PDF cảnh báo https://www.ukmto.org/-/media/ukmto/products/YYYYMMDD-ukmto_warning_NNN-26.pdf (thấy qua WebSearch) | hằng ngày | WARNING 177-26 (18/10) | — | 403 cả PDF (19/10, curl + WebFetch) | anews.com.tr, Arab News (Reuters), CBS live updates
straits.live | /briefs/YYYY-MM-DD | hằng ngày | 18/10 (đóng dấu 19/10 00:05Z, mở được lúc 00:15 UTC 19/10) | 19/10 | không | — ; ghi chú: bản 18/10 KHÔNG có số tàu chờ
Arab News (Reuters đăng lại) | bài lẻ arabnews.com/saudi-arabia/<slug>-<id> mở được (WebFetch) | hằng ngày | 17/10 tàu dầu trúng vật thể ngoài khơi Jubail | 19/10 | không | Emirates 24/7, SANA
CBS News live updates (tổng hợp có giờ) | https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-of-hormuz-yemen-houthis-saudi-arabia/ (WebFetch) | hằng ngày | 18/10 15:02 EDT | 19/10 | không | Fox live
anews.com.tr (Anadolu, dẫn UKMTO) | bài lẻ /world/YYYY/MM/DD/<slug> mở được | hằng ngày | 18/10 tàu kéo Khor Fakkan | 19/10 | không | Shafaq, aninews
Iran International | feed https://www.iranintl.com/en/feed (curl 200) + bài /en/<id> (WebFetch) | hằng ngày | 18/10 19:36 | 19/10 | không | —
OFAC Recent Actions | https://ofac.treasury.gov/recent-actions (curl 200) | theo sự kiện | 16/10 | 19/10 | không | —
ReCAAP ISC | https://www.recaap.org/reports ; /alerts (curl 200) | hằng tuần | weekly 06–12/10 | 19/10 | không | —
Kpler blog | KHÔNG đoán URL tracker theo ngày (6 URL đoán 404, 19/10); tìm qua WebSearch | không đều | 1/10 | — | 404 (URL đoán) | Safety4Sea, Reuters đăng lại
tankermap.com | /analytics/straits/hormuz mở được nhưng số tự mâu thuẫn → chỉ tham khảo | — | 18/10 | 19/10 | không | —
Kyiv Independent | https://kyivindependent.com/news-archive/rss/ ; /tag/black-sea/ (curl, grep 'kyivindependent.com/<slug>') | hằng ngày | 18/10 22:34 GMT | 19/10 | không | Moscow Times
The Moscow Times | https://www.themoscowtimes.com/rss/news | hằng ngày | 18/10 12:53 St. Petersburg | 19/10 | không | KI
AP qua ABC News/NBC News | bài lẻ abcnews.com/International/wireStory/<slug>-<id> ; nbcnews.com/world/... (WebFetch) | hằng ngày | 18/10 St. Petersburg | 19/10 | không | —
OilPrice.com | https://oilprice.com/rss/main (curl -L) | hằng ngày | 18/10 18:00 | 19/10 | không | —
Trading Economics Brent | /commodity/brent-crude-oil (WebFetch) | ngày | 19/10 108,10 | 19/10 | không | FX Leaders
EIA WPSR | table1.pdf (curl 200) | thứ Tư | tuần đến 09/10 | 19/10 (kiểm tra) | không | —
OPEC MOMR | opec.org, momr.opec.org: curl 403 (19/10); dùng The Star/HSN đăng lại | tháng | 13/10 | 19/10 | 403 | The Star (thestar.com.my)
Hellenic Shipping News | /feed/?paged=1..4 (curl -L) | hằng ngày | 36 bài ghi 18/10 21:00 UTC | 19/10 | không | —
ENGINE (engine.online) | /news 301 khi curl; đọc qua HSN đăng lại (tồn kho Singapore, Mỹ) | hằng ngày | 19/10 | 19/10 | 301 | HSN
FX Leaders, The Peninsula Qatar | bài lẻ mở được (WebFetch) | hằng ngày | 18/10 giá dầu | 19/10 | không | —
Swarajya, noinotizie.it | bài lẻ mở được | theo sự kiện | 18/10, 16/10 | 19/10 | không | —
chinaglobalsouth.com | /feed/ HTTP 410 (19/10); bài lẻ vẫn mở được (18/10) | | 17/10 | 18/10 | 410 feed | —
russiamatters.org, deccanherald.com, agenzianova.com, opec.org | | | | | 403 (19/10) | ABC/AP, Swarajya, noinotizie, The Star
Xclusiv | HSN "xclusiv-shipbrokers-weekly-<ngày>" | thứ Hai | 12/10 | 19/10 (kiểm tra) | bản 19/10 chưa đăng lúc 00:14 UTC 19/10 (lần chạy 07:00 giờ VN thứ Hai thường chưa có) | Lion, Advanced
Clarksons Hellas SnP | HSN "clarksons-hellas-snp-weekly-13" = Weekly-Sales-9th-October-2026.pdf | thứ Sáu (đăng HSN trễ, có thể sau thứ Hai) | 09/10 | 19/10 | không | Advanced
Lion, Star Asia | HSN | thứ Sáu | W41 | 19/10 | W42 chưa lên HSN lúc 00:14 UTC 19/10; starasiashipbroking.com, starasia-sg.com: curl (56) CONNECT tunnel failed 502; lionshipbrokers.gr không có trang báo cáo | Advanced
ICIS cước tàu hóa chất | HSN đăng lại, tiêu đề kiểu "Asia-US container rates mixed…; tanker rates stable" (mục LIQUID CHEMICAL TANKERS) | thứ Sáu (HSN thứ Hai) | 16/10 | 19/10 | không | —
Baltic khí: BLPG1 công bố thứ Ba và thứ Năm (Circular 16/26 từ 7/4/2026) | balticexchange.com/en/data-services/WeeklyRoundup/Gas/News/2026/gas-report-week-NN.html → "Challenge Validation" (19/10) | — | — | — | challenge | The Edge, HSN
Splash "Weekly Broker" | không tìm thấy mục; /tag/weekly-broker/feed/ trả Cloudflare "Just a moment..." (19/10) | — | — | — | Cloudflare | feed chính
Cyprus Shipping News | https://cyprusshippingnews.com/feed/ (curl) | hằng ngày (không đăng cuối tuần) | 16/10 02:40 UTC | 19/10 | không | —
Baltic tuần theo tuyến | HSN đăng lại bản tuần Baltic tanker + dry vào tối Chủ nhật UTC (HSN ghi thứ Hai): slug kiểu "vlcc-tanker-rates-retreated-last-week", "dry-bulk-market-capesizes-declined-slightly-last-week" (tìm qua feed, tiêu đề đổi theo tuần; cuối bài "Source: Baltic Exchange"); số tanker là số thứ Năm như The Edge, có thêm TD33, TD28, TD29, TC15, TC23 | thứ Sáu | tuần 42 (19/10) | 19/10 | — | The Edge, Affinity
Xclusiv | slug HSN dạng "xclusiv-shipbrokers-weekly-12th-october-2026" (số thứ tự có đuôi th/st/rd) ; 19th chưa có lúc 00:15 UTC thứ Hai | thứ Hai | 12/10 | 19/10 (kiểm tra) | 404 (19/10, chưa đăng) | —
MarineLink | https://www.marinelink.com/news (200, link /news/<slug>-<id>) | hằng ngày | 18/10 | 19/10 | /rss/news 404 (19/10) | gCaptain
Dry Bulk Magazine | trang chủ https://www.drybulkmagazine.com/ (link /<mục>/<ddmmyyyy>/<slug>/) | hằng ngày | 15/10 | 19/10 | /rss/ trả "Article Not Found" | —
SMM (news.metal.com) Iron Ore Weekly Brief | bài lẻ newscontent/<id> (WebFetch OK) | thứ Sáu | 16/10 | 19/10 | — | Mysteel
NBS Trung Quốc | https://www.stats.gov.cn/english/PressRelease/ (curl 200) | theo lịch | 15/10 CPI/PPI | 19/10 | — | —
PAGASA | https://www.pagasa.dost.gov.ph/tropical-cyclone/severe-weather-bulletin (WebFetch OK) | theo bão | 19/10 không có bão trong PAR | 19/10 | — | JMA
miningweekly.com | | | | | 403 (19/10) | Mysteel
bimco.org | | | | | 403 / Azure WAF (19/10) | HSN ?s=BIMCO
Everstream port congestion | https://www.everstream.ai/risk-centers/port-congestion-report-DD-month-2026/ | hằng tuần | 14/10 | 19/10 | — | —
Tin PVT | https://cafef.vn/pvtrans.html (curl -A Mozilla); CBTT: https://cafef.vn/du-lieu/Ajax/Events_RelatedNews_New.aspx?symbol=<MÃ>&floorID=0&configID=0&PageIndex=1&PageSize=6&Type=2 (PVT, PVP, PDV, VOS, VTO, GSP, BSR, PVS); PDF CBTT ở cafefnew.mediacdn.vn/download/<ddmmyy>/... (scan, đọc bằng pdftoppm) | hằng ngày | PVT 27/09; PDV 16/10 NQ 38 | 19/10 | pvtrans.com bỏ qua (lỗi lặp lại) | petrotimes, baoxaydung
PetroTimes (petrovietnam.petrotimes.vn) | trang chủ (curl, link -7468xx.html); bài lẻ WebFetch OK | hằng ngày | 18/10 22:37 ĐBQH Lê Ngọc Sơn (746838) | 19/10 | không | VietNamNet, Tiền Phong
Vietstock | https://vietstock.vn/rss/doanh-nghiep.rss trả HTML (không phải RSS); dùng WebSearch allowed_domains vietstock.vn | hằng ngày | 05/10 PVT Logistics xin ý kiến cổ đông | 19/10 (tìm kiếm) | RSS không dùng được (19/10) | cafef CBTT
Federal Register | /api/v1/public-inspection-documents/current.json qua WebFetch (3 đoạn offset); curl bị chặn IP | hằng ngày | 19/10–20/10 (nộp 16/10): không có văn bản USTR | 19/10 | curl HTTP 403 "address has been blocked" (19/10) | —
SEC EDGAR (DN cùng ngành niêm yết Mỹ) | https://data.sec.gov/submissions/CIK<10 số>.json (curl, UA có email liên hệ chung) → lọc filingDate; tài liệu https://www.sec.gov/Archives/edgar/data/<cik>/<accession>/<file> | theo sự kiện | INSW 8-K 16/10; Hafnia, TORM 6-K 13/10; DHT 6-K 13/10 | 19/10 | không | globenewswire/stocktitan (403)
Pacific Basin | bản chép lời investing.com (OK); gurufocus (tường phí sau mở đầu) | quý (trading update giữa tháng 1/4/7/10) | Q3 15/10 | 19/10 | không | pacificbasin.com chưa thử
Cập nhật 2026-10-20:
Optima Shipbroking (Baltic tanker theo tuyến hằng ngày, LPG/petchem) | https://www.optimashipbroking.com/market-reports/ (trang liệt kê; /market-report/ không có chữ s trả 404) ; bài dạng /market-report/dirty-tanker-index-summary-DD-month-YYYY/ , /lpg-petchem-market-report-DD-month-YYYY/ | ngày làm việc (số của phiên trước) | 19/10 (dirty: số 16/10; LPG: định hạn VLGC và LPG nhỏ Đông/Tây) | 20/10 | clean 19/10 404 | Xclusiv
FreightX (hàng rời theo tuyến hằng ngày + FFA FIS) | https://freightx.gr/reports/ (dữ liệu tuyến nhúng trong HTML) | ngày làm việc | 19/10 tuần 43 | 20/10 | không | The Edge
Baltic khí tuần (HSN) | HSN tiêu đề kiểu "LNG, Gas Shipping Rates Under Pressure" (Source: Baltic Exchange), đăng thứ Hai | tuần | 19/10 (tuần đến 16/10) | 20/10 | không | Optima LPG
Kpler blog | https://www.kpler.com/blog/<slug> (mở được) | theo sự kiện | 19/10 LPG shuttle trade | 20/10 | không | —
ENGINE (bunker, tồn kho ARA/Singapore, EIA) | https://engine.online/news/<slug> | ngày | 19/10 East of Suez | 20/10 | không | —
BOE Report (Reuters đăng lại) | https://boereport.com/YYYY/MM/DD/<slug>/ | ngày | 19/10 Bousso | 20/10 | không | —
Gulf News | bài lẻ gulfnews.com/world/mena/<slug> mở được | ngày | 19/10 | 20/10 | không | Al Jazeera
Mekong ASEAN (tin BSR, doanh nghiệp năng lượng) | bài lẻ mekongasean.vn/<slug>.html | ngày | 19/10 BSR dầu nội địa 88% | 20/10 | không | petrotimes
SEC EDGAR (doanh nghiệp cùng ngành) | https://www.sec.gov/Archives/edgar/data/<CIK>/... (6-K exhibit 99.1); submissions JSON | theo DN | 19/10 Scorpio lịch quý 3 (28/10) | 20/10 | không | HSN
zoom.earth (bão, dữ liệu JTWC) | https://zoom.earth/storms/<tên>-2026/ | theo bão | Champi 21:00 UTC 19/10 | 20/10 | không | NCHMF
aa.com.tr (20/10: không kết nối), bne IntelliNews, oilandgas360, S&P Global (403), globenewswire, torm.com | | | | | 20/10 | anews.com.tr, HSN
Cập nhật 2026-10-21:
straits.live | /briefs/YYYY-MM-DD | hằng ngày | 20/10 (đóng dấu 15:28 UTC, có số tàu chờ 115) | 21/10 | không | —
OFAC Recent Actions | https://ofac.treasury.gov/recent-actions (curl 200) | theo sự kiện | 19/10 PAIPA | 21/10 | không | —
ReCAAP ISC | https://www.recaap.org/reports (curl 200, link PDF dạng /resources/ck/files/reports/weekly/2026/ReCAAP%20ISC%20Weekly%20Report%20(DD-DD%20Mon)%202026.pdf) | hằng tuần (bản tuần đăng ~thứ Ba sau tuần) | tuần 13–19/10 + Q3 2026 | 21/10 | không | —
Riviera Maritime Media | bài lẻ rivieramm.com/news-content-hub/<slug>-<id> (curl 200) | hằng ngày | 19/10 (tên VLCC ST3, Loyalty; Kpler lượt qua eo) | 21/10 | không | —
The Peninsula Qatar (dẫn UKMTO) | bài lẻ thepeninsulaqatar.com/article/DD/MM/YYYY/<slug> (curl 200) | hằng ngày | 20/10 | 21/10 | không | Euronews
Euronews | bài lẻ euronews.com/YYYY/MM/DD/<slug> (curl 200) | hằng ngày | 20/10 | 21/10 | không | —
United24 Media | bài lẻ united24media.com/world/<slug>-<id> (curl 200) | hằng ngày | 20/10 | 21/10 | không | —
Seoul Economic Daily (en.sedaily.com) | bài lẻ (curl 200) | hằng ngày | 20/10 | 21/10 | không | —
energynews.pro | | | | | 403 (21/10) | United24
Gulf News live | bài lẻ /world/mena/<slug>-1.5007xxxxx (curl 200; WebFetch lấy được mục theo giờ) | hằng ngày | 21/10 03:59 GST | 21/10 | không | —
Kpler blog | https://www.kpler.com/blog (curl 200) | vài ngày | Hormuz mới nhất 9/10 | 21/10 | không | Riviera/Bloomberg dẫn Kpler
- OilPrice.com | https://oilprice.com/rss/main (curl); bài lẻ chỉ đọc được bằng WebFetch; URL bài mới lấy từ thanh bên của một bài bất kỳ (curl, grep oilprice.com/Latest-Energy-News) | hằng ngày | 20/10 19:00 | 21/10 | không | —
- Trading Economics Brent/WTI | /commodity/brent-crude-oil ; /commodity/crude-oil (WebFetch) | ngày | 21/10: Brent 109,50, WTI 98,49 (HĐ tháng 12 sau khi HĐ tháng 11 đáo hạn 20/10) | 21/10 | không | Yahoo UK Finance
- Marinelink (Reuters đăng lại) | https://www.marinelink.com/news/<slug>-<id> (curl OK) | ngày | 20/10 Russian diesel cargoes | 21/10 | không | Baird Maritime
- Breakwave Tanker Report | HSN /breakwave-tanker-report-MM-DD-YYYY/ → PDF wp-content/uploads/YYYY/MM/BreakwaveTankers<Month><DD>YYYYReport.pdf (curl 200) | 2 tuần | 20/10 | 21/10 | không | —
- Gulf Times (Reuters đăng lại) | bài lẻ /article/<id>/... /amp (WebFetch) | theo sự kiện | 18/10 PetroChina Dalian | 21/10 | không | NST (chỉ ra tiêu đề)
- brecorder.com | | | | | Cloudflare "Just a moment..." (21/10) | Yahoo UK Finance
- euromaidanpress.com | | | | | 403 (21/10, lặp lại) | KI, MT
Intermodal Weekly | HSN "intermodal-weekly-market-report-week-NN-2026-brokers-insight" + PDF Intermodal-Report-Week-NN-2026.pdf | thứ Ba (HSN 21:00 UTC thứ Ba = 04:00 giờ VN thứ Tư) | W42 20/10 | 21/10 | không | Banchero
Banchero Costa Weekly | HSN "banchero-costa-weekly-market-report-week-NN-2026" + PDF Bancosta-Weekly-2026-NN.pdf | thứ Ba (HSN 21:00 UTC) | W42 (số 16/10) | 21/10 | không | Intermodal
VesselsValue | trang mục https://www.hellenicshippingnews.com/category/weekly-vessel-valuations-report/ (curl, liệt kê slug) ; slug "weekly-vessel-valuations-report-october-20-2026" | thứ Ba | 20/10 (đã có lúc 00:20 UTC thứ Tư) | 21/10 | slug "-20th-" 404 | Xclusiv
Optima Shipbroking | https://www.optimashipbroking.com/wp-json/wp/v2/market-report?per_page=20&_fields=date,link (liệt kê bài kèm ngày, ổn định hơn trang /market-reports/) | ngày làm việc; LPG & Petchem thứ Hai | clean/dirty 20/10 | 21/10 | lpg-petchem 20/21-10 404 (không phát hành) | —
BW LPG (thông cáo) | Inderes: https://www.inderes.se/releases/bwlpg-bw-lpg-limited-announces-sale-of-<tên tàu> | theo sự kiện | 20/10 BW Loyalty | 21/10 | bwlpg.com/investors/news/ 404 | Splash247
Athenian Shipbrokers (phá dỡ) | HSN "athenian-shipbrokers-s-a-demolition-quick-update-week-NN-2026" + PDF Week_NN_Athenian_Demolition_Report_2026.pdf | thứ Hai/Ba | W42 20/10 | 21/10 | PDF chủ yếu là hình, ít số | GMS, Best Oasis
Alibra | HSN slug "weekly-tanker-time-charter-estimates-october-21-2026" | thứ Tư (chưa có lúc 00:30 UTC) | 14/10 | 15/10 | 404 21/10 00:30 UTC (chưa đăng) | Intermodal, Banchero
- Optima Shipbroking | https://www.optimashipbroking.com/wp-json/wp/v2/market-report?per_page=8&_fields=slug,date (curl, 200: liệt kê slug+giờ đăng UTC) ; bài /market-report/dirty-tanker-index-summary-DD-october-2026/ | ngày làm việc, ~10:00 UTC (bản ngày D chứa số Baltic ngày D−1; lần chạy sáng giờ VN chỉ có số D−2) | 20/10 (số 19/10) | 21/10 | 21/10: dirty 20/10 lần 1 HTTP 520 rồi 200; bản 21/10 404 (chưa đăng) | FreightX, Banchero
- FreightX | https://freightx.gr/reports/ (curl; tuyến trong JS `routes`, FFA bid/offer trong mảng ["Nov 26",bid,offer]) | ngày làm việc, cập nhật ~12:50 UTC | 20/10 | 21/10 | không | —
- Banchero Costa Weekly | HSN feed → /banchero-costa-weekly-market-report-week-NN-2026/ + PDF wp-content/uploads/2026/10/Bancosta-Weekly-2026-NN.pdf (curl, pdftotext) | thứ Ba (HSN 21:00 UTC thứ Ba) | tuần 42 (20/10; số 16/10, FFA 18/10; có TC11 TCE) | 21/10 | không | Intermodal
- ENGINE | https://engine.online/news (curl; link /news/<slug>) | hằng ngày | 20/10 East of Suez outlook | 21/10 | không | HSN đăng lại
- SteelOrbis | bài tin /steel-news/latest-news/… mở được; trang giá /steel-prices/… tường phí | hằng ngày | 15/10 | 21/10 | tường phí (giá quặng 20/10) | HSN MMI
- Mining Weekly | — | — | — | — | 21/10 HTTP 403 "Just a moment..." | SteelOrbis
- JTWC | https://www.metoc.navy.mil/jtwc/rss/jtwc.rss ; products/wp2926web.txt, wp2926prog.txt | 6 giờ | Champi cảnh báo 26 (20/10 21Z) | 21/10 | không | ENGINE/HKO qua HSN
- NCHMF | https://nchmf.gov.vn/kttv/ (curl) → tin-du-bao-gio-manh-song-lon-va-mua-dong-tren-bien-post54353.html | hằng ngày | 04h 21/10 | 21/10 | không | —
- Kênh Panama | https://pancanal.com/en/maritime-services/advisory-to-shipping/ (curl, link PDF wp-content/uploads/2026/10/) | theo thông báo | A-38 (9/10) | 21/10 | không | HSN
Tin PVT – BCTC theo mã | https://cafef.vn/du-lieu/Ajax/PageNew/FileBCTC.ashx?Symbol=<MÃ>&Type=1&Year=2026 (curl, JSON: Time, Name, Link PDF) | quý | PVT/PVP/PDV/VOS/VTO/GSP/BSR: mới nhất Q2/2026 (đến 07:10 21/10) | 21/10 | không | Ajax CBTT cafef
Oslo Børs (thông báo DN cùng ngành) | POST https://api3.oslo.oslobors.no/v1/newsreader/list?category=&issuer=&fromDate=YYYY-MM-DD&toDate=YYYY-MM-DD&market=&messageTitle= (curl; tham số issuer không lọc được, lọc theo issuerSign: BWLPG, HAFNI, ODF, SNI, AGAS, OET, FRO, KCC) | hằng ngày | 20/10 07:30 BWLPG bán BW Loyalty; 20/10 KCC mời họp Q3 | 21/10 | không | Splash feed
SEC EDGAR (DN cùng ngành) | CIK: STNG 1483934, DHT 1331284, INSW 1679049, FRO 913290, TNK 1419945, TRMD 1655891, HAFN 1815779, ECO 1964954, ASC 1577437, SBLK 1386716, GNK 1326200, BWLP 1649313, CMBT 1604481, NVGS 1581804, LPG 1596993 | theo DN | 20/10 BWLP 6-K (BW Loyalty) | 21/10 | không | Oslo API
Federal Register (EO/USTR) | https://www.federalregister.gov/api/v1/public-inspection-documents/current.json (curl 200 hôm nay với UA ngắn; WebFetch cũng OK); PDF https://public-inspection.federalregister.gov/<số>.pdf (curl 200) | hằng ngày | nộp 20/10: EO 14436 (Graham Act, miễn trừ vô thời hạn); không có USTR | 21/10 | không | —
Star Bulk | https://www.starbulk.com/gr/en/press-releases/ (curl, có ngày) | theo DN | 09/10 Hermes World Maritime | 21/10 | không | EDGAR SBLK
norden.com/investors/company-announcements | | | | | 404 (21/10) | WebSearch
genco.com | | | | | curl 56 CONNECT 502 (21/10) | EDGAR GNK
teekay.com, pacificbasin.com (trang IR) | | | | | danh sách JS, không đọc được (21/10) | EDGAR TNK
Cập nhật 2026-10-22:
gCaptain | https://gcaptain.com/feed/ (curl 200) | hằng ngày | 21/10 20:35 UTC Panama Canal traffic…; 15:12 Two More Tankers Struck | 22/10 | không | HSN, MarEx
straits.live | /briefs/YYYY-MM-DD (bản 21/10 đóng dấu 22/10 00:05Z, mở được 00:15 UTC 22/10; có số tàu chờ 90 lúc 03:22 UTC) ; /strait-of-hormuz-war-risk-insurance-rate (số liệu 07/10) | hằng ngày | 21/10 | 22/10 | không | —
OFAC Recent Actions | https://ofac.treasury.gov/recent-actions ; /recent-actions/20261021 (curl 200) | theo sự kiện | 21/10 Iran-related (9 tàu hàng khô/dịch vụ, GL GG/HH, Russia GL 131K) | 22/10 | không | gCaptain
ReCAAP ISC | https://www.recaap.org/reports (curl 200) | hằng tuần | vẫn tuần 13–19/10 | 22/10 | không | Safety4Sea
The National | feed RSS (curl 200) + bài lẻ WebFetch | hằng ngày | 22/10 00:01 | 22/10 | không | —
Al Jazeera | RSS all.xml (curl 200) + bài lẻ WebFetch | hằng ngày | 21/10 23:20 | 22/10 | không | —
Iran International | feed /en/feed (curl 200) + bài /en/<id> (WebFetch) | hằng ngày | 21/10 22:26 | 22/10 | không | —
Al Arabiya | | | | | english.alarabiya.net bài lẻ 403 (22/10, WebFetch) | Iran Intl, gCaptain
UANI Iran Shipping Update | | 2 lần/tuần | 20/10 | — | 403 (22/10) | gCaptain By the Numbers
MND Đài Loan (PLA quanh Đài Loan) | https://www.mnd.gov.tw/en/news/plaactlist (curl 200) → /En/News/PLAAct/<id> | hằng ngày | 21/10 (88041) | 22/10 | không | —
Inquirer (số tàu TQ ở Biển Đông, AFP Philippines) | bài lẻ inquirer.net/<id>/<slug> (WebFetch) | hằng tuần | 21/10 | 22/10 | không | —
EEAS (europa.eu) | | | | | 403 (22/10) | Law360/CNBC
Kyiv Independent | https://kyivindependent.com/news-archive/rss/ ; /tag/energy/ ; /tag/black-sea/ (curl, grep 'kyivindependent.com/<slug>/') | hằng ngày | 21/10 23:46 GMT Lipetsk | 22/10 | không | Moscow Times
The Moscow Times | https://www.themoscowtimes.com/rss/news (curl) | hằng ngày | 21/10 21:46 | 22/10 | không | KI
OilPrice.com | https://oilprice.com/rss/main (curl); bài lẻ WebFetch | hằng ngày | 21/10 19:00 | 22/10 | không | —
Trading Economics Brent/WTI | /commodity/brent-crude-oil ; /commodity/crude-oil (WebFetch) | ngày | 22/10: Brent 110,01, WTI ~98,07 | 22/10 | không | HSN (ICIS)
EIA WPSR | table1.pdf, table2.pdf (công suất lọc), table4.pdf (Cushing), psw00.csv (chỉ tồn kho thô) | thứ Tư | tuần đến 16/10 (21/10) | 22/10 | không | OilPrice
Hellenic Shipping News | /feed/?paged=1..6 (curl -L) ; ?s=<từ khóa> | hằng ngày | 21/10 21:00 UTC (trang bài ghi 22/10) | 22/10 | không | —
OPEC MOMR | (opec.org 403 lặp lại – bỏ qua) | tháng | 13/10 | — | 403 (19/10) | HSN, The Star
Baird Maritime | https://www.bairdmaritime.com/shipping/tankers (curl; grep 'bairdmaritime.com/shipping/tankers/<slug>'); bài lẻ curl, ngày trong "datePublished" | hằng ngày | 21/10 17:47 UTC Urals ~80 USD | 22/10 | không | —
BOE Report (Reuters) | boereport.com/YYYY/MM/DD/<slug>/ (WebFetch) | ngày | 21/10 Exxon Joliet | 22/10 | không | —
marinelink.com/news/maritime/tanker | | | | | curl 403 (22/10) | Baird Maritime
Fearnleys Weekly | tuần 43 PDF: wp-content/uploads/2026/10/Fearnleys-Weekly-Report-_-Fearnpulse-2.pdf (hậu tố tăng mỗi tuần: W42 -1, W43 -2); HSN đăng 21:00 UTC thứ Tư (ghi 22/10); có mục LPG nhỏ: HDY SR 20-22k, SR 6.5k, ETH 8-12k, Coaster Europe 3.500–5.000 cbm (USD/tháng) | thứ Tư | W43 (21/10) | 22/10 | không | —
Alibra | HSN slug weekly-tanker-time-charter-estimates-october-21-2026 và weekly-dry-…; ảnh DDMMYYYYtanker.png / DDMMYYYYdry.png (21102026tanker.png), tuần trước dùng DDMMtanker.png (1410tanker.png) – lấy link từ trang bài | thứ Tư (HSN 17:00 UTC) | 21/10 | 22/10 | không | Intermodal
EIA xuất khẩu/tồn propane tuần | https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=W_EPLLPZ_EEX_NUS-Z00_MBBLD&f=W (xuất) ; s=WPRSTUS1 (tồn) (curl 200) | thứ Tư | tuần đến 16/10 | 22/10 | không | —
Riviera Maritime Media | trang mục news-content-hub: HTTP 429 (22/10, curl) – bài lẻ trước đây 200 | — | — | — | 429 | WebSearch
Cyprus SN Allied | W42 chưa đăng lúc 00:30 UTC 22/10 (404) | thứ Sáu | W41 | 22/10 kiểm tra | 404 | —
SEC EDGAR | data.sec.gov/submissions/CIK##########.json (curl với User-Agent, 200) | theo DN | 21/10 INSW 8-K | 22/10 | không | Oslo API
Optima: wp-json `?_fields=` vẫn trả cả trường `acf` chứa TOÀN BỘ số tuyến (rate_value, rate_change, tce, tce_change), chuyến thực tế, giá bunker → không cần mở bài lẻ. Bài lẻ dirty 21/10: curl 403 (mới), WebFetch OK. Clean 21/10 chưa đăng lúc 00:20 UTC 22/10.
FreightX: đến 00:20 UTC 22/10 vẫn bản 20/10 → bản 21/10 trễ hoặc không phát hành; thay thế: Fearnleys Weekly PDF (thứ Tư) có bảng "Rates" gồm C5, C9, C10, P1A, P2A, P3A, P4, S1C, S10 đúng số Baltic ngày phát hành (đã đối chiếu khớp với FreightX phiên trước).
ADMIS Singapore "Ag Market View" https://admis.com.sg/ag-market-view-for-oct-DD-2026 (curl 200; bản ngày D đăng tối D giờ Mỹ) — ngũ cốc: flash sale USDA, xuất Brazil theo tháng, SovEcon/IKAR.
Breakwave insights https://www.breakwaveadvisors.com/insights (curl 200, link /insights/2026/MM/DD/slug) — bài Commodore/Signal hàng rời gần như hằng ngày.
Alibra dry TC: HSN "weekly-dry-time-charter-estimates-<ngày>" là ẢNH (wp-content/uploads/2026/10/DDMM2026dry.png) → tải ảnh và đọc.
turkishstraits.com: trang /demo/gplan-* (tàu chờ) nạp bằng JS → không lấy được số tàu chờ Bosphorus bằng curl.
IRI ENSO https://iri.columbia.edu/our-expertise/climate/forecasts/enso/current/ (WebFetch OK, cập nhật ~ngày 19 hằng tháng).
Everstream: bản 20/21/22-10 404; mysteel.net trang chủ curl reset (35).
Taipei Times bài lẻ WebFetch OK; malaymail.com 403 → dùng malaysia.news.yahoo.com.
Vietstock | bài lẻ vietstock.vn/2026/10/<slug>-<số>.htm đọc được bằng WebFetch (22/10, bài 1504597) | hằng ngày | 20/10 17:33 Vietcap về PVT | 22/10 | trang danh sách/RSS vẫn JS/HTML | cafef CBTT. → bỏ nhãn "CHƯA XÁC MINH (trang JS)" cho bài lẻ.
cafef trang CBTT chi tiết: URL trong Ajax dạng /du-lieu/VOS-3003130/... trả 301 sang chữ thường; dùng curl -L; PDF ở cafefnew.mediacdn.vn/download/<ddmmyy>/<slug>-0.pdf (scan, đọc bằng pdftoppm -r 80). | 22/10 OK
cafef FileBCTC.ashx: VOS có Q3/2026 (21/10 16:21); VTO đã giải trình Q3 nhưng chưa có file BCTC Q3 trong danh mục (07:15 22/10); PVT, PVP, PDV, GSP, BSR mới nhất Q2/2026.
Oslo Børs API: chi tiết tin GET https://api3.oslo.oslobors.no/v1/newsreader/message?messageId=<id> (curl, JSON body) | 22/10 OK.
Splash247 bài lẻ: 21/10 'shipping-equities-turn-geopolitical-risk-into-an-advantage' và 20/10 'uk-shipowners-warn-against-copying-fueleu-red-tape' mở được bằng WebFetch (không 403). Feed chuyên mục quy định: https://splash247.com/category/sector/regulatory/feed/ (curl 200).
tienphong.vn bài lẻ WebFetch OK (17/10 NSRP).
uniindia.com bài lẻ WebFetch OK (16/10). blogs.tradlinx.com OK (bài 14/8).
Cập nhật 2026-10-25:
Báo cáo tuần Baltic theo tuyến | The Edge "Baltic Exchange shipping updates: Oct 23, 2026" = theedgemalaysia.com/node/823074 (đăng 12:57 UTC thứ Sáu; curl, đọc __NEXT_DATA__; số tanker/gas là của thứ Năm, dry là thứ Sáu; có BLPG1–3) ; Affinity Tanker Weekly PDF (TCE thứ Sáu, không có TD8/TD14) ; Optima wp-json https://www.optimashipbroking.com/wp-json/wp/v2/market-report?per_page=12 (HTTP 403 nhưng thân JSON đủ, trường acf có số tuyến) ; FreightX https://freightx.gr/reports/ (bảng tuyến hàng rời S1B–S15, HS1–HS7, FFA) | thứ Sáu | tuần 43 (23/10) | 25/10 | The Edge search 404, API 502 | Gibson
Lion Shipbrokers | PDF wp-content/uploads/2026/10/Lion-Weekly-Report-23-October-2026-W43.pdf | thứ Sáu | tuần 43 | 25/10 | không | Clarksons Hellas
Clarksons Hellas | PDF wp-content/uploads/2026/10/Weekly-Sales-23rd-October-2026.pdf | thứ Sáu | 23/10 | 25/10 | không | Lion
Best Oasis (phá dỡ) | PDF wp-content/uploads/2026/10/Weekly-Ship-Recycling-Report-17-October-23-October-2026.pdf | thứ Sáu | 23/10 | 25/10 | không | GMS
Advanced, Star Asia | slug tuần 43 trên HSN trả 404 lúc 07:15 Chủ nhật (thường đăng thứ Hai) | thứ Sáu | tuần 42 | 25/10 (kiểm tra) | 404 | Lion, Clarksons
OPEC MOMR | opec.org, momr.opec.org: 403 (curl) | hằng tháng | 13/10 | — | 403 (25/10) | HSN ?s=OPEC
cyprusshippingnews.com | dùng bản không có www (www lỗi SSL) | hằng ngày | 23/10 BIMCO Number of the Week | 25/10 | www: SSL | —
ENGINE (engine.online/news) | bài lẻ mở được (tồn kho ARA, Singapore, Brent) | hằng ngày | 23/10 | 25/10 | không | —
Federal Register public inspection | https://public-inspection.federalregister.gov/<số>.pdf mở được | theo sự kiện | 2026-21755 (USTR, 23/10) | 25/10 | không | gCaptain
moit.gov.vn (giá xăng dầu) | bài điều hành giá lấy từ WebSearch, không tự đoán URL (URL đoán trả 404) | 10 ngày/lần (thứ Năm) | 22/10 | 25/10 | 404 URL đoán | —
JTWC / JMA | metoc.navy.mil/jtwc/products/wpNNNNweb.txt, abioweb.txt (io9126web.txt 403); jma.go.jp/bosai/typhoon/data/TC26NN/specifications.json | theo bão | 24/10 | 25/10 | io 403 | NCHMF
gulfbusiness.com, TradeWinds | | | | | 403 / tường phí (25/10) | The National, Lion

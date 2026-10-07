# Sổ nguồn (cập nhật 2026-10-07 lần 1)
Tên | URL liệt kê mở được | Nhịp | Bài mới nhất đã thấy | Mở thành công gần nhất | Lỗi gần nhất | Nguồn thay thế
Splash247 | https://splash247.com/feed/ ; /category/sector/tankers/feed/ ; /category/sector/dry-cargo/feed/ ; /category/sector/gas/feed/ | hằng ngày | 06/10 Shipping rewinds the future | 07/10 | bài lẻ HTTP 403 (07/10: Tanker attacks around Hormuz, Exmar, Taylor Maritime, Bunker prices) | thẻ description trong feed chuyên mục; HSN/gCaptain/MarEx/Safety4Sea
Hellenic Shipping News | https://www.hellenicshippingnews.com/feed/ (thêm ?paged=2..5 để lấy ~100 bài) ; danh mục https://www.hellenicshippingnews.com/category/report-analysis/weekly-shipbrokers-reports/ (curl, có link PDF) | hằng ngày + báo cáo tuần | 06/10 21:00 (ClarkSea, Banchero, Intermodal) | 07/10 | không | gCaptain
gCaptain | https://gcaptain.com/feed/ (?paged=2..3) | hằng ngày | 06/10 19:53 Iran’s Offshore Oil Stockpile Nears Exhaustion | 07/10 | không | HSN, MarEx
OilPrice.com | https://oilprice.com/rss/main | hằng ngày | 06/10 Why $100 Oil Is Hard to Kill | 07/10 | không | —
Trading Economics BDI | https://tradingeconomics.com/commodity/baltic ; /brent-crude-oil ; /iron-ore | ngày làm việc | 06/10: 3.002 | 07/10 | không | build.py
Baltic Exchange tuần theo tuyến | The Edge: tìm "Baltic Exchange shipping updates: <ngày>" → theedgemalaysia.com/node/<số> (tuần 40 = node/820392) | thứ Sáu (The Edge đăng Chủ nhật) | tuần 40 (02/10) | 04/10 | balticexchange.com: trang thử thách/trống (lỗi lặp lại, bỏ qua) | Gibson (gibsons.co.uk/report/...), HSN
Gibson Shipbrokers | https://www.gibsons.co.uk/report/<slug>/ (link từ HSN) | thứ Sáu | 02/10 Running Out of Room? | 04/10 | không | HSN tóm tắt
Fearnleys Weekly | PDF trên hellenicshippingnews.com (wp-content/uploads); tiêu đề HSN "Fearnleys Week NN 2026" | thứ Tư (HSN đăng chiều/tối giờ VN, sau giờ chạy 07:00) | tuần 40 (30/09) | 07/10 (danh mục) | không | —
ICIS cước tàu hóa chất | HSN đăng lại (tiêu đề "...liquid chem tanker rates...") | thứ Sáu (HSN đăng thứ Hai) | tuần đến 02/10 (HSN 05/10) | 05/10 (qua HSN) | icis.com trang trống/Incapsula (04/10) | HSN
NOAA ENSO | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml | thứ Năm thứ 2 của tháng | 10/09 (kỳ tới 08/10) | 06/10 | không | —
Lloyd's List Red Sea Brief | https://www.lloydslistintelligence.com/resources/blog/red-sea-brief-<ngày> | hằng tuần (thứ Năm) | 01/10 | 04/10 | không | —
Tin PVT | https://cafef.vn/pvtrans.html | hằng ngày | 27/09 | 07/10 | không | vietstock
Seatrade, AGBI, zamin.uz, thehill.com | | | | | 403 | bỏ qua, dùng nguồn khác
globalsecurity.org | | | | | 402 | CBS, EA WorldView
marinelink.com | | | | | 502 (04/10) | gCaptain
Lion Shipbrokers (S&P, phá dỡ) | HSN "lion-shipbrokers-weekly-market-report-week-NN-2026" + PDF wp-content/uploads | thứ Sáu | tuần 40 (02/10) | 05/10 | không | Advanced
Advanced Shipping & Trading (S&P, bảng giá tàu theo tuổi) | HSN "advanced-shipping-trading-weekly-shipping-market-report-week-NN-2026" + PDF | thứ Sáu | tuần 40 (02/10) | 05/10 | không | Lion
Affinity Tanker Weekly (Baltic TCE đủ tuyến, có TC7 châu Á) | HSN "affinity-tanker-weekly-<ngày>" + PDF | thứ Sáu | 02/10 | 05/10 | không | The Edge
Xclusiv | HSN "xclusiv-shipbrokers-weekly-<ngày>" + PDF wp-content/uploads/2026/10/xclusiv-2026_10_05.pdf | thứ Hai | 05/10 (tuần 40) | 06/10 | không | Lion, Advanced
The Maritime Executive | trang chủ https://maritime-executive.com/ (curl, lấy /article/<slug>) ; bài lẻ mở được | hằng ngày | 06/10 tàu dầu cháy gần Sochi | 07/10 | không | —
cnbc.com, cnn.com (451), malaymail.com, lloydslist.com | | | | | 403/451 (05/10) | The National, ABC/AP, Tribune
Star Asia (hàng rời châu Á, giá tàu, S&P) | HSN "star-asia-shipbroking-weekly-market-report-week-NN-N" + PDF wp-content/uploads/2026/10/Market-Report-Week-40.pdf | thứ Sáu (HSN thứ Hai) | tuần 40 (02/10) | 06/10 | không | Xclusiv
Clarksons Hellas SnP | HSN "clarksons-hellas-snp-weekly-NN" | thứ Sáu | 02/10 | 06/10 | không | Star Asia
Veson Nautical (triển vọng quý) | HSN "shipping-market-outlook-q4-2026" | hằng quý | 06/10 (Q4 2026) | 06/10 | không | —
usnews.com (503), detroitnews.com (402), scmp.com (403) | | | | | 06/10 | Alhurra, Anews, Aaj, Epoch Times, The National
argusmedia.com | WebFetch trả nội dung trống; curl đọc được | | 15/09 propane | 06/10 (curl) | WebFetch trống | curl
Intermodal Weekly (định hạn 1 năm/3 năm, giá tàu 5 tuổi, S&P) | HSN "intermodal-weekly-market-report-week-NN-2026-brokers-insight" + PDF wp-content/uploads/2026/10/Intermodal-Report-Week-NN-2026.pdf (curl + pdftotext) | thứ Ba | tuần 40 (06/10) | 07/10 | trang HSN chỉ có đoạn đầu | Banchero
Banchero Costa Weekly (định hạn MR/LR/Supra/Handy, tuyến châu Á S10, HS5, TC11) | HSN "banchero-costa-weekly-market-report-week-NN-2026" + PDF Bancosta-Weekly-2026-NN.pdf | thứ Ba | tuần 40 (06/10) | 07/10 | trang HSN chỉ có đoạn đầu | Intermodal
VesselsValue (Weekly Vessel Valuations, giao dịch kèm định giá) | HSN "weekly-vessel-valuations-report-<ngày>" | thứ Ba | 06/10 | 07/10 | không | Xclusiv
Clarksons ClarkSea (quý) | HSN "clarksons-clarksea-index..." | hằng quý | 07/10 (Q3 2026) | 07/10 | không | —
The National | https://www.thenationalnews.com/news/gulf/ (curl, lấy /news/<mục>/2026/MM/DD/<slug>/) | hằng ngày | 06/10 | 07/10 | không | Al Jazeera
Al Jazeera | https://www.aljazeera.com/xml/rss/all.xml (curl) | hằng ngày | 06/10 | 07/10 | không | The National
The Moscow Times | https://www.themoscowtimes.com/rss/news (curl) | hằng ngày | 06/10 | 07/10 | không | Kyiv Independent
Kyiv Independent | https://kyivindependent.com/ (curl, lấy href="/<slug>/") | hằng ngày | 06/10 | 07/10 | không | Moscow Times
Safety4Sea | bài lẻ mở được (tìm bằng WebSearch allowed_domains) | hằng ngày | 06/10 | 07/10 | không | MarEx
reuters.com, apnews.com | không dùng được trong allowed_domains của WebSearch (API Error 400) | | | | 07/10 | Kyiv Independent, MarEx, The National

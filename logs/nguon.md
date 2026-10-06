# Sổ nguồn (cập nhật 2026-10-06 lần 1)
Tên | URL liệt kê mở được | Nhịp | Bài mới nhất đã thấy | Mở thành công gần nhất | Lỗi gần nhất | Nguồn thay thế
Splash247 | https://splash247.com/feed/ ; /category/sector/tankers/feed/ ; /category/sector/dry-cargo/feed/ ; /category/sector/gas/feed/ | hằng ngày | 05/10 How close is shipping to the top? | 06/10 | bài lẻ HTTP 403 (06/10: How close..., Russia hits four ships) | đoạn đầu bài trong feed chuyên mục; HSN/gCaptain/MarEx
Hellenic Shipping News | https://www.hellenicshippingnews.com/feed/ (thêm ?paged=2..4 để lấy ~80 bài) ; danh mục https://www.hellenicshippingnews.com/category/report-analysis/weekly-shipbrokers-reports/ (curl, có link PDF) | hằng ngày + báo cáo tuần thứ Sáu | 05/10 21:00 (Xclusiv, Kpler, Veson Q4) | 06/10 | không | gCaptain
gCaptain | https://gcaptain.com/feed/ (?paged=2..3) | hằng ngày | 05/10 22:28 Five Hormuz Incidents Reported Monday | 06/10 | không | HSN, MarEx
OilPrice.com | https://oilprice.com/rss/main | hằng ngày | 04/10 Europe's Diesel Woes Just Got Even Worse | 05/10 | không | —
Trading Economics BDI | https://tradingeconomics.com/commodity/baltic ; /brent-crude-oil ; /iron-ore | ngày làm việc | 05/10: 3.070 | 06/10 | không | build.py
Baltic Exchange tuần theo tuyến | The Edge: tìm "Baltic Exchange shipping updates: <ngày>" → theedgemalaysia.com/node/<số> (tuần 40 = node/820392) | thứ Sáu (The Edge đăng Chủ nhật) | tuần 40 (02/10) | 04/10 | balticexchange.com: trang thử thách/trống (lỗi lặp lại, bỏ qua) | Gibson (gibsons.co.uk/report/...), HSN
Gibson Shipbrokers | https://www.gibsons.co.uk/report/<slug>/ (link từ HSN) | thứ Sáu | 02/10 Running Out of Room? | 04/10 | không | HSN tóm tắt
Fearnleys Weekly | PDF trên hellenicshippingnews.com (wp-content/uploads); tiêu đề HSN "Fearnleys Week NN 2026" | thứ Tư | tuần 40 (30/09) | 04/10 | không | —
ICIS cước tàu hóa chất | HSN đăng lại (tiêu đề "...liquid chem tanker rates...") | thứ Sáu (HSN đăng thứ Hai) | tuần đến 02/10 (HSN 05/10) | 05/10 (qua HSN) | icis.com trang trống/Incapsula (04/10) | HSN
NOAA ENSO | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml | thứ Năm thứ 2 của tháng | 10/09 (kỳ tới 08/10) | 06/10 | không | —
Lloyd's List Red Sea Brief | https://www.lloydslistintelligence.com/resources/blog/red-sea-brief-<ngày> | hằng tuần (thứ Năm) | 01/10 | 04/10 | không | —
Tin PVT | https://cafef.vn/pvtrans.html | hằng ngày | 27/09 | 06/10 | không | vietstock
Seatrade, AGBI, zamin.uz, thehill.com | | | | | 403 | bỏ qua, dùng nguồn khác
globalsecurity.org | | | | | 402 | CBS, EA WorldView
marinelink.com | | | | | 502 (04/10) | gCaptain
Lion Shipbrokers (S&P, phá dỡ) | HSN "lion-shipbrokers-weekly-market-report-week-NN-2026" + PDF wp-content/uploads | thứ Sáu | tuần 40 (02/10) | 05/10 | không | Advanced
Advanced Shipping & Trading (S&P, bảng giá tàu theo tuổi) | HSN "advanced-shipping-trading-weekly-shipping-market-report-week-NN-2026" + PDF | thứ Sáu | tuần 40 (02/10) | 05/10 | không | Lion
Affinity Tanker Weekly (Baltic TCE đủ tuyến, có TC7 châu Á) | HSN "affinity-tanker-weekly-<ngày>" + PDF | thứ Sáu | 02/10 | 05/10 | không | The Edge
Xclusiv | HSN "xclusiv-shipbrokers-weekly-<ngày>" + PDF wp-content/uploads/2026/10/xclusiv-2026_10_05.pdf | thứ Hai | 05/10 (tuần 40) | 06/10 | không | Lion, Advanced
The Maritime Executive | bài lẻ mở được (feed RSS trống); tìm bằng WebSearch allowed_domains=maritime-executive.com | hằng ngày | 05/10 tàu cháy buồng máy ngoài Musandam | 06/10 | không | —
cnbc.com, cnn.com (451), malaymail.com, lloydslist.com | | | | | 403/451 (05/10) | The National, ABC/AP, Tribune
Star Asia (hàng rời châu Á, giá tàu, S&P) | HSN "star-asia-shipbroking-weekly-market-report-week-NN-N" + PDF wp-content/uploads/2026/10/Market-Report-Week-40.pdf | thứ Sáu (HSN thứ Hai) | tuần 40 (02/10) | 06/10 | không | Xclusiv
Clarksons Hellas SnP | HSN "clarksons-hellas-snp-weekly-NN" | thứ Sáu | 02/10 | 06/10 | không | Star Asia
Veson Nautical (triển vọng quý) | HSN "shipping-market-outlook-q4-2026" | hằng quý | 06/10 (Q4 2026) | 06/10 | không | —
usnews.com (503), detroitnews.com (402), scmp.com (403) | | | | | 06/10 | Alhurra, Anews, Aaj, Epoch Times, The National
argusmedia.com | WebFetch trả nội dung trống; curl đọc được | | 15/09 propane | 06/10 (curl) | WebFetch trống | curl

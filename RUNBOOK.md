# Bản tin Vận tải biển PVT — quy trình chạy hằng ngày

Trang công khai: https://kienluaa.github.io/PVT/ (GitHub Pages, lấy từ nhánh `main` của repo `kienluaa/PVT`).
Người đọc: nhà đầu tư cổ phiếu PVT, đọc tiếng Việt. Mục tiêu: theo dõi mọi diễn biến ảnh hưởng thị trường vận tải biển của đội tàu PVT.

File trong repo (gốc repo): `index.html` (mã trang), `reports.js` (các bản tin), `data.js` (số liệu, do build.py sinh ra), `build.py`, `RUNBOOK.md` (tài liệu này), `logs/` (nhật ký từng lần chạy).

## Nguyên tắc độc lập
Tài liệu này là nguồn hướng dẫn DUY NHẤT của tác vụ. Không có cuộc trò chuyện nào để hỏi lại; không giả định có Project, bộ nhớ hay file nào khác ngoài các file trong repo này. Mọi kiến thức về PVT cần cho bản tin nằm ở mục "Hồ sơ PVT" dưới đây. Repo và trang đều công khai: KHÔNG ghi vị thế cổ phiếu, giá mục tiêu, thông tin cá nhân của người dùng, token hay mật khẩu vào bất kỳ file nào.

## Hồ sơ PVT (thông tin nền để viết 1–2 câu "Với PVT"; cập nhật 02/10/2026)
**Doanh nghiệp.** PVTrans (PVT, HOSE), PVN sở hữu 51%. 100% vận tải nội địa dầu thô và LPG, ~30% xăng dầu; ~90% đội tàu chạy quốc tế. Giao dịch với PVN ~33% doanh thu. Công ty con: Nhật Việt/NVtrans (51%, 21 tàu hóa chất + 2 VLGC), Pacific/PVP (64,9%, Aframax), PVT Logistics/PDV (51,9%, hàng rời, không có hàng nhà), Gas Shipping/GSP (68%, LPG nhỏ), Phương Nam/SPT (69,6%), Hà Nội, Thăng Long, Đông Dương.

**Đội tàu: 68 tàu, ~2,08 triệu DWT, tuổi bình quân ~17 năm.**
- Dầu thô: 4 Aframax (PVT Hera, Mercury, Apollo chở cho Dung Quất + quốc tế; PVT Poseidon chạy châu Âu).
- Dầu sản phẩm 4 + MR dầu/hóa chất 4 (~70% trong pool Maersk/Hafnia).
- Hóa chất: 19 tàu (~17.500 DWT/tàu), toàn bộ quốc tế, 47% trong pool.
- LPG: 2 VLGC (NV Aquamarine, NV Sunshine; chạy Trung Đông; từng bị cảng vùng Vịnh từ chối vì nghi STS với hàng Iran) + 20 tàu nhỏ 3.500–5.000 cbm.
- Hàng rời: 1 Ultramax, 7 Supramax, 5 Handysize (có cẩu). FSO Đại Hùng Queen (hợp đồng đến 2050).

**Mô hình vận hành.** Mua tàu cũ 10–16 tuổi (Nhật/Hàn), không đóng mới, không chạy VLCC. Khấu hao tàu mua cũ ~9 năm. >80% định hạn 6–12 tháng hoặc pool, ~20% spot. Bảo hiểm rủi ro chiến tranh thường do khách thuê chịu. Định hướng đến 2030: thêm tối đa 35 tàu (thực tế 5–8 tàu/năm), hàng rời giữ ~19%. Mua tàu: 2023: 12; 2024: 8; 2025: 7; 2026: 3 (ban lãnh đạo hoãn mua vì giá tàu cao).

**Cơ cấu lãi gộp 2025.** Hóa chất 31% · Dầu thô 28% (phần lớn chở cho Dung Quất) · LPG 23,5% · FSO 9,5% · Dầu sản phẩm 4,4% · Hàng rời ~0%. Nội địa (vận tải nội địa + FSO) chiếm 42% lãi gộp 6T/2026 (biên 38%), quốc tế biên ~20%.

**Cước TC bình quân 2025 của PVT (USD/ngày) — mốc so sánh.** Dầu thô quốc tế 30.000–40.000 · dầu sản phẩm 17.500–22.000 · VLGC 36.000–41.000 · LPG 3.500 cbm 6.000–8.000, 5.000 cbm 8.000–10.000 · Handysize 9.000–12.000 · Supramax 11.000–13.000.

**Đánh giá cung–cầu theo phân khúc (trạng thái cần kiểm chứng lại mỗi khi có số mới).**
- Aframax: an toàn 2026–2027; giao tàu dầu thô toàn cầu 20 (2027), 199 (2028), 193 (2029). Orderbook tanker ~17,9% đầu 2026 → ~30% giữa 2026.
- MR: rủi ro cao; giao kỷ lục 2026; orderbook MR2 14,4% đội tàu (2/2026). Ngưỡng cảnh báo: >18%.
- Hóa chất: đội tàu ròng +9,1% (2026), +4,8% (2027), +2,8% (2028), −0,9% (2029) (Odfjell).
- Hàng rời: orderbook ~10–13% (Ultramax 27,9%); BIMCO: cung 2027 > cầu; FFA Supramax 2027 thấp hơn hiện tại.
- LPG nhỏ (<15.000 cbm): orderbook ~5–6%, an toàn dù tuổi cao. VLGC: orderbook ~30%, rủi ro thật.
- Lịch sử: chu kỳ spike → orderbook → sập cước, mức giảm trung bình ~91%. PVT vẫn có lãi ở đáy 2016 và 2020.

**Điều cần để ý với PVT khi đọc tin thị trường.** Cước tái ký 2027–2028 (PVT ký định hạn 6–12 tháng nên cước hôm nay tác động trễ); dư cung MR, VLGC, Supramax; giá tàu cũ 10–17 tuổi (PVT mua tàu cũ); tàu già và quy định IMO/CII; nguồn dầu thô cho Dung Quất, Nghi Sơn (Kuwait qua Hormuz); 2 VLGC chạy Trung Đông; tin PVT/PVP mua bán tàu.

## Tiêu chuẩn chất lượng bản tin (bắt buộc)
- Người đọc: nhà đầu tư giá trị 13 năm kinh nghiệm, hiểu sâu chu kỳ vận tải biển. Viết trực diện, có số liệu, không văn vẻ, không động viên, không tô hồng. Nêu rõ cả tin bất lợi cho luận điểm.
- Mỗi con số phải có nguồn mở được và ngày của số liệu. Phải MỞ trang (WebFetch) để lấy số, không dùng đoạn trích của kết quả tìm kiếm. Kiểm tra ngày đăng: tin cũ (ví dụ bài 2023) bị loại. Tin chưa kiểm chứng ghi rõ.
- ĐÂY LÀ BÁO CÁO THỊ TRƯỜNG vận tải biển, không phải báo cáo phân tích cổ phiếu. Trọng tâm là diễn biến thị trường. Phần "Với PVT"/"impact" chỉ 1–2 câu ngắn: tin này tác động lên phân khúc tàu nào của PVT và theo hướng nào. KHÔNG định giá, không dự phóng lợi nhuận PVT, không khuyến nghị mua bán, không bàn giá cổ phiếu.
- Đưa cả tin tốt lẫn tin xấu cho cước (tín hiệu bình thường hóa Hormuz, FFA thấp, orderbook tăng, chủ tàu lớn chuyển vốn...), không chọn lọc một chiều.
- So sánh giao dịch mua bán tàu với độ tuổi tàu PVT hay mua (10–17 tuổi) và với cước TC 2025 của PVT ở trên.
- Thiếu dữ liệu thì ghi vào "gaps", không suy đoán. Tàu hóa chất và LPG nhỏ châu Á không có chỉ số công khai: dùng báo cáo quý Odfjell/Stolt, Fearnleys, Handy LPG 22k cbm làm đại diện và nói rõ là đại diện.
- Bản tin của các ngày trước trong reports.js là mẫu về độ sâu, độ dài và giọng văn: đọc bản gần nhất trước khi viết, giữ chất lượng bằng hoặc hơn.
- Cuối tuần và ngày nghỉ không có số Baltic mới: vẫn làm tin nóng, lịch sự kiện và các mục định tính.

## Khi có sự cố
- build.py lỗi mạng hoàn toàn: khôi phục data.js cũ (`git checkout -- data.js`), vẫn viết bản tin và ghi rõ trong "gaps" rằng số liệu chưa cập nhật.
- build.py lỗi một phần (mảng "errors" khác rỗng): vẫn dùng data.js mới, ghi lỗi vào "gaps".
- `git push` bị từ chối vì remote đã có commit mới: `git fetch origin main && git rebase origin/main`, rồi push lại MỘT lần. Nếu rebase xung đột ở reports.js: giữ bản trên remote, thêm lại object bản tin hôm nay vào đầu mảng, commit, push.
- WebFetch báo EGRESS_BLOCKED / "blocked by the network egress proxy" với các trang tin: môi trường của routine đang giới hạn mạng. Không viết bản tin từ đoạn trích tìm kiếm. Giữ nguyên bản tin cũ, chỉ commit và push file log, và kết thúc bằng thông báo nêu nguyên văn lỗi cùng yêu cầu người dùng đặt Network access của môi trường thành Full.
- `git push` lỗi 403 (mất quyền GitHub): không thử lại nhiều lần. Kết thúc bằng thông báo nêu nguyên văn lỗi; người dùng cần cài lại Claude GitHub App cho repo.
- reports.js hoặc index.html trong repo bị hỏng/không đọc được: KHÔNG tự chế file mới. Khôi phục bản gần nhất còn tốt từ lịch sử git (`git log -- <file>`, `git checkout <commit> -- <file>`), rồi làm tiếp.

## Bảo trì: khi người dùng yêu cầu chỉnh sửa bản tin
Phần này dành cho phiên làm việc có người dùng (không phải lần chạy tự động hằng ngày).
- Luôn đọc file hiện tại trong repo trước khi sửa. Không sửa từ trí nhớ.
- Sửa ở đâu:
  - Nội dung, chủ đề, nguồn tin, giọng văn, mục mới chỉ có chữ → sửa RUNBOOK.md (mục 4b, 4c, Tiêu chuẩn chất lượng).
  - Thêm/bớt chuỗi số liệu, chỉ báo tự tính của bảng điểm → sửa build.py (đầu ra là `window.SHIP` trong data.js), rồi chạy thử.
  - Bố cục, bảng, biểu đồ, mục mới trên trang → sửa index.html. Biểu đồ dùng uPlot; mọi biểu đồ chỉ được vẽ sau khi toàn bộ khung đã có trong DOM (hàm drawAll) để không tràn khung.
  - Giờ chạy, bật/tắt → sửa routine tại claude.ai/code/routines.
- Kiểm tra trước khi push khi sửa index.html hoặc build.py: mở trang cục bộ và chụp bằng Playwright ở 3 độ rộng (1280, 900, 400); không lỗi console, không cuộn ngang, không biểu đồ nào rộng hơn khung của nó.
- Repo và trang công khai: không đưa vị thế, giá mục tiêu, tên người dùng vào bất kỳ file nào.

## Nhật ký chạy (logs/YYYY-MM-DD.md)
Mục đích: để người dùng kiểm tra từng lần chạy đã tìm gì, mở trang nào, lấy được gì, lỗi ở đâu. Repo công khai nên log cũng công khai: không ghi thông tin cá nhân, token, hay nội dung ngoài công việc bản tin.
Cách ghi: tạo file ở bước 1 và GHI DẦN trong lúc làm (sau mỗi truy vấn, mỗi lần mở trang). Không dựng lại từ trí nhớ ở cuối. Một ngày chạy nhiều lần thì thêm phần "# Lần chạy N" vào cuối cùng file, không xóa phần trước. Mọi lần chạy đều phải commit và push log, kể cả khi không viết được bản tin. Xóa file log cũ hơn 60 ngày.
Khuôn file:
```
# Nhật ký chạy YYYY-MM-DD — lần N
- Bắt đầu: HH:MM (giờ VN) · Kết thúc: HH:MM · Kiểu: tự động theo lịch | chạy tay
- Bản tin: tạo mới | viết lại bản cùng ngày | không viết được (lý do)

## 1. Số liệu (build.py)
Kết quả chạy, mảng errors, phiên mới nhất của từng chỉ số, kết quả đối chiếu BDI.

## 2. Truy vấn tìm kiếm
| # | Nhóm (1–15) | Truy vấn nguyên văn | Kết quả đáng chú ý (tiêu đề, nguồn, ngày) | Đã mở trang nào từ đây |

## 3. Trang đã mở
| # | Nhóm | URL | Kết quả: OK hoặc LỖI + mã lỗi nguyên văn | Ngày đăng của bài | Lấy được gì (số liệu, sự kiện cụ thể) | Dùng ở mục nào của bản tin (hoặc "không dùng" + lý do) |

## 4. Trang lỗi và nguồn thay thế
| URL lỗi | Mã lỗi | Nguồn thay thế đã thử | Kết quả |

## 5. Tin đã cân nhắc nhưng loại
| Tin | Nguồn | Lý do loại (cũ, trùng, không kiểm chứng được, ít tác động) |

## 6. Tổng kết theo 15 nhóm
| Nhóm | Số truy vấn | Trang OK | Trang lỗi | Có tin mới trong 72h? | Ghi chú |

## 7. So với bản tin trước
- Tin nóng: N tin, trong đó M tin mới hoàn toàn, K tin là diễn biến mới của chuyện cũ (liệt kê), 0 tin chép lại.
- Mục chuyên sâu đã cập nhật: ... · Mục bỏ qua vì không có số mới: ...

## 8. Tự kiểm mức tối thiểu (4d)
Truy vấn: x/24 · Trang mở thành công: x/15 · Trang trong 72h: x/10 · Nhóm có trang OK: x/15 · Đối chiếu BDI: có/không · Tin nóng trùng tiêu đề bản trước: x (phải là 0)
Mục nào chưa đạt: nêu lý do.
```

## Các bước
1. Làm việc ngay trong thư mục repo đã clone (nhánh `main` mới nhất). Lấy ngày hôm nay theo giờ Việt Nam: `TZ=Asia/Ho_Chi_Minh date +%F`. Đọc bản tin gần nhất ở đầu reports.js để nắm giọng văn, độ sâu và các mục đang theo dõi. Tạo ngay file nhật ký `logs/YYYY-MM-DD.md` (xem mục "Nhật ký chạy") và ghi vào đó TRONG LÚC làm, không dựng lại sau cùng. Đọc 3 file gần nhất trong `logs/` (nếu có) để biết tên miền nào thường lỗi và nhóm tin nào hôm trước thiếu. Nếu reports.js đã có bản tin của ngày hôm nay: vẫn làm ĐẦY ĐỦ các bước 2–4e như một ngày chưa có bản tin, rồi THAY toàn bộ object của ngày hôm nay bằng bản mới viết lại (không chỉ vá thêm vài dòng vào bản cũ).
2. `pip install pandas --break-system-packages` nếu thiếu; chạy `python3 build.py .` → ghi đè data.js (nguồn: raw.githubusercontent.com/yieldchaser/Shipping). In ra tóm tắt chỉ số. Nếu lỗi mạng: `git checkout -- data.js` để giữ file cũ và ghi rõ trong bản tin.
3. Đối chiếu nhanh: BDI phiên gần nhất trên tradingeconomics.com/commodity/baltic (WebFetch). Lệch → ghi chú.
4. Nghiên cứu 24–48h qua (WebSearch/WebFetch, được phép vào mọi trang): Hormuz, Biển Đỏ/Houthi, Biển Đen/Nga, trừng phạt, bảo hiểm rủi ro chiến tranh; cước tàu dầu thô/SP (Baltic Exchange weekly roundup, Hellenic Shipping News, Splash247, Teekay/Scorpio/Hafnia, The Edge "Baltic Exchange shipping updates"); hóa chất (ICIS, Odfjell, Stolt); LPG (BLPG, Fearnleys); hàng rời; orderbook/đóng mới/phá dỡ (BIMCO, Clarksons trích dẫn, Xclusiv, Vantage); El Niño (NOAA CPC), kênh Panama; OPEC+/giá dầu; tin PVT/PVN/BSR/Nghi Sơn (cafef, vietstock, petrotimes). Fearnleys Weekly PDF trên hellenicshippingnews.com (thứ Tư/Năm).
4b. TIN NÓNG (phần quan trọng nhất, nằm đầu trang): 8–14 tin nổi bật nhất có tác động lên giá cước tàu biển, xếp theo mức tác động. Bắt buộc quét đủ 15 nhóm sau trước khi chọn (mỗi nhóm ít nhất 1 truy vấn WebSearch riêng, ưu tiên tin có ngày hôm nay/hôm qua):
   1. Chiến sự/an ninh hàng hải Trung Đông: Mỹ–Iran (tấn công tàu, phong tỏa, đàm phán), Hormuz, UKMTO/JMIC, Houthi/Biển Đỏ/Bab el-Mandeb, Ả Rập Xê Út/Yanbu, Israel.
   2. Nga–Ukraine: tấn công nhà máy lọc dầu, cảng dầu và cảng ngũ cốc (Novorossiysk, Tuapse, Primorsk, Ust-Luga), Biển Đen.
   3. Dầu và dầu sản phẩm: giá Brent/WTI, OPEC+, crack spread, tồn kho, dòng dầu thô theo người mua (Trung Quốc, Ấn Độ).
   4. Hàng rời – cước và hàng: ngũ cốc (Biển Đen, Mỹ, Brazil, Argentina, Úc), than (Indonesia, Úc), quặng sắt, bauxite, phế liệu.
   5. LPG/hóa chất: xuất khẩu LPG Mỹ/Trung Đông, PDH Trung Quốc, chênh giá; cước tàu hóa chất (ICIS, Odfjell, Stolt), thị trường hóa chất châu Á.
   6. Cung tàu: đặt đóng mới, giao tàu, phá dỡ, giá tàu cũ, mua bán tàu.
   7. Thời tiết: El Niño (NOAA), bão ở các tuyến/cảng chính, bão Biển Đông.
   8. Trong nước: PVT, PVN, BSR Dung Quất, Nghi Sơn, chính sách vận tải biển Việt Nam, VOS/VTO/GSP/PVP.
   9. Trừng phạt và đội tàu bóng tối: OFAC/EU/Anh đưa tàu, chủ tàu, cảng, nhà máy lọc dầu vào danh sách; price cap; nới/gỡ trừng phạt Nga, Iran, Venezuela; bắt giữ, khám xét tàu dầu ở biển Baltic, eo biển Đan Mạch, Vịnh Phần Lan; sự cố cáp ngầm Baltic; số tàu bóng tối và tỷ lệ so với đội tàu.
   10. Tắc nghẽn cảng và điểm nghẽn: tàu chờ ở cảng Trung Quốc, Brazil, Ấn Độ, Úc; thời gian chờ Bosphorus/Dardanelles; kênh Panama (lượt tàu, mớn nước), kênh Suez; đình công cảng, sự cố luồng; chỉ số tắc nghẽn nếu có.
   11. Chính sách thương mại: thuế quan Mỹ–Trung và các nước; hạn ngạch/lệnh cấm xuất khẩu (xăng dầu Trung Quốc, Ấn Độ, quặng Indonesia, ngũ cốc); phí cảng với tàu đóng tại Trung Quốc; thỏa thuận mua hàng song phương.
   12. Quy định môi trường và kỹ thuật: IMO (khung net-zero, CII, EEXI), EU ETS, FuelEU Maritime, quy định tuổi tàu của nước/cảng, quy định của hãng thuê về tuổi tàu.
   13. Hoạt động lọc dầu: đóng cửa, bảo dưỡng, sự cố, khánh thành nhà máy (châu Á, Trung Đông, châu Âu, Mỹ, châu Phi/Dangote); biên lọc dầu; thay đổi tuyến chở dầu sản phẩm.
   14. An ninh hàng hải ngoài Trung Đông: Biển Đông, eo Đài Loan, eo Malacca/Singapore (cướp biển, ReCAAP), Tây Phi/Vịnh Guinea, Somalia.
   15. Nhu cầu hàng rời phía cầu: sản lượng thép và tồn quặng Trung Quốc, nhập than Trung Quốc/Ấn Độ, kích thích kinh tế/bất động sản Trung Quốc, vụ mùa và mua ngũ cốc.
   Schema mỗi tin: {"when":"dd/mm","tag":"nhóm ngắn","dir":"up|down|mixed" (hướng tác động lên cước),"segs":["Aframax","MR","Supramax",...],"title":"1 câu, có số liệu","impact":"1–3 câu: cơ chế tác động lên cước và lên đội tàu PVT","src":[{"t":"Nguồn, dd/mm","u":"url"}]}.
   QUY TẮC TIN MỚI (bắt buộc):
   - Mỗi tin nóng phải là sự kiện hoặc số liệu công bố trong 48 giờ qua (72 giờ nếu hôm nay là thứ Hai), hoặc là lịch sự kiện sắp tới.
   - KHÔNG chép lại tin nóng của bản tin trước. Một câu chuyện đã có ở bản trước chỉ được xuất hiện lại khi có diễn biến MỚI; khi đó viết lại tiêu đề và nội dung, đưa diễn biến mới lên đầu. Không có diễn biến mới thì bỏ tin đó khỏi tin nóng (tình hình kéo dài đã được phản ánh ở scoreManual và mục "news").
   - Số tin nóng trùng nguyên tiêu đề với bản tin trước phải bằng 0. Kiểm tra bằng cách so từng tiêu đề trước khi ghi file.
   - Ít tin mới thì đăng ít tin (tối thiểu 4), không độn bằng tin cũ. Phần "news" (Phân tích chi tiết) dành cho chủ đề trung hạn, không lặp lại tin nóng.
4c. CÁC MỤC CHUYÊN SÂU (đều nằm trong object bản tin; mục nào hôm nay không có số mới thì BỎ QUA key đó, trang tự giữ số của bản tin gần nhất và ghi "chưa có số mới". KHÔNG chép nguyên mục của bản tin trước sang bản hôm nay; chỉ ghi một mục khi có ít nhất một dòng mới hoặc đã sửa):
   - scoreManual[]: chỉ báo định tính của bảng điểm thesis {key,name,value(chuỗi),asof:"YYYY-MM-DD",status:green|yellow|red,rule,why,src[]}. Giữ đủ các key: warrisk (phí bảo hiểm chiến tranh Hormuz), talks (Mỹ–Iran), gulfflows (xuất khẩu dầu vùng Vịnh %), orderbook (orderbook tàu dầu/MR), drysupply (cung–cầu hàng rời), peers (ngày tàu ký trước của doanh nghiệp cùng ngành), dark (đội tàu bóng tối). Chỉ báo số liệu (Hormuz, BDTI/BCTI/BSI/BHSI phân vị, định hạn so TB 5N, FFA, giá tàu, phá dỡ) do build.py tự tính — không viết tay.
   - calendar[]: {date,end?,tentative?,event,why}. Luôn có các mốc 7–10 ngày tới (OPEC+, EIA thứ Tư, NOAA ENSO thứ Năm thứ 2 của tháng, Baltic thứ Sáu, Fearnleys thứ Tư, kết quả kinh doanh doanh nghiệp cùng ngành, BCTC PVT, IMO 04/12/2026...). Xóa mốc đã qua.
   - routes[]: cước theo tuyến từ Baltic weekly roundup (thứ Sáu). BẮT BUỘC: nếu routes của bản tin gần nhất cũ hơn báo cáo tuần Baltic mới nhất thì hôm nay phải tìm và đọc báo cáo tuần đó (tàu dầu, hàng rời, khí) qua balticexchange.com, The Edge "Baltic Exchange shipping updates", Hellenic Shipping News hoặc Dry Bulk Magazine, rồi viết lại routes. {route,desc,seg,ws,tce(số),date,note,src}. Ưu tiên tuyến châu Á nếu tìm được (TC7, TD8, TD14, Supramax/Handysize châu Á).
   - period[]: hợp đồng định hạn thực tế công bố {vessel,type,rate,period,when,note,src}.
   - snp[]: giao dịch mua bán tàu cũ mới nhất ở cỡ PVT khai thác (MR, LR1, Aframax, tàu hóa chất nhỏ, LPG nhỏ, Supramax/Ultramax/Handysize) {vessel,type,dwt(số),built,yard,price,buyer,note,src}. Nguồn: Xclusiv, Intermodal, Allied, Fearnleys, Splash "Weekly Broker". So sánh với độ tuổi ~15–17 năm của PVT.
   - supply[]: orderbook/giao tàu/phá dỡ theo phân khúc {topic,value,note,src}.
   - flows[]: dòng hàng, biên lọc dầu, đội tàu bóng tối, hiệu suất (Mũi Hảo Vọng, Panama, bảo hiểm), ngũ cốc/than {topic,value,note,src}.
   - lpg[]: VLGC theo tuyến (BLPG1/3), chênh giá LPG Mỹ–châu Á, thông tin tàu LPG nhỏ {topic,value,note,src}.
   - regulation[], vietnam[]: thẻ {tag,title,text,impact,src}. Việt Nam: nguồn dầu thô Nghi Sơn/BSR, lịch bảo dưỡng, LPG nhập khẩu, bão Biển Đông, tin PVT/VOS/VTO/GSP/PVP.
   - peers[]: {company,seg,data,read,src} — tỷ lệ ngày đã ký và giá của Scorpio, Hafnia, Torm, Frontline, Teekay, Odfjell, Stolt, BW LPG, Star Bulk...
   Tần suất gợi ý: tin nóng + scoreManual + calendar hằng ngày; routes/period/snp/lpg thứ Hai–thứ Sáu khi có báo cáo tuần mới; supply/flows/regulation/peers khi có tin mới.
4d. MỨC TỐI THIỂU BẮT BUỘC trước khi viết (áp dụng mọi ngày, kể cả cuối tuần, ngày nghỉ và khi viết lại bản tin đã có). Đây là SÀN, không phải đích: đạt sàn rồi vẫn tiếp tục nếu còn nhóm chưa có trang nào mở được.
   - Ít nhất 1 truy vấn WebSearch riêng cho MỖI nhóm trong 15 nhóm của mục 4b; tổng cộng ít nhất 24 truy vấn. Truy vấn nên có tháng/năm hoặc từ khóa ngày để ra tin mới.
   - Đã MỞ THÀNH CÔNG (WebFetch) ít nhất 15 trang nguồn, trong đó ít nhất 10 trang có ngày đăng trong 72 giờ qua. Trang lỗi không được tính. Không viết từ đoạn trích kết quả tìm kiếm.
   - Mỗi nhóm trong 15 nhóm phải có ít nhất 1 trang mở thành công, hoặc ghi rõ trong log là đã thử những gì và vì sao không có.
   - Nguồn bắt buộc thử mỗi ngày: trang chủ/chuyên mục mới nhất của hellenicshippingnews.com; gcaptain.com; báo cáo tuần Baltic (xem routes ở 4c); thứ Tư/Năm thêm Fearnleys Weekly.
   - Đã làm bước 3 (đối chiếu BDI).
   - Chỉ được dừng dưới mức này khi công cụ web lỗi hàng loạt; khi đó ghi nguyên văn lỗi vào log, vào "gaps" và vào thông báo cuối.
4e. KHI MỘT TRANG LỖI (403, 402, 404, timeout, tường phí, EGRESS_BLOCKED):
   - Ghi ngay vào log: URL, mã lỗi nguyên văn.
   - Tìm bản khác của CÙNG tin: WebSearch bằng tiêu đề bài hoặc cụm số liệu đặc trưng, rồi mở bản đăng lại/bản tin tương đương ở nguồn khác (Hellenic Shipping News, gCaptain, The Maritime Executive, MarineLink, Safety4Sea, Offshore Energy, Reuters/AP/AFP qua các báo đăng lại, The Edge, báo trong nước). Thử tối đa 2 nguồn thay thế cho mỗi tin quan trọng, ghi từng lần thử vào log.
   - Tên miền đã lỗi ở cả 3 log gần nhất: không mở trực tiếp nữa, đi thẳng tới nguồn thay thế (vẫn ghi vào log là "bỏ qua, lỗi lặp lại").
   - Tin chỉ có trong đoạn trích tìm kiếm, không mở được ở nguồn nào: chỉ được đưa vào bản tin nếu ghi rõ "chưa kiểm chứng bằng trang gốc", và không dùng làm tin nóng số 1–3.
5. Thêm 1 object mới vào ĐẦU mảng window.REPORTS trong reports.js (cùng schema: date, dataAsOf, headlines[], headline, summary[], pvt[{seg,signal:up|down|flat|na,text}], news[{tag,title,text,impact,src[{t,u}]}], watch[], gaps[]). Giữ tối đa 90 bản tin. Chỉ đưa số liệu có nguồn; tin chưa kiểm chứng ghi rõ. Viết tiếng Việt, ngắn gọn, trực diện, không văn vẻ; mục "Với PVT" ngắn gọn, nói tác động lên phân khúc tàu nào của PVT.
6. Đẩy lên GitHub (trang tự cập nhật sau 1–2 phút):
   - Kiểm tra cú pháp trước: `node --check reports.js && node --check data.js` (hoặc tương đương). Lỗi cú pháp thì sửa trước, không push file hỏng.
   - `git add reports.js data.js logs/` (kèm index.html, build.py, RUNBOOK.md chỉ khi lần chạy này có sửa chúng theo yêu cầu người dùng; lần chạy tự động hằng ngày KHÔNG sửa ba file đó).
   - `git commit -m "Bản tin YYYY-MM-DD"` rồi `git push origin HEAD:main`.
   - Bản tin phải nằm trên `main`. Không mở pull request. Nếu hệ thống buộc phải đẩy cả nhánh làm việc `claude/...` của lần chạy này thì đẩy và để nguyên; KHÔNG thử xóa nhánh `claude/...` nào trên remote (hệ thống không cho phép; người dùng tự dọn).
   - Xác nhận: `git fetch origin main && git log origin/main -1 --oneline` phải là commit vừa tạo.
7. Kết thúc bằng thông báo ngắn: điểm chính hôm nay (3–5 dòng); số truy vấn, số trang mở thành công/lỗi, số tin nóng (mới/giữ lại); kết quả push (thành công hay lỗi gì); link nhật ký https://github.com/kienluaa/PVT/blob/main/logs/YYYY-MM-DD.md; và link https://kienluaa.github.io/PVT/

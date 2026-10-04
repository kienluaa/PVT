# Chẩn đoán truy cập web (2026-10-04)

| URL | WebFetch | curl: trạng thái | server | cf-mitigated | cf-ray | x-deny-reason | via |
|---|---|---|---|---|---|---|---|
| https://splash247.com/ | Thành công | HTTP/2 200 | cloudflare | - | a45085c7c9f96ac6-IAD | - | - |
| https://splash247.com/feed/ | Thành công | HTTP/2 200 | cloudflare | - | a45085cbae21d6c7-IAD | - | - |
| https://www.seatrade-maritime.com/ | Lỗi: "The server returned HTTP 403 Forbidden." | HTTP/2 403 | cloudflare | - | a45085ce5dcdffd7-IAD | - | - |
| https://www.agbi.com/ | Lỗi: "The server returned HTTP 403 Forbidden." | HTTP/2 403 | CloudFront | - | - | - | 1.1 2998d920822e5ea25e271f9a9d21f94e.cloudfront.net (CloudFront) |
| https://www.hellenicshippingnews.com/ | Thành công | HTTP/2 200 | cloudflare | - | a45085d0ef277c74-IAD | - | - |
| https://gcaptain.com/ | Thành công | HTTP/2 200 | cloudflare | - | a45085d70e36c8a1-IAD | - | - |
| https://www.balticexchange.com/ | Thành công (tải được, nhưng headline trả về là "Challenge Validation" — có thể là trang thử thách) | HTTP/2 301 | - | - | - | - | - |
| https://theedgemalaysia.com/ | Thành công (không thấy tiêu đề bài viết trong nội dung) | HTTP/2 200 | cloudflare | - | a45085db3cfbe61f-IAD | - | - |

Ghi chú: mỗi lệnh curl cũng có dòng "HTTP/1.1 200 Connection Established" từ proxy, không tính vào bảng.

# Mừng 20-10 · Phòng MKT

Trang chúc mừng Ngày Phụ nữ Việt Nam 20-10 cho 4 thành viên nữ phòng Marketing: Ngọc Khánh, Hồng Viên, Minh Châu, Thu Hiền.

**Luồng trang:** trang chủ (phòng hoa, ảnh nhóm) → nhập số điện thoại để nhận diện (số được lưu dạng SHA-256, không lưu số thật) → minigame 3D nhặt 20 bông hoa và chạy qua cổng hoa 20-10 → thiệp chúc mừng dạng vòng xoay với lời chúc riêng.

## Cấu trúc
| Đường dẫn | Nội dung |
|---|---|
| `index.html` | Toàn bộ trang (HTML, CSS, JS). Bản này dùng cho Claude Artifact nên không có thẻ `<html>/<head>` |
| `assets/` | Ảnh, nhạc, mô hình 3D (`.gltf.json`, glTF có dữ liệu nhúng) |
| `tools/build.py` | Đóng gói thành trang độc lập trong `dist/` để deploy |

## Deploy
```bash
python3 tools/build.py   # tạo dist/index.html + dist/assets/
```
Upload toàn bộ thư mục `dist/` lên hosting tĩnh (Vibe Host, GitHub Pages…). Trang cần chạy qua `http(s)://`, không mở trực tiếp bằng `file://` được.

Thư viện: three.js 0.160.0 (tải từ cdn.jsdelivr.net), font Google Fonts (Bungee, Be Vietnam Pro, Pacifico).

## Mã test
Gõ `1`, `2`, `3`, `4` vào ô số điện thoại để vào nhanh vai Khánh, Viên, Châu, Hiền. Xoá các trường `testHash` trong `MEMBERS` trước khi gửi link chính thức.

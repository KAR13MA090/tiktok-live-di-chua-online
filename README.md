# tiktok-live-di-chua-online

<div align="center">

![GitHub repo size](https://img.shields.io/badge/Status-Hoàn%20thiện%20100%25-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Nền%20tảng-TikTok%20Live%20%7C%20OBS%20Studio-fe2c55?style=for-the-badge&logo=tiktok)
![Resolution](https://img.shields.io/badge/Khung%20hình-9:16%20(1080%C3%971920)-ffaa00?style=for-the-badge)
![Runtime](https://img.shields.io/badge/Backend-Bun.js%20%7C%20Node.js-fbf0df?style=for-the-badge&logo=bun)
![License](https://img.shields.io/badge/Giấy%20phép-MIT-blue?style=for-the-badge)

<p align="center">
  <b>Hệ Thống Phát Trực Tiếp Đi Chùa Online — Tương Tác TikTok Live & JSON-RPC 2.0 Chuẩn Khung Hình Dọc 9:16</b><br/>
  <i>Tích hợp Chánh Điện Đức Phật A Di Đà, Đạo Tràng 40 Phật tử, Bảng Vàng Công Đức, Gieo Quẻ Linh Xăm & Giọng đọc AI Tiếng Việt (Mai Chi).</i>
</p>
---

## Tính Năng Nổi Bật

| Tính năng | Mô tả chi tiết |
| :--- | :--- |
| **Chánh Điện A Di Đà 2.5D** | Không gian Chánh Điện tôn nghiêm, tượng Phật A Di Đà trang nghiêm, Lư Hương Đỉnh Đồng, hoành phi câu đối sơn son thếp vàng. |
| **8-Frame Đảnh Lễ Tam Bái** | Nhân vật áo lam bước dọc thảm đỏ hoa sen, quỳ gối thực hiện 3 lạy Ngũ thể đầu địa (`Ngũ thể đầu địa`) chân thực, không nhấp nháy hình ảnh. |
| **Giọng Đọc AI (Mai Chi)** | Tổng hợp giọng đọc tiếng Việt 48kHz mượt mà, truyền cảm: tự động đọc tên thí chủ, lời khấn nguyện, cảm tạ dâng lễ và lời giải quẻ xăm. |
| **Linh Xăm 18 Quẻ Đồng Bộ** | Lắc ống xăm tre, gieo quẻ và tự động mở tờ Giải Quẻ (Thượng Thượng Cát, Đại Cát...) khớp chính xác từng giây với giọng đọc AI. |
| **Bảng Vàng TẤM LÒNG THÀNH** | Tự động ghi nhận và vinh danh Top người xem có điểm Công Đức cao nhất trên 6 Đệm Quỳ Gấm Đỏ VIP và bảng xếp hạng HUD góc phải. |
| **Đạo Tràng 40 Vị Trí** | Khán giả vào xem live được tự động sắp xếp chỗ ngồi quỳ lễ hai bên thảm đỏ với bảng tên và avatar cá nhân theo phối cảnh xa gần. |
| **Đại Hồng Chung & Mõ Gỗ** | Pháp khí Web Audio API mô phỏng âm thanh gõ mõ tâm linh và tiếng chuông đồng ngân vang lan tỏa sóng âm vàng đánh thức Đạo Tràng. |
| **Đèn Hoa Đăng Bay Lên** | Mỗi bình luận cầu nguyện, chúc phúc sẽ hóa thành Đèn Hoa Đăng mang tên và lời khấn trôi nhẹ lên nền trời thiền tịnh. |
| **Đại Lễ Kim Long Chầu Phật** | Kích hoạt hiệu ứng Đại Lễ khi nhận quà giá trị cao: mưa hoa sen vàng, hào quang Phật rực sáng và chuông đồng ngân vang liên tục. |
| **Siêu Tiết Kiệm CPU / GPU** | Động cơ hạt Canvas 30 FPS với Offscreen Sprite Pre-rendering, tiêu thụ chỉ **~0.1% CPU** khi chờ, an toàn treo máy live 24/7. |

---

## 🎮 Bảng Quy Tắc Tương Tác TikTok Live

Hệ thống tích hợp bộ phân tích ngôn ngữ tự nhiên tiếng Việt (có dấu và không dấu), tự động nhận diện ý định của người xem để kích hoạt nghi thức:

| Sự kiện TikTok Live | Điều kiện nhận diện / Từ khóa | Nghi thức cử hành trên Chánh Điện | Điểm Công Đức |
| :--- | :--- | :--- | :---: |
| **Thả tim (Like)** | Khán giả chạm màn hình thả tim | Gõ mõ gỗ tụng kinh + Làn sóng Phật tử Đạo Tràng đồng loạt vái lạy | `+1` / tim |
| **Follow / Share** | Bấm Theo dõi hoặc Chia sẻ live | Thỉnh Đại Hồng Chung ngân vang + Lan tỏa sóng âm vàng cứu độ | `+10` |
| **Bình luận Thắp Hương** | `thắp hương`, `dâng hương`, `thap huong`, `bái phật`, `lạy phật`, `bai phat` | Phật tử áo lam bước dọc thảm đỏ lên Lư Hương, quỳ đảnh lễ 3 lạy + Giọng đọc tên khấn | `+15` |
| **Bình luận Cầu Nguyện** | `cầu...`, `nguyện...`, `nam mô`, `a di đà phật`, `bình an`, `chúc...`, `cau...`, `nguyen...` | Bước lên đảnh lễ + Thả Đèn Hoa Đăng mang lời khấn bay lên trời + Đọc trích đoạn lời cầu | `+10` |
| **Bình luận Xin Xăm** | `xin xăm`, `gieo quẻ`, `rút quẻ`, `quẻ`, `xin xam`, `gieo que`, `rut que`, `que` | Ống xăm tre lắc hạt + Mở tờ Giải Quẻ linh ứng khớp chuẩn xác từng chữ với giọng đọc | `+10` |
| **Tặng quà Nhỏ (1–4 xu)** | Hoa hồng (Rose), Heart Me, Bánh tiêu... | Dâng Đài Hoa Sen Vàng + Thắp 3 nén hương thơm + Đọc lời cảm tạ thí chủ | `+20` / xu |
| **Tặng quà Vừa (5–99 xu)** | Đèn lưu ly, Mâm ngũ quả, Chuông gió... | Dâng Mâm Ngũ Quả / Đèn Lưu Ly + Thỉnh chuông đồng ngân vang + Đọc lời chúc phúc | `+30` / xu |
| **Tặng quà Lớn (≥ 100 xu)** | Kim Long, Vương miện, Tràng hoa... | **🐉 ĐẠI LỄ KIM LONG CHẦU PHẬT**: Mưa hoa sen vàng, Hào quang vạn trượng, Chuông Bát Nhã ngân vang | `+50` / xu |

---

## Bản Đồ Tài Nguyên Đồ Họa (Assets 01 - 12)

Toàn bộ đồ họa trong thư mục `public/assets/` đã được chuẩn hóa theo mã số thứ tự từ `01` đến `12` để dễ dàng quản lý và thay thế skin giao diện theo nhu cầu:

| Tên File Mã Hóa | Tên Gốc Ban Đầu | Vai Trò & Vị Trí Sử Dụng Trong Mã Nguồn |
| :---: | :--- | :--- |
| **`01.jpg`** | `amitabha_stage.jpg` | Ảnh nền Chánh Điện Đức Phật A Di Đà (phiên bản JPEG nén nhẹ). |
| **`02.png`** | `amitabha_stage.png` | **Ảnh nền Chánh Điện Đức Phật A Di Đà sắc nét** (hiển thị chính tại `public/index.html` dòng 21). |
| **`03.png`** | `buddha.png` | Tôn tượng Đức Phật A Di Đà tọa đài sen vàng (layer độc lập tách nền). |
| **`04.png`** | `devotee_bow_mid.png` | Khung hình Sprite 6: Phật tử cúi gập lưng góc 45 độ (`bowMid`). |
| **`05.png`** | `devotee_bow.png` | Khung hình Sprite 5: Phật tử chắp hai tay đưa ngang chân mày (`forehead`). |
| **`06.png`** | `devotee_kneel_down.png` | Khung hình Sprite 3: Phật tử bắt đầu hạ gối xuống đệm hoa sen (`kneelDown`). |
| **`07.png`** | `devotee_prostrate_deep.png`| Khung hình Sprite 8: Phật tử lạy sát đất Ngũ thể đầu địa (`prostrateDeep`). |
| **`08.png`** | `devotee_prostrate.png` | Khung hình Sprite 7: Phật tử vươn tay đè đệm bái Phật (`prostrate`). |
| **`09.png`** | `devotee_walk_2.png` | Khung hình Sprite 2: Phật tử sải bước chân phải dọc thảm đỏ (`walk2`). |
| **`10.png`** | `devotee_walk.png` | Khung hình Sprite 1: Phật tử sải bước chân trái dọc thảm đỏ (`walk1`). |
| **`11.png`** | `devotee.png` | **Khung hình Sprite trung tâm**: Phật tử quỳ chắp tay trang nghiêm trên đệm (`kneel`), dùng cho cả 40 Phật tử Đạo Tràng và 6 Đệm VIP. |
| **`12.png`** | `temple_stage_bg.png` | Ảnh nền Chánh Điện cổ điển thay thế dự phòng. |

---

## Kiến Trúc Kỹ Thuật & Tối Ưu Hiệu Năng

- **Runtime Siêu Nhẹ**: Chạy trên **Bun.js** (hoặc Node.js >= 18), bộ nhớ chiếm dụng `< 70MB RAM`, CPU khi chờ duy trì mức **~0.1%**.
- **Canvas Particle Engine Khóa 30 FPS (`public/js/particles.js`)**:
  - Không vẽ gradient hoặc đổ bóng phức tạp (`shadowBlur`) trong từng frame.
  - Toàn bộ cánh hoa sen, khói nhang uốn lượn và hạt bụi vàng được **Pre-render 1 lần duy nhất** ra Offscreen Canvas và vẽ lại bằng `drawImage`.
  - Tự động đóng băng luồng render khi cửa sổ bị ẩn (`document.hidden`).
- **Zero-Flicker GPU Compositor Stack (`public/js/live.js`)**:
  - 8 khung hình chuyển động đảnh lễ được nạp sẵn vào GPU texture cache, chuyển đổi tức thì `0ms`, loại bỏ triệt để hiện tượng nhấp nháy đen khung hình khi đổi động tác lạy.
- **Tiến trình Python Thường Trú (`tts_worker.py`)**:
  - Khởi chạy nền với các biến môi trường thụ động (`OMP_WAIT_POLICY=PASSIVE`, `intra_op_num_threads=3`).
  - Tự động khử DC offset, chuẩn hóa đỉnh sóng âm `peak <= 0.90` và áp dụng bộ đệm Cosine Fade chống xước rè loa khi phát trực tiếp.
  - Lưu trữ bộ đệm file âm thanh `.wav` theo mã băm SHA-1 tại `data/tts-cache/`, cùng một câu khấn sẽ không bao giờ tốn tài nguyên đọc lại.
- **Bộ Lọc Chống Ký Tự Lạ & Spam (`server.js`)**:
  - Chặn đứng các ký tự Zalgo, chữ Cuneiform Babylon (``), chữ Ả Rập gây lag font hệ thống, icon spam và từ ngữ không phù hợp.
  - Tự động chuẩn hóa chữ viết Unicode `NFKC` về tiếng Việt chuẩn trước khi đọc.

---

## Hướng Dẫn Cài Đặt & Chạy Nhanh

### 1. Yêu cầu môi trường
- [Bun.js](https://bun.sh/) (Khuyến nghị, phiên bản `>= 1.1`) hoặc [Node.js](https://nodejs.org/) (`>= 18`)
- Python `3.10+`

### 2. Cài đặt các gói phụ thuộc
```bash
# 1. Cài đặt thư viện Node / Bun
bun install
# (Hoặc nếu dùng npm: npm install)

# 2. Tạo môi trường ảo Python và cài đặt gói đọc giọng nói
python -m venv .venv

# Trên Windows PowerShell:
.venv\Scripts\activate
pip install zerotts pillow

# Trên macOS / Linux:
source .venv/bin/activate
pip install zerotts pillow
```

### 3. Khởi chạy hệ thống
```bash
# Chạy với Bun (Khuyến nghị tốc độ cao nhất):
bun start

# Hoặc chế độ tự động reload khi chỉnh sửa mã nguồn:
bun run dev

# Hoặc chạy với Node.js:
npm start
```

Sau khi khởi chạy thành công, mở trình duyệt truy cập:
- **Màn hình Live Chánh Điện**: [http://localhost:3000](http://localhost:3000)
- **Màn hình OBS Browser Source (Chuẩn sạch 9:16)**: [http://localhost:3000/?obs=1](http://localhost:3000/?obs=1)
- **Bảng Quản Trị & Điều Khiển RPC**: [http://localhost:3000/admin](http://localhost:3000/admin)

---

## Hướng Dẫn Thiết Lập OBS Studio / TikTok Live Studio

1. **Khởi chạy phần mềm OBS Studio** hoặc TikTok Live Studio.
2. Thêm nguồn mới: Chọn dấu `+` tại bảng **Sources** ➔ Chọn **Browser** (Trình duyệt).
3. Đặt tên nguồn: `Chua_Online_9x16`.
4. Cấu hình các thông số chuẩn sau:
   - **URL**: `http://localhost:3000/?obs=1` *(tham số `?obs=1` sẽ tự động ẩn bảng điều khiển bên phải, chỉ để lại Chánh Điện)*
   - **Width (Chiều rộng)**: `1080`
   - **Height (Chiều cao)**: `1920`
   - **Custom Frame Rate**: Đánh dấu chọn và nhập `30`
   - **Control audio via OBS**: Đánh dấu chọn (để quản lý âm lượng thanh chuông, mõ, nhạc thiền trực tiếp qua mixer OBS).
5. Nhấn **OK**. Chánh Điện Chùa Linh Ứng sẽ khớp vừa vặn 100% khung hình livestream dọc của bạn.

---

## 🔌 Giao Thức JSON-RPC 2.0 (`POST /rpc` & WebSocket)

Hệ thống hỗ trợ toàn diện chuẩn **JSON-RPC 2.0**. Bạn có thể tích hợp với **TikFinity**, **Streamer.bot**, phím bấm macro Elgato Stream Deck hoặc gửi lệnh bằng `curl`:

### 1. Thắp hương dâng lễ bái Phật
```bash
curl -X POST http://localhost:3000/rpc \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "temple.burnIncense",
    "params": {
      "user": "Thí Chủ Minh Tâm",
      "count": 3,
      "wish": "Cầu gia đình bình an, công việc thuận lợi vạn sự như ý"
    }
  }'
```

### 2. Gieo quẻ Linh Xăm đầu năm
```bash
curl -X POST http://localhost:3000/rpc \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "temple.drawFortune",
    "params": {
      "user": "Thí Chủ Diệu Thảo",
      "topic": "Cầu công danh sự nghiệp và sức khỏe"
    }
  }'
```

### 3. Kết nối phòng phát trực tiếp TikTok Live
```bash
curl -X POST http://localhost:3000/rpc \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "live.connect",
    "params": {
      "username": "@GOCNHINMUDEN"
    }
  }'
```

### Bảng tra cứu toàn bộ JSON-RPC Methods:

| Phương thức (Method) | Tham số (Params) | Mô tả công dụng |
| :--- | :--- | :--- |
| `temple.getState` | Không | Lấy dữ liệu toàn diện của phòng live (số hương, công đức, bảng vàng, cấu hình). |
| `temple.burnIncense` | `user`, `avatar`, `count`, `wish`, `readTts` | Thắp hương, bước lên đảnh lễ Tam Bái và đọc lời khấn nguyện. |
| `temple.sendPrayer` | `user`, `avatar`, `wish`, `readTts` | Thả Đèn Hoa Đăng mang sớ cầu an bay lên trời kèm đọc lời khấn. |
| `temple.drawFortune` | `user`, `avatar`, `topic` | Rung ống xăm tre, gieo quẻ và giải quẻ xăm linh ứng. |
| `temple.strikeWoodenFish` | `user`, `count` | Gõ mõ tích điểm công đức và kích hoạt Phật tử Đạo Tràng vái lạy. |
| `temple.ringBell` | `user`, `count`, `wish`, `readTts` | Thỉnh Đại Hồng Chung ngân vang lan tỏa sóng âm vàng. |
| `temple.offerGift` | `user`, `giftType`, `coins`, `giftName`, `wish` | Dâng lễ vật cúng dường (`lotus`, `fruit`, `lamp`, `dragon`). |
| `temple.grandCeremony` | `user`, `coins`, `giftName` | Kích hoạt Đại Lễ Kim Long Chầu Phật (Hào quang vạn trượng). |
| `temple.updateSettings` | `musicVolume`, `ttsVolume`, `autoSim` | Cập nhật cấu hình âm lượng, nhạc nền và chế độ giả lập. |
| `temple.resetMerit` | Không | Xóa trắng và đặt lại Bảng Vàng Công Đức của phiên phát sóng mới. |
| `live.connect` | `username` | Kết nối lắng nghe sự kiện từ phòng TikTok Live (`@GOCNHINMUDEN`). |
| `live.disconnect` | Không | Ngắt kết nối phòng TikTok Live hiện tại. |
| `live.setAutoSim` | `enabled` (`true`/`false`) | Bật / tắt chế độ tự động giả lập người xem dâng hương liên tục. |

---
## ❓ Câu Hỏi Thường Gặp (FAQ)

<details>
<summary><b>1. Làm thế nào để thay đổi tài khoản TikTok Live kết nối?</b></summary>
<br/>
Bạn có thể nhập tên tài khoản trực tiếp trên bảng điều khiển nhanh ở màn hình chính, hoặc trong trang <code>http://localhost:3000/admin</code>, hoặc truyền biến môi trường khi khởi động:
<pre><code>TIKTOK_USER=GOCNHINMUDEN bun start</code></pre>
</details>

<details>
<summary><b>2. Tại sao mở trình duyệt lần đầu không nghe thấy tiếng nhạc và giọng đọc?</b></summary>
<br/>
Chính sách bảo mật của các trình duyệt hiện đại (Chrome, Edge) chặn tự động phát âm thanh khi chưa có tương tác. Bạn chỉ cần <b>nhấp chuột 1 lần bất kỳ lên màn hình</b> hoặc bấm nút <b>"Bật Âm Thanh Chùa"</b> ở góc phải là âm thanh sẽ được kích hoạt vĩnh viễn. Khi đưa vào OBS qua Browser Source, OBS sẽ tự động phát âm thanh mà không bị chặn.
</details>

<details>
<summary><b>3. Giọng đọc AI có cần kết nối Internet không?</b></summary>
<br/>
Ở lần đầu tiên khởi động, worker Python sẽ tải model giọng đọc Mai Chi chuẩn về máy. Từ các lần sau, hệ thống sẽ chạy hoàn toàn Offline nội bộ trên máy của bạn với tốc độ phản hồi cực nhanh (~0.1s - 0.3s) mà không tốn chi phí API của bên thứ ba.
</details>

---

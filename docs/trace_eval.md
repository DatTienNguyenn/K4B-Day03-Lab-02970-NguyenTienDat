# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Điền Họ và Tên]  
> **Mã Sinh Viên / Mã Học viên:** [Điền MSSV]  
> **Chủ đề Lựa chọn:** [Điền tên chủ đề đã chọn từ docs/DANH_SACH_DE_TAI.md hoặc Đề tài Mở]

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá           | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                                                                                                                                                                      |
| :-------------------------- | :------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Multi-step Reasoning** |     3 / 5      | Bài toán cần tách nhỏ việc dặt phòng/thiết bị ra thành kiểm tra thông tin đặt, kiểm tra phòng/thiết bị được đặt có available không rồi mới đặt phòng/thiết bị                                                            |
| **2. Tool Interaction**     |     3 / 5      | Hệ thống cần kết nối với database quản lí của phòng họp/thiết bị để biết phòng/thiết bị nào phù hợp và có available không cũng như cần kết nối đến tool đặt phòng/thiết bị                                               |
| **3. Dynamic Decision**     |     4 / 5      | Phụ thuộc rất nhiều vào kết quả bước trước, nếu thông tin không hợp lệ thì không kiểm tra được trạng thái phòng/thiết bị và nếu phòng/thiết bị không available thì không thể đặt                                         |
| **4. Long Horizon Goal**    |     3 / 5      | Hệ thống cần nắm được thông tin yêu cầu của người dùng vì những yêu cầu sẽ được người dùng thêm vào để tìm được phòng phù hợp nên cần nhớ những yêu cầu trước mà người dùng đã input để đưa ra câu trả lời chính xác hơn |
| **TỔNG ĐIỂM AGENTIC FIT**   |   13/ 20\*\*   | _Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System._                                                                                                                                                 |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
{
  {
    "step": 1,
    "query": "Kiểm tra xem phòng họp P302 có còn trống vào khung giờ từ 14:00 đến 16:00 chiều nay không?",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "check_room_availability",
    "arguments": {
      "room_id": "P302",
      "start_time": "14:00",
      "end_time": "16:00",
      "date": "hôm nay"
    },
    "observation": {
      "status": "SUCCESS",
      "room_id": "P302",
      "available": true,
      "start_time": "14:00",
      "end_time": "16:00",
      "date": "hôm nay",
      "message": "Phòng P302 còn trống từ 14:00 đến 16:00 vào ngày hôm nay."
    },
    "latency_ms": 1511.07
  },
  {
    "step": 2,
    "query": "Kiểm tra xem phòng họp P302 có còn trống vào khung giờ từ 14:00 đến 16:00 chiều nay không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Phòng P302 còn trống từ 14:00 đến 16:00 vào ngày hôm nay.",
    "latency_ms": 10.0
  }
}
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!

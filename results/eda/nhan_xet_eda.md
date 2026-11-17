### Nhận xét sau EDA (số liệu tự động)

- **Quy mô:** 1,223 phản hồi, 11 cột. Đầu vào mô hình là `feedback_text`, nhãn dự đoán là `sentiment_label`.
- **Phân bố nhãn:** positive: 489 (39.98%); neutral: 368 (30.09%); negative: 366 (29.93%). Tỷ lệ giữa lớp đông nhất và ít nhất là 1.34 lần; lớp không cân bằng hoàn toàn, do đó nên dùng **Macro F1** cùng Accuracy khi so sánh.
- **Chất lượng dữ liệu:** 0 phản hồi thiếu/rỗng, 0 nhãn thiếu; 0 dòng trùng hoàn toàn; 0 dòng trùng nội dung; 0 nhóm văn bản mang nhiều nhãn khác nhau (theo kiểm tra trong notebook).
- **Độ dài:** trung bình 11.45 từ/phản hồi, ngắn nhất 4, dài nhất 22 từ. Văn bản tương đối ngắn có thể hạn chế bối cảnh, nhưng cần kiểm chứng thay vì kết luận đây là nguyên nhân duy nhất.
- **Rà soát ngữ nghĩa:** Các câu được lấy mẫu ở mục 9.5 có nhiều tổ hợp từ thiếu ngữ cảnh rõ ràng. Cần xem xét tính tự nhiên của phản hồi và kiểm tra nhãn bằng tay; chưa đủ bằng chứng để khẳng định nhãn sai hoặc dữ liệu là giả lập.
- **Quyết định tiếp theo:** Dùng đúng cột văn bản gốc và nhãn đã chỉ định, xử lý phản hồi trống/trùng trước khi chia train/test; thử BoW và TF-IDF, không dùng các cột có nguy cơ tiết lộ nhãn làm đặc trưng đầu vào.

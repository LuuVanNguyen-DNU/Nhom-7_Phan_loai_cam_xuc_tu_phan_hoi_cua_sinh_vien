# Diễn giải kết quả thực nghiệm – Thành viên 3

- Đã thử **8** tổ hợp biểu diễn–thuật toán và **24** lượt cấu hình tham số bằng Stratified 3-fold CV **chỉ trên train** (tiêu chí F1-macro).
- Điểm CV tốt nhất thuộc **TFIDF_Unigram__KNN**: **0.3647**; hạng hai **BoW_Unigram__NaiveBayes**: **0.3637**. Mức chênh CV chỉ **0.0010**; một chênh lệch rất nhỏ chưa đủ để khẳng định một thuật toán tốt hơn ổn định.
- Sau khi chọn theo CV, mô hình được đánh giá một lần trên tập test cố định: **Accuracy=0.3388**, **Macro F1=0.3369**; baseline BoW+NB **Macro F1=0.3748**. Mức chênh (mô hình chọn – baseline) là **-0.0379**.
- Dummy majority có **Accuracy=0.4000**, **Macro F1=0.1905**. Chỉ số Accuracy một mình có thể đánh lừa khi dự đoán dồn vào lớp đông nhất.
- Việc mô hình CV tốt nhất có điểm test thấp hơn baseline **không chứng minh thuật toán bị lỗi**. Cần xem xét biến thiên do cách chia dữ liệu, chất lượng nhãn/văn bản và đặc trưng; **không chọn lại theo test** sau khi xem kết quả.
- Lịch sử 24 lượt thử nằm tại `results/training/cv_hyperparameter_details.csv`; bảng độ nhạy alpha/k nằm tại `results/training/cv_parameter_effect.csv`. Đầu ra chuyển cho Thành viên 4 là `test_metrics.csv`, `test_predictions.csv`, `best_model.json`.

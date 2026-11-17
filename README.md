# FIT4013 – Phân loại cảm xúc từ phản hồi của sinh viên

## 1. Giới thiệu đề tài

Đây là bài tập lớn học phần **Nhập môn Học máy (FIT4013)**, thực hiện bởi **Nhóm 7 – Trường Đại học Đại Nam**, năm học 2026–2027.

Đề tài xây dựng và đánh giá quy trình học máy có giám sát nhằm phân loại phản hồi dạng văn bản của sinh viên thành ba nhóm cảm xúc:

- **Positive:** Tích cực.
- **Neutral:** Trung tính.
- **Negative:** Tiêu cực.

Mục tiêu chính là so sánh các phương pháp biểu diễn văn bản và thuật toán học máy, đánh giá kết quả và phân tích những trường hợp dự đoán sai.

## 2. Bộ dữ liệu

**Tên bộ dữ liệu:** Contextual Sentiment Feedback Dataset.

**Nguồn:** [Kaggle – ziya07](https://www.kaggle.com/datasets/ziya07/contextual-sentiment-feedback-dataset)

**Tệp dữ liệu:** `student_feedback_dataset.csv`

Thông tin tổng quan:

| Thông tin | Giá trị |
|---|---|
| Tổng số mẫu | 1.223 |
| Tổng số cột | 11 |
| Cột văn bản | `feedback_text` |
| Cột nhãn | `sentiment_label` |
| Positive | 489 |
| Neutral | 368 |
| Negative | 366 |

Dữ liệu được chia thành 978 mẫu huấn luyện và 245 mẫu kiểm thử, sử dụng `random_state=42` và phân tầng theo nhãn.

## 3. Phương pháp thực hiện

Quy trình gồm các giai đoạn:

1. Khám phá và phân tích dữ liệu (EDA).
2. Làm sạch văn bản và kiểm tra dữ liệu.
3. Chia dữ liệu Train/Test.
4. Biểu diễn văn bản bằng Bag-of-Words và TF-IDF.
5. Huấn luyện Multinomial Naive Bayes và K-NN.
6. Lựa chọn siêu tham số bằng Stratified 3-Fold Cross-Validation.
7. Đánh giá mô hình và phân tích những dự đoán sai.

Nhóm thử nghiệm bốn cấu hình biểu diễn đặc trưng: BoW Unigram, BoW Unigram–Bigram, TF-IDF Unigram và TF-IDF Unigram–Bigram.

Tiêu chí lựa chọn mô hình là **Macro F1-score trên Cross-Validation**. Tập kiểm thử được giữ riêng trong quá trình chọn mô hình.

## 4. Cấu trúc dự án

Các thành phần chính của dự án:

- `data/`: Chứa bộ dữ liệu CSV.
- `notebook/01_EDA.ipynb`: Khám phá và phân tích dữ liệu.
- `notebook/02_Preprocessing.ipynb`: Tiền xử lý, chia dữ liệu và vector hóa.
- `notebook/03_Training.ipynb`: Huấn luyện, thử nghiệm siêu tham số.
- `notebook/04_Evaluation.ipynb`: Đánh giá và phân tích lỗi.
- `src/text_utils.py`: Hàm làm sạch văn bản dùng chung.
- `results/`: Lưu dữ liệu trung gian và kết quả thực nghiệm.
- `requirements.txt`: Khai báo thư viện cần thiết.
- `README.md`: Giới thiệu và hướng dẫn chạy chương trình.

Thư mục `results/` gồm các đầu ra chính:

- `results/eda/` và `results/figures/`: Thống kê và biểu đồ EDA.
- `results/member2_outputs/`: Dữ liệu train/test và các bộ vector hóa.
- `results/training/`: Kết quả Cross-Validation, mô hình và dự đoán.
- `results/evaluation/`: Bảng chỉ số, Confusion Matrix và phân tích lỗi.

## 5. Cài đặt môi trường

**Python khuyến nghị:** 3.11.

Có thể sử dụng Anaconda và Visual Studio Code.

Tạo môi trường mới trong Anaconda Prompt:

`conda create -n fit4013 python=3.11 -y`

`conda activate fit4013`

Mở terminal tại thư mục gốc dự án và cài đặt thư viện:

`python -m pip install -r requirements.txt`

Kiểm tra các gói đã cài:

`python -m pip check`

Trong Visual Studio Code, chọn môi trường Python vừa tạo làm Jupyter Kernel.

## 6. Chuẩn bị dữ liệu

Tải dataset từ liên kết Kaggle ở Mục 2.

Đặt tệp CSV tại:

`data/student_feedback_dataset.csv`

Kiểm tra tệp `src/text_utils.py` tồn tại trước khi chạy notebook tiền xử lý.

## 7. Hướng dẫn chạy chương trình

Chạy bốn notebook theo đúng thứ tự:

**Bước 1 – `01_EDA.ipynb`**

Đọc dữ liệu, kiểm tra chất lượng, thống kê phân phối nhãn và tạo các biểu đồ EDA.

**Bước 2 – `02_Preprocessing.ipynb`**

Làm sạch văn bản, kiểm tra dữ liệu, chia Train/Test và tạo các bộ vector hóa BoW/TF-IDF.

Đầu ra được lưu trong `results/member2_outputs/`.

**Bước 3 – `03_Training.ipynb`**

Đọc dữ liệu từ notebook 02, huấn luyện baseline, Naive Bayes và K-NN, thử nghiệm siêu tham số bằng GridSearchCV.

Đầu ra được lưu trong `results/training/`.

**Bước 4 – `04_Evaluation.ipynb`**

Đọc kết quả từ notebook 03, tổng hợp các chỉ số đánh giá, tạo biểu đồ so sánh, Confusion Matrix và phân tích các phản hồi dự đoán sai.

Đầu ra được lưu trong `results/evaluation/`.

**Lưu ý:** Cần chạy các ô trong từng notebook từ đầu đến cuối. Notebook 03 yêu cầu đầu ra từ notebook 02, còn notebook 04 yêu cầu đầu ra từ notebook 03.

## 8. Kết quả thực nghiệm

Nhóm sử dụng Accuracy, Precision, Recall, Macro F1-score và Confusion Matrix để đánh giá.

Kết quả chính:

| Phương án | Macro F1 trên test |
|---|---:|
| DummyClassifier | 0,1905 |
| Baseline BoW Unigram + Naive Bayes | 0,3748 |
| TF-IDF Unigram + K-NN, k=5 | 0,3369 |

Cấu hình TF-IDF Unigram kết hợp K-NN đạt Macro F1 trung bình cao nhất trên CV là 0,3647, nhưng chưa vượt baseline trên tập kiểm thử.

Các kết quả cho thấy mô hình còn hạn chế trong việc phân biệt ba lớp cảm xúc và chưa đủ cơ sở để triển khai trong môi trường ứng dụng thực tế.

## 9. Báo cáo khoa học

Báo cáo được viết bằng LaTeX theo hướng dẫn học phần FIT4013.

Nội dung gồm sáu chương: đặt vấn đề, thiết kế giải pháp, phân tích mã nguồn, thử nghiệm, thảo luận và tổng kết hướng phát triển.

## 10. Phân công và đóng góp

Các thành viên phối hợp thực hiện các giai đoạn khám phá dữ liệu, tiền xử lý, huấn luyện mô hình, đánh giá và viết báo cáo.

Lịch sử commit trên GitHub được sử dụng để minh chứng quá trình phát triển và đóng góp của các thành viên.

## 11. Sử dụng công cụ AI

Nhóm có sử dụng ChatGPT để hỗ trợ tìm hiểu kiến thức, gợi ý và kiểm tra mã nguồn, xử lý lỗi, phân tích kết quả và soạn thảo báo cáo LaTeX.

Nhóm chịu trách nhiệm kiểm tra, đối chiếu số liệu và giải thích các phương pháp, mã nguồn và kết quả được nộp.

Nội dung khai báo chi tiết được trình bày trong phụ lục báo cáo hoặc file `AI_USAGE.md`.

## 12. Tài liệu tham khảo

- Tài liệu hướng dẫn bài tập lớn FIT4013, năm học 2026–2027.
- Tài liệu chính thức của [Scikit-learn](https://scikit-learn.org/stable/).
- Bộ dữ liệu Contextual Sentiment Feedback Dataset trên Kaggle.
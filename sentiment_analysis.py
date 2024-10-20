from transformers import pipeline

# Tạo một pipeline cho phân loại cảm xúc
classifier = pipeline("sentiment-analysis")

# Phân loại một câu
result = classifier("Hôm nay là một ngày tuyệt vời!")
print(result)  # Kết quả sẽ cho bạn biết cảm xúc của câu

# thêm mới cho oách

# thêm cái nữa xem sao



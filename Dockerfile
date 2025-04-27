# 使用官方 Python image
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製目前資料夾所有檔案到容器
COPY . .

# 安裝 requirements.txt 裡的套件
RUN pip install --no-cache-dir -r requirements.txt

# 直接跑 bot.py
CMD ["python", "bot.py"]

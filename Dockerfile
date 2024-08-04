# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを作成し、設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
  libjpeg-dev \
  zlib1g-dev

# Pythonのライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコンテナ内にコピー
COPY . .

# スクリプトを実行するエントリーポイントを指定
ENTRYPOINT ["python", "convert_images.py"]

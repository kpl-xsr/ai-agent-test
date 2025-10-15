FROM mcr.microsoft.com/devcontainers/python:3.12

# 必要に応じて OS パッケージなどを追加
RUN apt-get update && apt-get install -y \
    curl git vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# requirements.txt をコピー（存在しない場合はスキップしてOK）
COPY requirements.txt* ./

# 仮想環境を有効にしてパッケージをインストール（失敗しても続行）
RUN pip install --upgrade pip && pip install -r requirements.txt || true
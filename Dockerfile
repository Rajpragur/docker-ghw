FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pizza_steak

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV TF_ENABLE_ONEDNN_OPTS=0

CMD ["python3","app.py"]
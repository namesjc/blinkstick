FROM python:3.9.2-slim-buster

WORKDIR /app

RUN apt update && \
    apt install -y libusb-1.0-0-dev libudev-dev && \
    rm -rf /var/apt/lists/*

ENV red=0
ENV green=0
ENV blue=0

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple

COPY /app .

CMD [ "python", "./app/blink_controller.py" ]

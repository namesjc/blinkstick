FROM python:3.9.2-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple

CMD [ "python", "./app/blink_single.py" ]

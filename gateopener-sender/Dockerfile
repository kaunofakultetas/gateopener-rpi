FROM python:3.13.7-slim

WORKDIR app

RUN pip3 install --no-cache-dir      \
    "requests==2.32.5"

COPY . .

CMD ["python3", "-u", "sender.py"]

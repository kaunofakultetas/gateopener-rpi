FROM python:3.13.7-slim

WORKDIR app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install --no-cache-dir      \
    "Flask==3.0.0"                  \
    "Flask-CORS==4.0.0"             \
    "RPi.GPIO==0.7.1"


EXPOSE 8000
CMD ["python", "main.py", "--http"]
FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt  && \
    pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

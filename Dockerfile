
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

COPY app/requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip setuptools wheel \
    && python -m pip install --no-cache-dir --target=/install -r requirements.txt

FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y python3.11 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /install /install
ENV PYTHONPATH=/install

COPY app/ ./app/

EXPOSE 5000

USER 65532:65532

CMD ["python3.11", "-m", "app.main"]

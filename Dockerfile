FROM python:3.9-slim as builder  

WORKDIR /app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt && \
    rm -rf /root/.cache/pip/* && rm -rf /var/cache/apk/* && rm -rf /tmp/*


FROM python:3.9-slim
WORKDIR /app
COPY . .
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache-dir /wheels/* && groupadd group && useradd user -G group && \
    chown -R user:group /app && chmod +x init.sh

USER user

CMD ["sh", "-c", "sh /app/init.sh"]

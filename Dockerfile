FROM python:3-alpine3.15

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN apk --no-cache add nodejs npm && \
    apk --no-cache add build-base libffi-dev && \
    pip install -r requirements.txt

CMD ["python", "app.py"]

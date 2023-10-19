FROM python:3-alpine3.15

RUN apk --no-cache add nodejs npm

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN apk --no-cache add build-base libffi-dev
RUN pip install -r requirements.txt

CMD ["python", "app.py"]

FROM python:3.12-slim

WORKDIR /app

COPY .env .
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "server.wsgi"]
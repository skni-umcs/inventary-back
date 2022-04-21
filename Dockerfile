# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code


COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code


CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]

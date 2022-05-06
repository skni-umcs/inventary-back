#syntax=docker/dockerfile:1
FROM python:3.10.4-bullseye
WORKDIR /code


COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code


CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8555"]

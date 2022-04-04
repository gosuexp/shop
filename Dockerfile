FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /online_store/online_shop/

EXPOSE 8000

COPY requirements.txt /online_store/online_shop/

RUN pip install -r requirements.txt




FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD manage.py /code/
RUN pip install -r requirements.txt
COPY . /code/
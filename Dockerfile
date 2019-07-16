FROM python:3

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
# Set work directory
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

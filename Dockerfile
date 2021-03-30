FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/database
RUN mkdir /code/staticfiles
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /code/
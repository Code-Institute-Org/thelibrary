FROM ubuntu:20.04

# ENV TZ=Europe/Dublin
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip libmysqlclient-dev build-essential mysql-client curl
RUN apt-get install libpcre3 libpcre3-dev -y
RUN apt-get install postgresql-server-dev-12 gcc python3-dev musl-dev -y

WORKDIR /thelibrary

COPY requirements.txt /thelibrary
RUN pip3 install -r requirements.txt

COPY ./src /thelibrary
COPY ./uwsgi.ini /thelibrary

# RUN python3 manage.py collectstatic --no-input

EXPOSE 8000
ENTRYPOINT ["uwsgi", "--enable-threads", "--ini", "uwsgi.ini"]
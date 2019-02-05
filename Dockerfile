FROM python:alpine3.7

RUN apk add --no-cache bash
RUN pip3 install flask
RUN pip3 install gunicorn

ADD ./src /app

EXPOSE 8888

WORKDIR /app

CMD ["bash", "run_gunicorn.sh"]
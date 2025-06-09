FROM python:3.10.12-alpine3.18@sha256:5d1dafb473686c5435faed90387956d6f1fdd919e4ced85eb2aa5ac45d29a98c

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN apk add chromium chromium-chromedriver
COPY ./ /home/
WORKDIR /home/app

CMD ["python3", "-u", "app.py"]
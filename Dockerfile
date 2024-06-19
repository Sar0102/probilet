FROM python:3.11.7-alpine3.19 as base

WORKDIR /home/user/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade setuptools pip && \
    pip install psycopg2-binary && \
    rm -rf /var/cache/apk/*

RUN apk install -y make

COPY ./requirements.txt .
RUN pip install -r requirements.txt


# Multistage build
FROM python:3.11.7-alpine3.19

WORKDIR /home/user/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY Makefile ./Makefile
COPY . .

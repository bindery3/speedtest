FROM python:3.7-slim AS build

RUN pip install --no-cache-dir flask flask_httpauth gevent speedtest-cli --prefix=/install


FROM python:3.7-alpine

ENV USERNAME=speedtest \
    PASSWORD=speedtest

WORKDIR /speedtest

COPY --from=build /install /usr/local
COPY main.py ./

EXPOSE 8000

CMD python main.py $USERNAME $PASSWORD

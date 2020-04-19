FROM python:3.8.2-alpine

RUN apk update && \
    apk add make && \
    apk add --virtual .build-deps gcc musl-dev

ADD requirements/requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt --no-cache-dir -q

RUN apk --purge del .build-deps


ADD src /app
WORKDIR /app

EXPOSE 5555

#CMD ["uvicorn", "mealprephelper:app", "--reload", "--host", "0.0.0.0", "--port", "5555"]

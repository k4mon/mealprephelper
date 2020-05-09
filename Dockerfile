FROM python:3.8.2-alpine

RUN apk update && \
    apk add make && \
    apk add --virtual .build-deps gcc musl-dev libffi-dev

ADD requirements/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt --no-cache-dir -q

RUN apk --purge del .build-deps


ADD mealprephelper /app/mealprephelper
ENV PYTHONPATH=/app
WORKDIR /app
EXPOSE 5555

CMD ["uvicorn", "mealprephelper.main:app", "--reload", "--host", "0.0.0.0", "--port", "5555"]

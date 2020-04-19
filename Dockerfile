FROM python:3.8.2-alpine

RUN apk update && \
    apk add make postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev

ADD requirements/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt --no-cache-dir -q

RUN apk --purge del .build-deps


ADD mealprephelper /app/mealprephelper
ADD alembic /app/alembic
ENV PYTHONPATH=/app
EXPOSE 5555

#CMD ["uvicorn", "mealprephelper:main", "--reload", "--host", "0.0.0.0", "--port", "5555"]

FROM python:3-alpine

RUN mkdir -p /code && python -m pip install --upgrade pip

ENV PYTHONUNBUFFERED 1

COPY . /code

WORKDIR /

RUN pip install -r code/requirements.txt

CMD [ "python", "code/testapi/manage.py", "runserver", "0.0.0.0:8001", "--settings=testapi.settings" ]

#!/bin/bash
set -e
pipenv run python testapi/manage.py migrate --noinput
pipenv run python testapi/manage.py runserver 0.0.0.0:8001
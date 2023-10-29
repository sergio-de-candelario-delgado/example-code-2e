FROM python:3.11 as builder

WORKDIR /app

ARG CI_BUILD=0

RUN apt-get update -yq && apt-get install python3-dev -yq

RUN pip install poetry==1.6.1

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH="${PYTHONPATH}:/src"

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry config virtualenvs.create false \
  && poetry install $(if [ "$CI_BUILD" = 0 ]; then echo '--without dev'; fi) --no-interaction --no-ansi

ENV VIRTUAL_ENV=/packages/ \
    PATH="/packages/bin:$PATH"

COPY . /app

CMD uvicorn main:app --host 0.0.0.0 --app-dir src
FROM python:3.7

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 8000

CMD gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker -b 0.0.0.0:8000 app:app

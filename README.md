# backend

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/Spin14/wolf-backend.svg?branch=master)](https://travis-ci.com/Spin14/wolf-backend)
[![codecov](https://codecov.io/gh/Spin14/wolf-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/Spin14/wolf-backend)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Intro

This is a `asgi - starlette` demo project. 

What's [_asgi_](https://asgi.readthedocs.io/en/latest/index.html)? In short, the successor to [_wsgi_](https://docs.python.org/3.7/library/wsgiref.html)!

It features:

- `starlette` [asgi framework](https://github.com/encode/starlette)
- `uvicorn` [asgi server](https://github.com/encode/uvicorn)
- `gunicorn` [http server](https://github.com/benoitc/gunicorn)
- `poetry` [dependency manager](https://github.com/sdispater/poetry)
- `databases` [async db support](https://github.com/encode/databases)
- `sqlalchemy` [sql toolkit](https://github.com/sqlalchemy/sqlalchemy)
- `alembic` [database migrations](https://github.com/sqlalchemy/alembic)
- `black` [code formatter](https://github.com/python/black)
- `flake8` [style checker](https://github.com/PyCQA/flake8)
- `mypy` [static type checker](https://github.com/python/mypy)
- `xenon` [cyclomatic complexity checker](https://github.com/rubik/xenon)
- `pytest` [test framework](https://github.com/pytest-dev/pytest)
 
 and:
 
 - a `Dockerfile` for [simple deployment](https://docs.docker.com/engine/reference/builder/)
 - a `travis` config for [continuous integration](https://travis-ci.org/getting_started)


## Development

### Setup Poetry

Using [poetry](https://github.com/sdispater/poetry) for project dependency management

```bash
# make sure poetry is installed
$ which poetry
/usr/local/bin/poetry

# how I setup poetry
$ poetry config settings.virtualenvs.create false
$ poetry config settings.virtualenvs.in-project true 

$ poetry config --list                               
settings.virtualenvs.create = false
settings.virtualenvs.in-project = true
```

### Install Dependencies

```bash
# create venv
$ python3.7 -m venv .venv
$ source venv/bin/activate

# install project dependencies
$ poetry install
```

### Setup Environment

```bash
# .env for development
$ ln -s .env.dev .env
```

### Code Formatting

```bash
$ balck app tests
All done! ✨ 🍰 ✨
18 files left unchanged.

$ black app tests --check # this one is for CI
``` 

### Import Sorting
```bash
$ isort -rc app tests

$ isort -rc app tests --check-only # this one is for CI
```

### Lint Checks

```bash
$ flake8 app tests
```

### Type Checks

```bash
$ mypy app tests
```

### Cyclomatic Complexity

```bash
$ radon cc app -n B -s
$ radon cc tests -n B -s

$ xenon app -b A # this one is for CI
$ xenon tests -b A # this one is for CI
```

### Run Tests
```bash
$ pytest
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.7.1, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/juan/Projects/WOLF/backend, inifile: setup.cfg
plugins: cov-2.7.1
collected 17 items                                                                                                                                                                           

tests/test_auth.py ...                                                                                                                                                                 [ 17%]
tests/test_config.py .                                                                                                                                                                 [ 23%]
tests/test_endpoints.py ...........                                                                                                                                                    [ 88%]
tests/test_loggers.py .                                                                                                                                                                [ 94%]
tests/test_models.py .                                                                                                                                                                 [100%]

----------- coverage: platform linux, python 3.7.1-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
app/__init__.py                18      0   100%
app/auth.py                    24      0   100%
app/config.py                   7      0   100%
app/db.py                      14      0   100%
app/endpoints.py               53      0   100%
app/exception_handlers.py       5      0   100%
app/logging.py                  9      0   100%
app/models.py                   3      0   100%
app/routes.py                   5      0   100%
app/static.py                   3      0   100%
app/tasks.py                   11      0   100%
tests/__init__.py               0      0   100%
tests/conftest.py              31      0   100%
tests/test_auth.py             24      0   100%
tests/test_config.py            3      0   100%
tests/test_endpoints.py        72      0   100%
tests/test_loggers.py           5      0   100%
tests/test_models.py           22      0   100%
-----------------------------------------------
TOTAL                         309      0   100%

Required test coverage of 100% reached. Total coverage: 100.00%

================================================================================= 17 passed in 0.50 seconds ==================================================================================
```
```bash
# for ipdb compatibale test runs
# $ pytest -s

# for detailed coverage report
$ coverage html
$ firefox htmlcov/index.html

```

### Run DB migrations

```bash
$ alembic upgrate head
...
INFO  [alembic.runtime.migration] Running upgrade  -> 8a4192a2406a, create protocols table
INFO  [alembic.runtime.migration] Running upgrade 8a4192a2406a -> 1a9952031305, update protocols table: is_cool col
...

$ alembic revision --autogenerate -m "update protocols table: add example col"
...
INFO  [alembic.autogenerate.compare] Detected added column 'protocols.example'
...

```

### Run Dev Server

```bash
# run asgi server with auto load
$ ./dev.sh
```


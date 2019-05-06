# backend

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Build Status](https://travis-ci.com/Spin14/wolf-backend.svg?branch=master)](https://travis-ci.com/Spin14/wolf-backend)
[![codecov](https://codecov.io/gh/Spin14/wolf-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/Spin14/wolf-backend)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

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
settings.virtualenvs.in-project = false
settings.virtualenvs.path = "/home/<user>/.cache/pypoetry/virtualenvs"
repositories = {}
```

### Install Dependencies

```bash
# create venv
$ python3.7 -m venv venv
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

$ black app tests --check # this one is for CI
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
============================================================================================ test session starts ============================================================================================
platform linux -- Python 3.7.1, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/juan/Projects/WOLF/backend, inifile: setup.cfg
plugins: cov-2.7.1
collected 1 item                                                                                                                                                                                            

tests/test_app.py .                                                                                                                                                                                   [100%]

----------- coverage: platform linux, python 3.7.1-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
app/__init__.py         4      0   100%
app/config.py           3      0   100%
app/endpoints.py        4      0   100%
app/routes.py           4      0   100%
tests/__init__.py       0      0   100%
tests/test_app.py       8      0   100%
---------------------------------------
TOTAL                  23      0   100%

Required test coverage of 100% reached. Total coverage: 100.00%

========================================================================================= 1 passed in 0.12 seconds ==========================================================================================

# for ipdb compatibale test runs
# $ pytest -s

# for detailed coverage report
$ coverage html
$ firefox htmlcov/index.html

```

### Run Server

```bash
# run asgi server with auto load
$ ./dev.sh
```

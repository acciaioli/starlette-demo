# wolf backend


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

### Run Server

```bash
# run asgi server with auto load
$ ./dev.sh
```

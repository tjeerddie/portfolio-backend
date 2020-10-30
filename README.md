# portfolio-backend

backend for a portfolio website...

## features
- [ ] able to use django admin to populate your portfolio.
- [ ] todo...

## Setup

for now there is only a `poetry` setup, I do want to add `docker` at some point.

### Dev setup

1. Install [python](https://www.python.org/downloads/)
2. Install poetry, can be done with `pip install poetry`.
3. Install packages with poetry using: `poetry install`.
4. Copy and paste `cp .example.env env` and configure it for your environment.
   1. TODO: more details...
5. Migrate the database:
   1. I prefer to use poetry shell in which you can use: `py manage.py migrate`.
   2. You can also use `poetry run py manage.py migrate` outside of the shell.
6. (optional/add your own fixture) Adding pre-defined data using fixtures:
   1. In poetry shell: `py manage.py loaddata FILE` where `FILE` is the file in the fixture folder.
   2. With poetry run: `poetry run py manage.py loaddata FILE`.
7. create a super user with `py manage.py createsuperuser`.
8. Running the project:
   1. In poetry shell: `py manage.py runserver`.
   2. With poetry run: `poetry run py manage.py runserver`.


### Production setup

TODO

info available at:
- https://docs.djangoproject.com/en/3.1/howto/deployment/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

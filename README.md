# travel-api

Migrate Database:
$ flask db init
$ flask db migrate

Run in Development:
$ python wsgi.py

Run in Production:
$ gunicorn wsgi:handler
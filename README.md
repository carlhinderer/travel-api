# travel-api

Migrate Database:
$ flask db init
$ flask db migrate

Run in Development:
$ python app.py OR 
$ flask run

Run in Production:
$ gunicorn wsgi:handler
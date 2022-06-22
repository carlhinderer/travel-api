# travel-api

#h4 Migrate Database

> $ flask db init
> $ flask db migrate -m commit_message
> $ flask db upgrade

#h4 Run in Development
> $ python app.py OR 
> $ flask run

#h4 Run in Production
> $ gunicorn wsgi:handler
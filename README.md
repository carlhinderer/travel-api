# travel-api

#### Migrate Database

`$ flask db init`  
`$ flask db migrate -m commit_message`  
`$ flask db upgrade`

#### Run in Development

`$ python app.py` OR  
`$ flask run`

#### Run in Production

`$ gunicorn wsgi:handler`
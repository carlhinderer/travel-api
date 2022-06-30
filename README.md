# travel-api

#### Migrate Database

`$ flask db init`  
`$ flask db migrate -m commit_message`  
`$ flask db upgrade`

#### Run in Development

`$ flask run`

#### Run tests

`$ python -m pytest tests`

#### Run in Production

`$ gunicorn wsgi:handler`
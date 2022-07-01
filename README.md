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

#### Development

Put configuration settings in `settings.toml` at the project root.
Put secrets in `.secrets.toml`, also at the project root.
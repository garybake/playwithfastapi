# playwithfastapi

Basic pointless app, so I can toy around with structure and web toys.

v1.0
- Basic structure for fastapi project
- Jinja2 templating with bootstrap 5


    uvicorn app.main:app   
    python -m app.main

For the locations page you will need to add the following env key from mapbox.com  
`MAPBOX_API_KEY`

## Dev

    pip install -r requirements-dev.txt 
    pre-commit install

Precommit runs the following
 - Black
 - Flake8

## Links
https://github.com/skb1129/fastapi-boilerplate  
https://official-joke-api.appspot.com/random_joke  
https://leafletjs.com/

## TODO
 - Add more tests
 - Add maps to front end
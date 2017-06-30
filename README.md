# Movies API

This API endpoint lets you post, update, get all movies and get other information about a movie to a deployed database.
A deployed version can be found on https://dkimmoviesapi.herokuapp.com/

## Getting Started

The current build is set up to be run on Heroku. 
The following endpoints can be accessed:
- GET at https://dkimmoviesapi.herokuapp.com/movies/ to get all movies in the DB
- GET at https://dkimmoviesapi.herokuapp.com/movies/{movie id} to get specific movie in the DB with IMDB and metascore ratings
- POST at https://dkimmoviesapi.herokuapp.com/movies/ with a JSON object/file with the parameters of title and rating to add a row to the DB
- PUT at https://dkimmoviesapi.herokuapp.com/movies/ with same JSON as POST to update a row in the DB

### Prerequisites

Django, Python 3 and modules in requirements.txt

### Installing and Deploying

To begin you must first get an API key from http://www.omdbapi.com/ by becoming a patron for pledging a dollar. After you've acquired the key place it in movies/views.py where apikey is the variable.
Second, you must set up a database and put its information in moviesapi/settings.py DATABASES configuration.
Install Python and run manage.py runserver on your command line interpreter.
You can also deploy this app directly to Heroku.

## Authors

* **David Kim** - *Initial work* - [drakexp](https://github.com/drakexp)

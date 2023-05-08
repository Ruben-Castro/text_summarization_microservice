![Continuous Integration and Delivery](https://github.com/ruben-castro/text_summarization_microservice/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

# Live site 
- https://frozen-chamber-25489.herokuapp.com/docs

# Text Summarization Microservice
Text summarization is a microservice web api written in using the FastAPI Framework, an asynchronous python web framework very similar to flask but with built it type hinting, OPEN API Schema, Dependency Injections and much more. This api outputs a summary of the input where input is a news article. 

## Tech Stack 
 - FastAPI
 - Postgres database
 - pytest
 - tortoise orm a asynchronous ORM
 - aerich for database migrations 
 - Docker 
 - Docker Compose 


## What I learned
- how to use FastAPI 
- The importance of TDD and how to efficiently do it in a FastAPI App
- how to dockerize fastapi and deploy on Heroku
- how to set up a postgres database in a docker container
- 

### Future State 
- consume this API in a client application
- add api key, and rate limiting to the API. 

### How to Run locally 
- install docker on your local computer 
- clone this repository
- cd into the root directory of the clone project 
- in a your terminal execute the following docker-compose up -d --build
- in your browser go to localhost:8004/


#### Useful pytest commands 
- normal run
  docker-compose exec web python -m pytest

- disable warnings
 docker-compose exec web python -m pytest -p no:warnings

- run only the last failed tests
 docker-compose exec web python -m pytest --lf

- run only the tests with names that match the string expression
  docker-compose exec web python -m pytest -k "summary and not test_read_summary"

- stop the test session after the first failure
 docker-compose exec web python -m pytest -x

- enter PDB after first failure then end the test session
 docker-compose exec web python -m pytest -x --pdb

- stop the test run after two failures
 docker-compose exec web python -m pytest --maxfail=2

- show local variables in tracebacks
 docker-compose exec web python -m pytest -l

- list the 2 slowest tests
 docker-compose exec web python -m pytest --durations=2


 #### Code Coverage with pytest-cov
 - docker-compose exec web python -m pytest --cov="."
 generates report in the terminal 
 - docker-compose exec web python -m pytest --cov="." --cov-report html
 generates html report 

 #### run unit test in parallel 
 - docker-compose exec web pytest -k "unit" -n auto
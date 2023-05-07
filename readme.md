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



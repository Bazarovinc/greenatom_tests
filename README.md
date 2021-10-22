# How to start the application
* Build the project in docker
```
docker-compose build
```
* Up database
```
docker-compose up -d db
```
* Upgrade alembic head
```
docker-compose run backend alembic upgrade head
```
* Up the application
```
docker-compose up
```

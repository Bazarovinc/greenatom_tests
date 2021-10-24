#!/bin/bash
docker-compose build
docker-compose up -d db
sleep 10
docker-compose run backend alembic upgrade head
docker-compose up -d backend
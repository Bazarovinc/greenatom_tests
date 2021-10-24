#!/bin/bash
docker-compose build
docker-compose up -d db
docker-compose run backend alembic upgrade head
docker-compose up -d backend
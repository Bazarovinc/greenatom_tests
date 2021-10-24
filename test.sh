#!/bin/bash
docker-compose up -d backend db
sleep 20
docker-compose up test
docker-compose stop
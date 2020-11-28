#!/bin/bash
docker-compose  up  --build -d

docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py makemigrations supply_order
docker-compose run web python manage.py migrate
docker-compose run web python seeder.py
docker exec -it driver_quality_web_1 python client.py

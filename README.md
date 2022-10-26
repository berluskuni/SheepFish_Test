# SheepFish_Test
- python3 -m venv venv
- source venv/bin/activate
- - docker-compose up -d
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py loaddata printer/fixtures/printer.json
- ./manage.py runserver 

## Start Celery worker 
New window activate virtualenv basedir and 

celery -A django_drf worker -l INFO

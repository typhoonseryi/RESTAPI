sudo docker run -d -p 27017:27017 mongo
python somemart/manage.py migrate
python somemart/manage.py runserver
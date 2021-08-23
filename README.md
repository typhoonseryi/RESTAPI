# Для запуска сервиса необходимо выполнение следующих команд:
## 1) bash init.sh
## 2) python somemart/manage.py migrate
## 3) python somemart/manage.py runserver
#
# cURL-команды для проверки работы сервиса:
## 1) Создание товара:
### curl -d '{"title": "Samsung Galaxy A52", "description": "Оцените плавность контуров элегантного дизайна смартфона Samsung Galaxy A52.", "params": {"memory": 256, "cpu": "Snapdragon 720G", "performance": 2300}}' -H "Content-type: application/json" -X POST http://localhost:8000/api/v1/goods/
## 2.1) Поиск товара по названию:
### curl -d '{"filter": {"title": "Samsung Galaxy A52"}}' -H "Content-type: application/json" -X GET http://localhost:8000/api/v1/goods/
## 2.2) Поиск товара по параметру:
### curl -d '{"filter": {"memory": 256}}' -H "Content-type: application/json" -X GET http://localhost:8000/api/v1/goods/
## 3) Получить детали товара (id=1):
### curl -X GET http://localhost:8000/api/v1/goods/1/

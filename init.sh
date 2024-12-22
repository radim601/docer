#!/bin/sh
sleep 5  # Ждем, пока база данных будет готова

# Инициализация миграций
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Запуск приложения
python app.py


# Лабораторная работа. Тема: докеризация
## Описание

В файле Dockerfile происходит установка требований из файла requirements.txt и перемещение файлов, затем создается непривилегированный пользователь со своей группой, от которого будет запускаться приложение. В данном файле была реализована многоэтапная сборка.

В docker-compose.yml указаны порты, переменные окружения и зависимости

Переменные окружения находятся в файле .env

Миграции осуществляются с помощью файла init.sh в котором используется Flask-Migrate. Они выполняются при старте приложения.

## Запуск
Запуск происходит с помощью команды

$ docker-compose up --build

После запуска можно открыть страницу http://localhost:5000/.

Для прекращения работы контейнера используется команда

$ docker-compose down

Что бы добавить нового человека в таблицу необходимо вписать в консоль команду:

$ curl -X POST -H "Content-Type: application/json" -d '{"username": "john"}' http://localhost:5000/users

Что бы вывести всех добавленных людей необходима команда:

curl http://localhost:5000/users

## Работу выполнили
Мещеряков Радомир 2383, Малюская Дарья 2381

# Oximeter REST Api

Project made for my Microcontrollers class, the goal of this project is to collect the heartrate and oxygen saturation data using the ESP32 microcontroller
and the MAX30100 sensor. The whole project is divided into 3 parts/repositories: the [microcontroller firmware](https://github.com/LaBatata101/oximeter-esp32-firmware),
the REST Api (this repository) for the data management and the [Telegram bot](https://github.com/LaBatata101/oximeter-telegram-bot) for real time data visualization.

The API offers 5 routes to manipulate the data received from the sensor, you can check them by going to [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)
after running the project.

## Dependencies
- fastapi v0.78.0
- SQLAlchemy v1.4.39
- uvicorn v0.18.2
- alembic v1.8.0
- psycopg2-binary v2.9.3
- PostgreSQL v14.3

## Installing and running the project
Clone the project:
```bash
$ git clone https://github.com/LaBatata101/oximeter-rest-api
$ cd oximeter-rest-api/
```

Installing the dependencies using `pip`:
```bash
$ pip install -r requirements.txt
```
Or, using `poetry`:
```bash
$ poetry install
```
Running:
```bash
$ POSTGRES_USER=YOUR_DB_USER POSTGRES_PASSWORD=YOUR_DB_PASSWORD POSTGRES_SERVER=YOUR_DB_SERVER POSTGRES_DB=YOUR_DB_NAME uvicorn oximeter.main:app --reload
```

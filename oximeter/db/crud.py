from datetime import datetime
from typing import Optional

from sqlalchemy import extract
from sqlalchemy.orm import Session

from oximeter import models
from oximeter.schemas import SensorDataCreate


def create_sensor_data(db: Session, sensor_data: SensorDataCreate) -> models.SensorData:
    db_user = models.SensorData(
        user_id=sensor_data.user_id, bpm=sensor_data.bpm, spo2=sensor_data.spo2, date=sensor_data.date
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_sensor_data_by_date_day(db: Session, date: datetime) -> list[models.SensorData]:
    return (
        db.query(models.SensorData)
        .filter(extract("day", models.SensorData.date) == date.day)
        .filter(extract("month", models.SensorData.date) == date.month)
        .filter(extract("year", models.SensorData.date) == date.year)
        .all()
    )


def get_sensor_data_by_date_month(db: Session, date: datetime) -> list[models.SensorData]:
    return (
        db.query(models.SensorData)
        .filter(extract("month", models.SensorData.date) == date.month)
        .filter(extract("year", models.SensorData.date) == date.year)
        .all()
    )


def get_sensor_data_by_date_year(db: Session, date: datetime) -> list[models.SensorData]:
    return db.query(models.SensorData).filter(extract("year", models.SensorData.date) == date.year).all()


def get_all_sensor_data_for_user_id(db: Session, user_id: int) -> list[models.SensorData]:
    return db.query(models.SensorData).filter(models.SensorData.user_id == user_id).all()


def get_all_sensor_data(db: Session, skip: int = 0, limit: int = 100) -> list[models.SensorData]:
    return db.query(models.SensorData).offset(skip).limit(limit).all()


def get_last_row(db: Session):
    return db.query(models.SensorData).order_by(models.SensorData.id.desc()).first()


def delete_sensor_data(db: Session, *, id: int) -> Optional[models.SensorData]:
    sensor_data = db.query(models.SensorData).get(id)
    if not sensor_data:
        return None

    db.delete(sensor_data)
    db.commit()

    return sensor_data

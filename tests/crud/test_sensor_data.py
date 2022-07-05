from datetime import datetime
from sqlalchemy.orm import Session
from oximeter.db.crud import get_last_row, create_sensor_data
from oximeter.schemas.sensor_data import SensorDataCreate, SensorData


def test_last_row(db: Session):
    d1 = create_sensor_data(db, SensorDataCreate(user_id=0, bpm=90, spo2=98, date=datetime.now()))
    d2 = create_sensor_data(db, SensorDataCreate(user_id=0, bpm=95, spo2=96, date=datetime.now()))
    d3 = create_sensor_data(db, SensorDataCreate(user_id=0, bpm=99, spo2=99, date=datetime.now()))

    last_row = SensorData.from_orm(get_last_row(db))

    assert last_row != SensorData.from_orm(d1)
    assert last_row != SensorData.from_orm(d2)
    assert last_row == SensorData.from_orm(d3)

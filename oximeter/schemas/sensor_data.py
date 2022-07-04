from datetime import datetime

from pydantic import BaseModel


class SensorDataBase(BaseModel):
    user_id: int
    bpm: int
    spo2: int
    date: datetime


class SensorDataCreate(SensorDataBase):
    ...
    class Config:
        schema_extra = {
            "example": {
                "user_id": 0,
                "bpm": 95,
                "spo2": 99,
                "date": "2022-07-04T20:15:42",
            }
        }


class SensorData(SensorDataBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "user_id": 0,
                "bpm": 95,
                "spo2": 99,
                "date": "2022-07-04T20:15:42",
            }
        }

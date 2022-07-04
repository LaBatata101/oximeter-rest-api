from datetime import datetime

from pydantic import BaseModel


class SensorDataBase(BaseModel):
    user_id: int
    bpm: int
    spo2: int
    date: datetime


class SensorDataCreate(SensorDataBase):
    ...


class SensorData(SensorDataBase):
    id: int

    class Config:
        orm_mode = True

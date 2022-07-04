from sqlalchemy import Column, DateTime, Integer
from oximeter.db import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    bpm = Column(Integer, nullable=False)
    spo2 = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=False, index=True)

    def __str__(self) -> str:
        return f"SensorData({self.id=}, {self.user_id=}, {self.bpm=}, {self.spo2=}, {self.date=})"

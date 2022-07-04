from datetime import datetime
from fastapi import APIRouter, HTTPException, Query, Depends, status
from sqlalchemy.orm import Session

from oximeter.db import crud
from oximeter.schemas import SensorData, SensorDataCreate
from oximeter.api.dependencies import get_db

route = APIRouter(prefix="/sensor", tags=["sensor"])


@route.post("/", response_model=SensorData, status_code=status.HTTP_201_CREATED)
def post_data(sensor_data: SensorDataCreate, db: Session = Depends(get_db)):
    return crud.create_sensor_data(db, sensor_data)


@route.get("/", response_model=list[SensorData])
def get_all_data(skip: int = Query(0, ge=0), limit: int = Query(100, ge=0), db: Session = Depends(get_db)):
    return crud.get_all_sensor_data(db, skip, limit)


@route.get("/{date}", response_model=SensorData)
def get_data_by_date(date: datetime, db: Session = Depends(get_db)):
    data = crud.get_sensor_data_by_date(db, date)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found for date.")
    return data


@route.get("/{user_id}", response_model=SensorData)
def get_data_by_user_id(user_id: int, db: Session = Depends(get_db)):
    data = crud.get_all_sensor_data_for_user_id(db, user_id)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data not found for user id \"{user_id}\"")
    return data

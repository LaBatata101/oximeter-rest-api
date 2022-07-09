from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from oximeter.api.dependencies import get_db
from oximeter.db import crud
from oximeter.schemas import SensorData, SensorDataCreate

route = APIRouter(prefix="/sensor", tags=["sensor"])


@route.post("/", response_model=SensorData, status_code=status.HTTP_201_CREATED)
def post_data(sensor_data: SensorDataCreate, db: Session = Depends(get_db)):
    return crud.create_sensor_data(db, sensor_data)


@route.get("/", response_model=list[SensorData])
def get_all_data(skip: int = Query(0, ge=0), limit: int = Query(100, ge=0), db: Session = Depends(get_db)):
    return crud.get_all_sensor_data(db, skip, limit)


@route.get("/last", response_model=SensorData)
def get_last_added_data(db: Session = Depends(get_db)):
    last_data = crud.get_last_row(db)
    if last_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Last added data not found. Database is probably empty!"
        )
    return last_data


@route.get("/date", response_model=list[SensorData])
def get_data_by_date(
    day: int | None = Query(None, ge=1, le=31),
    month: int | None = Query(None, ge=1, le=12),
    year: int | None = Query(None, ge=1, le=9999),
    db: Session = Depends(get_db),
):
    is_incorrect_date = day is not None and month is None and year is not None
    is_empty_date = day is None and month is None and year is None
    if is_incorrect_date and is_empty_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wasn't able to get data with current query parameter."
        )

    data = []
    if day is not None and month is not None and year is not None:
        data = crud.get_sensor_data_by_date_day(db, datetime(year=year, month=month, day=day))
    elif month is not None and year is not None:
        data = crud.get_sensor_data_by_date_month(db, datetime(year=year, month=month, day=1))
    elif year is not None:
        data = crud.get_sensor_data_by_date_year(db, datetime(year=year, month=1, day=1))

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found for date.")
    return data


@route.get("/{user_id}", response_model=SensorData)
def get_data_by_user_id(user_id: int, db: Session = Depends(get_db)):
    data = crud.get_all_sensor_data_for_user_id(db, user_id)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Data not found for user id "{user_id}"')
    return data

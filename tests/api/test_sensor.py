from datetime import datetime

from starlette.testclient import TestClient

from oximeter.schemas.sensor_data import SensorDataCreate


def test_post_sensor_data(client: TestClient):
    data = SensorDataCreate(user_id=0, bpm=88, spo2=99, date=datetime.now())

    d = data.dict()
    d["date"] = d["date"].strftime("%Y-%m-%dT%H:%M:%S")

    response = client.post(
        "/sensor/",
        json=d,
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 201


def test_get_sensor_data_by_day(client: TestClient):
    response = client.get("/sensor/date", params={"day": 6, "month": 7, "year": 2022})
    print(response.json())
    assert response.status_code == 200

from datetime import datetime

from starlette.testclient import TestClient

from oximeter.schemas.sensor_data import SensorDataCreate


def test_post_sensor_data(client: TestClient):
    data = SensorDataCreate(user_id=0, bpm=88, spo2=99, date=datetime.now())

    d = data.dict()
    d["date"] = d["date"].strftime("%Y-%m-%dT%H:%M:%S%Z")

    response = client.post(
        "/sensor/",
        json=d,
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 201

from fastapi import FastAPI

from oximeter.api.routes import sensor

app = FastAPI(title="Oximeter Sensor")

app.include_router(sensor.route)

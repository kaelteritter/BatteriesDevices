from fastapi import Depends, FastAPI

from backend.app import crud
from backend.app.database import get_db
from backend.app.schemas import DeviceReadSchema, DeviceCreateSchema


app = FastAPI()



@app.get("/devices/", response_model=list[DeviceReadSchema])
async def list_devices(session = Depends(get_db)):
    return await crud.read_devices(session)


@app.post("/devices/", response_model=DeviceReadSchema)
async def create_device(schema: DeviceCreateSchema, session = Depends(get_db)):
    return await crud.create_device(session, schema)
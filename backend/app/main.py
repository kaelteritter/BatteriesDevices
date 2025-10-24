from fastapi import Depends, FastAPI, HTTPException
from starlette import status

from backend.app import crud
from backend.app.database import get_db
from backend.app.schemas import (
    BatteryCreateSchema,
    DeviceReadSchema,
    DeviceCreateSchema,
    DeviceUpdateSchema,
    BatteryReadSchema,
    BatteryUpdateSchema,
)


app = FastAPI()


@app.get("/devices/", response_model=list[DeviceReadSchema])
async def list_devices(session=Depends(get_db)):
    return await crud.read_devices(session)


@app.post("/devices/", response_model=DeviceReadSchema)
async def create_device(schema: DeviceCreateSchema, session=Depends(get_db)):
    is_already_existed = await crud.read_device_by_name(session, schema.name)
    if is_already_existed:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Устройство с таким именем уже существует",
        )
    return await crud.create_device(session, schema)


@app.get("/devices/{device_id}/", response_model=DeviceReadSchema)
async def retrieve_device(device_id: int, session=Depends(get_db)):
    device = await crud.read_device(session, device_id)
    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого устройства не существует",
        )
    return device


@app.put("/devices/{device_id}/", response_model=DeviceReadSchema)
async def update_device(
    schema: DeviceUpdateSchema, device_id: int, session=Depends(get_db)
):
    return await crud.update_device(session, device_id, schema)


@app.delete("/devices/{device_id}/")
async def delete_device(device_id: int, session=Depends(get_db)):
    return await crud.delete_device(session, device_id)


@app.get("/batteries/", response_model=list[BatteryReadSchema])
async def list_batteries(session=Depends(get_db)):
    return await crud.read_batteries(session)


@app.post("/batteries/", response_model=BatteryReadSchema)
async def create_battery(schema: BatteryCreateSchema, session=Depends(get_db)):
    is_already_existed = await crud.read_battery_by_name(session, schema.name)
    if is_already_existed:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="АКБ с таким именем уже существует",
        )
    return await crud.create_battery(session, schema)


@app.get("/batteries/{battery_id}/", response_model=BatteryReadSchema)
async def retrieve_battery(battery_id: int, session=Depends(get_db)):
    battery = await crud.read_battery(session, battery_id)
    if not battery:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такого АКБ не существует",
        )
    return battery


@app.put("/batteries/{battery_id}/", response_model=BatteryReadSchema)
async def update_battery(schema: BatteryUpdateSchema, battery_id: int, session=Depends(get_db)):
    return await crud.update_battery(session, battery_id, schema)


@app.delete("/batteries/{battery_id}/")
async def delete_battery(battery_id: int, session=Depends(get_db)):
    return await crud.delete_battery(session, battery_id)



@app.put("/devices/{device_id}/batteries/{battery_id}/", response_model=DeviceReadSchema)
async def connect_battery_to_device(device_id: int, battery_id: int, session=Depends(get_db)):
    return await crud.update_device_batteries_list(session, device_id, battery_id)
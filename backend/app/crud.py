from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models import Battery, Device
from backend.app.schemas import BatteryCreateSchema, DeviceCreateSchema, DeviceUpdateSchema, BatteryUpdateSchema


async def create_device(session: AsyncSession, schema: DeviceCreateSchema):
    device = Device(**schema.model_dump())
    session.add(device)
    await session.commit()
    return device


async def read_device(session: AsyncSession, device_id: int):
    stmt = select(Device).where(Device.id == device_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def read_device_by_name(session: AsyncSession, device_name: str):
    stmt = select(Device).where(Device.name == device_name)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def read_devices(session: AsyncSession):
    stmt = select(Device)
    result = await session.execute(stmt)
    return result.scalars()


async def update_device(
    session: AsyncSession, device_id: int, schema: DeviceUpdateSchema
):
    device = await read_device(session, device_id)

    if not device:
        return None

    for key, value in schema.model_dump(exclude_unset=True).items():
        setattr(device, key, value)
    await session.commit()
    return device


async def delete_device(session: AsyncSession, device_id: int):
    device = await read_device(session, device_id)

    if not device:
        return False

    await session.delete(device)
    await session.commit()

    return True



async def create_battery(session: AsyncSession, schema: BatteryCreateSchema):
    battery = Battery(**schema.model_dump())
    session.add(battery)
    await session.commit()
    return battery


async def read_battery(session: AsyncSession, battery_id: int):
    stmt = select(Battery).where(Battery.id == battery_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def read_batteries(session: AsyncSession):
    stmt = select(Battery)
    result = await session.execute(stmt)
    return result.scalars()


async def read_battery_by_name(session: AsyncSession, battery_name: str):
    stmt = select(Battery).where(Battery.name == battery_name)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def update_battery(session: AsyncSession, battery_id: int, schema: BatteryUpdateSchema):
    battery = await read_battery(session, battery_id)

    if not battery:
        return None
    
    for key, value in schema.model_dump().items():
        setattr(battery, key, value)
    await session.commit()
    return battery


async def delete_battery(session: AsyncSession, battery_id: int):
    battery = await read_battery(session, battery_id)
    
    if not battery:
        return False
    
    await session.delete(battery)
    await session.commit()

    return True


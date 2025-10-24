from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models import Device
from backend.app.schemas import DeviceCreateSchema, DeviceUpdateSchema


async def create_device(session: AsyncSession, schema: DeviceCreateSchema):
    device = Device(**schema.model_dump())
    session.add(device)
    await session.commit()
    return device


async def read_device(session: AsyncSession, device_id: int):
    stmt = select(Device).where(Device.id == device_id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def update_device(session: AsyncSession, device_id: int, schema: DeviceUpdateSchema):
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
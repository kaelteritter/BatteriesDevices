from pydantic import BaseModel


class DeviceCreateSchema(BaseModel):
    name: str
    firmware: str
    is_on: bool


class DeviceUpdateSchema(BaseModel):
    name: str
    firmware: str
    is_on: bool
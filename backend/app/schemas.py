from pydantic import BaseModel


class BatteryReadSchema(BaseModel):
    id: int
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None = None 


class BatteryCreateSchema(BaseModel):
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None = None 


class BatteryUpdateSchema(BaseModel):
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None




class DeviceCreateSchema(BaseModel):
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float


class DeviceReadSchema(BaseModel):
    id: int
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float


class DeviceUpdateSchema(BaseModel):
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float



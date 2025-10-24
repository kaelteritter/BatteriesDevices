from pydantic import BaseModel







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
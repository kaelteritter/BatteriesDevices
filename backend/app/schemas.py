from pydantic import BaseModel, ConfigDict


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class BatteryReadSchema(CustomBaseModel):
    id: int
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None = None 


class BatteryCreateSchema(CustomBaseModel):
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None = None 


class BatteryUpdateSchema(CustomBaseModel):
    name: str
    firmare_version: str
    is_on: bool
    device_id: int | None




class DeviceCreateSchema(CustomBaseModel):
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float


class DeviceReadSchema(CustomBaseModel):
    id: int
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float
    batteries: list[BatteryReadSchema]


class DeviceUpdateSchema(CustomBaseModel):
    name: str
    nominal_voltage: float
    lifespan: int
    remaining_capacity: float



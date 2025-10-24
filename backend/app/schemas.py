from pydantic import BaseModel, ConfigDict


class CustomBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class BatteryReadSchema(CustomBaseModel):
    id: int
    name: str
    nominal_voltage: float
    remaining_capacity: float
    lifespan: int
    device_id: int | None = None


class BatteryCreateSchema(CustomBaseModel):
    name: str
    nominal_voltage: float
    remaining_capacity: float
    lifespan: int
    device_id: int | None = None


class BatteryUpdateSchema(CustomBaseModel):
    name: str
    nominal_voltage: float
    remaining_capacity: float
    lifespan: int
    device_id: int | None



class DeviceCreateSchema(CustomBaseModel):
    name: str
    firmware_version: str
    is_on: bool


class DeviceReadSchema(CustomBaseModel):
    id: int
    name: str
    firmware_version: str
    is_on: bool
    batteries: list[BatteryReadSchema]


class DeviceUpdateSchema(CustomBaseModel):
    name: str
    firmware_version: str
    is_on: bool



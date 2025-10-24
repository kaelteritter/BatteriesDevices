from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Device(Base):
    """
    lifespan: в месяцах
    remaining_capacity: в процентах
    """
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    nominal_voltage: Mapped[float] = mapped_column(nullable=False)
    lifespan: Mapped[int] = mapped_column(nullable=False)
    remaining_capacity: Mapped[float]

    batteries = relationship('Battery', back_populates='device')



class Battery(Base):
    __tablename__ = 'batteries'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    firmare_version: Mapped[str] = mapped_column(nullable=False)
    is_on: Mapped[bool] = mapped_column(default=False)

    device_id = mapped_column(ForeignKey("devices.id"), nullable=True)
    device = relationship(Device, back_populates="batteries")
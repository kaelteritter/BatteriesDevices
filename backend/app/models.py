from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Device(Base):
    __tablename__ = 'devices'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    firmware_version: Mapped[str] = mapped_column(nullable=False)
    is_on: Mapped[bool] = mapped_column(default=False)           

    batteries = relationship('Battery', back_populates='device')


class Battery(Base):
    __tablename__ = 'batteries'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    nominal_voltage: Mapped[float] = mapped_column(nullable=False)
    remaining_capacity: Mapped[float] = mapped_column(nullable=False)  # 0–100%
    lifespan: Mapped[int] = mapped_column(nullable=False)              # в месяцах

    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), nullable=True)
    device = relationship("Device", back_populates="batteries")
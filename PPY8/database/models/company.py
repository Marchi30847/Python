from __future__ import annotations

from sqlalchemy.orm import Mapped, relationship, mapped_column

from PPY8.database.data import Base


class Company(Base):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    address: Mapped[str]
    employees: Mapped[list["Employee"]] = relationship(back_populates="company", cascade="all", uselist=True)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List


class Base(DeclarativeBase):
    pass


class Weekend_Info(Base):
    __tablename__ = "weekend_info"

    RoundNumber: Mapped[int]
    Country: Mapped[str] = mapped_column(String())
    Location: Mapped[str] = mapped_column(String())
    OfficialEventName: Mapped[str] = mapped_column(String(), primary_key=True)
    EventDate: Mapped[int]
    EventName: Mapped[str] = mapped_column(String())
    EventFormat: Mapped[str] = mapped_column(String())
    Session1: Mapped[str] = mapped_column(String())
    Session1Date: Mapped[int]
    Session1DateUtc: Mapped[int]
    Session2: Mapped[str] = mapped_column(String())
    Session2Date: Mapped[int]
    Session2DateUtc: Mapped[int]
    Session3: Mapped[str] = mapped_column(String())
    Session3Date: Mapped[int]
    Session3DateUtc: Mapped[int]
    Session4: Mapped[str] = mapped_column(String())
    Session4Date: Mapped[int]
    Session4DateUtc: Mapped[int]
    Session5: Mapped[str] = mapped_column(String())
    Session5Date: Mapped[int]
    Session5DateUtc: Mapped[int]

    Results: Mapped[List["Race_Results"]] = relationship(back_populates="weekend")


class Race_Results(Base):
    __tablename__ = "race_results"

    DriverNumber: Mapped[int]
    Abbreviation: Mapped[str] = mapped_column(String())
    DriverId: Mapped[str] = mapped_column(String(), primary_key=True)
    TeamName: Mapped[str] = mapped_column(String())
    TeamColor: Mapped[str] = mapped_column(String())
    TeamId: Mapped[str] = mapped_column(String())
    FullName: Mapped[str] = mapped_column(String())
    CountryCode: Mapped[str] = mapped_column(String())
    Position: Mapped[float]
    ClassifiedPosition: Mapped[str] = mapped_column(String())
    GridPosition: Mapped[float]
    Time: Mapped[int]
    Status: Mapped[str] = mapped_column(String())
    Points: Mapped[str] = mapped_column(String())
    Laps: Mapped[float]
    Event: Mapped[str] = mapped_column(String(), primary_key=True)

    weekend_id: Mapped[str] = mapped_column(ForeignKey("Weekend_Info.OfficialEventName"))
    weekend: Mapped["Weekend_Info"] = relationship(back_populates="Results")

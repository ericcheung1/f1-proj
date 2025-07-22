from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String

engine = create_engine("sqlite://db/f1-test.db", echo=True)

class Base(DeclarativeBase):
    pass

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
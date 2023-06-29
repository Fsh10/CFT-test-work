from sqlalchemy import Table, Column, Integer, String, MetaData, Date

from src.database import Base

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", String, primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("salary", Integer, nullable=False),
    Column("promotion_date", Date, nullable=False),
)


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    salary = Column(Integer)
    promotion_date = Column(Date)

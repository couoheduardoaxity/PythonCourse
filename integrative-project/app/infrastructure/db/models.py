from sqlalchemy import Column, DateTime, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True)
    customer_id = Column(String)
    total = Column(Float)
    created_at = Column(DateTime)

from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .card import Card

class CardType(Base):
    __tablename__="card_type"

    type_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    type_name:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    description:Mapped[str|None]=mapped_column(String,nullable=True)

    cards:Mapped[list["Card"]]=relationship(back_populates="card_type")
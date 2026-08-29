from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .account import Account

class AccountType(Base):
    __tablename__="account_type"

    type_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    type_name:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    minimum_balance:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False,default=0)
    interest_rate:Mapped[Decimal]=mapped_column(Numeric(5,2),nullable=False)
    description:Mapped[str|None]=mapped_column(String,nullable=True)

    __table_args__=(
        CheckConstraint("minimum_balance >=0",name="account_type_minimum_balance_check"),
        CheckConstraint("interest_rate>=0",name="account_type_interest_rate_check")
    )

    accounts:Mapped[list["Account"]]=relationship(back_populates="account_type")
from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .card_type import CardType
    from .customer import Customer
    from .account import Account

class Card(Base):
    __tablename__="card"
    card_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    card_number:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    account_id:Mapped[int]=mapped_column(Integer,ForeignKey("account.account_id"),nullable=False)
    card_type_id:Mapped[int]=mapped_column(Integer,ForeignKey("card_type.type_id"),nullable=False)
    issued_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    expiry_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=True)
    status:Mapped[str]=mapped_column(String,nullable=False,default="ACTIVE")

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','BLOCKED','EXPIRED','CANCELLED')",name="card_status_check"),
    )

    card_type:Mapped["CardType"]=relationship(back_populates="cards")
    customer:Mapped["Customer"]=relationship(back_populates="cards")
    account:Mapped["Account"]=relationship(back_populates="cards")
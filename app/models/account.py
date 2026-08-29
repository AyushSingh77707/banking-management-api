from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import Customer
    from .account_type import AccountType
    from .card import Card
    
class Account(Base):
    __tablename__="account"

    account_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    account_number:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    branch_id:Mapped[int]=mapped_column(Integer,ForeignKey("branch.branch_id"),nullable=False)
    account_type_id:Mapped[int]=mapped_column(Integer,ForeignKey("account_type.type_id"),nullable=False)
    balance:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    status:Mapped[str]=mapped_column(String,default='ACTIVE',nullable=False)
    opened_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),server_default=func.now(),nullable=False)
    closed_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=True)

    customer:Mapped["Customer"]=relationship(back_populates="accounts")

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','CLOSED','BLOCKED')",name="account_status_check"),
        CheckConstraint("balance >=0",name="account_balance_check")
    )

    account_type:Mapped["AccountType"]=relationship(back_populates="accounts")
    cards:Mapped["Card"]=relationship(back_populates="account")
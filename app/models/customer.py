from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .account import Account
    from .loan import Loan
    from .beneficiary import Beneficiary
    from .kyc import Kyc
    from .card import Card
    from .support_ticket import SupportTicket
    from .customer_address import CustomerAddress

class Customer(Base):
    __tablename__='customer'

    customer_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    full_name:Mapped[str]=mapped_column(String,nullable=False)
    date_of_birth:Mapped[date]=mapped_column(Date,nullable=False)
    gender:Mapped[str | None ]=mapped_column(String)
    mobile:Mapped[str]=mapped_column(String,nullable=False,unique=True)
    email:Mapped[str | None]=mapped_column(String,unique=True)
    occupation:Mapped[str|None]=mapped_column(String)
    status:Mapped[str]=mapped_column(String,nullable=False,default='ACTIVE')
    created_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())

    accounts:Mapped[list["Account"]]=relationship(back_populates="customer")
    loans:Mapped[list["Loan"]]=relationship(back_populates="customer")
    kyc:Mapped["Kyc | None"]=relationship(back_populates="customer",uselist=False)
    beneficiaries:Mapped[list["Beneficiary"]]=relationship(back_populates="customer")
    cards:Mapped[list["Card"]]=relationship(back_populates="customer")
    tickets:Mapped[list["SupportTicket"]]=relationship(back_populates="customer")
    addresses:Mapped[list["CustomerAddress"]]=relationship(back_populates="customer")

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','FROZEN','BLOCKED','INACTIVE')",name="customer_status_check"),
    )






from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import Customer


class Beneficiary(Base):
    __tablename__="beneficiary"

    beneficiary_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    beneficiary_name:Mapped[str]=mapped_column(String,nullable=False)
    account_number:Mapped[str]=mapped_column(String,nullable=False)
    ifsc_code:Mapped[str]=mapped_column(String,nullable=False)
    nickname:Mapped[str|None]=mapped_column(String,nullable=True)
    status:Mapped[str]=mapped_column(String,nullable=False,server_default='ACTIVE')
    created_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','BLOCKED')",name="beneficiary_status_check"),
    )

    customer:Mapped["Customer"]=relationship(back_populates="beneficaries")
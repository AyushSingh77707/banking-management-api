from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import Customer

class Kyc(Base):
    __tablename__="kyc"

    kyc_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),unique=True,nullable=False)
    document_type:Mapped[str]=mapped_column(String,nullable=False)
    document_number:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    kyc_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    kyc_status:Mapped[str]=mapped_column(String,server_default='VERIFIED',nullable=False)
    verification_method:Mapped[str]=mapped_column(String,nullable=False)

    __table_args__=(
        CheckConstraint("kyc_status IN ('VERIFIED','REJECTED','EXPIRED','PENDING')",name="kyc_status_check"),
    )

    customer:Mapped["Customer"]=relationship(back_populates="kyc")


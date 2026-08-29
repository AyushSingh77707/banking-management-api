from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import  Customer

class CustomerAddress(Base):
    __tablename__="customer_address"

    address_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    type_of_address:Mapped[str]=mapped_column(String,nullable=False)
    address_line:Mapped[str]=mapped_column(String,nullable=False)
    city:Mapped[str]=mapped_column(String,nullable=False)
    state:Mapped[str]=mapped_column(String,nullable=False)
    pincode:Mapped[str]=mapped_column(String,nullable=False)


    customer:Mapped["Customer"]=relationship(back_populates="addresses")
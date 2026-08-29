from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .account import Account
    from .employee import Employee
    from .loan import Loan

class Branch(Base):
    __tablename__="branch"

    branch_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    branch_name:Mapped[str]=mapped_column(String,nullable=False)
    ifsc_code:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    address:Mapped[str]=mapped_column(String,nullable=False)
    city:Mapped[str]=mapped_column(String,nullable=False)
    state:Mapped[str]=mapped_column(String,nullable=False)
    contact_no:Mapped[str]=mapped_column(String,nullable=False)

    accounts:Mapped[list["Account"]]=relationship(back_populates="branch")
    employees:Mapped[list["Employee"]]=relationship(back_populates="branch")
    loans:Mapped[list["Loan"]]=relationship(back_populates="branch")
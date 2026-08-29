from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .branch import Branch
    from .loan import Loan

class Employee(Base):
    __tablename__="employee"

    employee_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    employee_name:Mapped[str]=mapped_column(String,nullable=False)
    employee_role:Mapped[str]=mapped_column(String,nullable=False)
    employee_mobile:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    employee_email:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    employee_status:Mapped[str]=mapped_column(String,nullable=False,default='ACTIVE')
    branch_id:Mapped[int]=mapped_column(Integer,ForeignKey("branch.branch_id"),nullable=False)
    joining_date:Mapped[date]=mapped_column(Date,server_default=func.now(),nullable=True)

    branch:Mapped["Branch"]=relationship(back_populates="employees")
    issued_loan:Mapped[list["Loan"]]=relationship(back_populates="issued_by")

    __table_args__=(
            CheckConstraint("employee_status IN ('ACTIVE','ONLEAVE','RESIGNED')",name="employee_status_check"),
        )
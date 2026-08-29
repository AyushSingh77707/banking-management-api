from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import Customer
    from .employee import Employee
    from .branch import Branch
    from .loan_payment import LoanPayment
    from .loan_collateral import LoanCollateral

class Loan(Base):
    __tablename__="loan"

    loan_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    branch_id:Mapped[int]=mapped_column(Integer,ForeignKey("branch.branch_id"),nullable=False)
    loan_type:Mapped[str]=mapped_column(String,nullable=False)
    loan_issued_by_emp_id:Mapped[int]=mapped_column(Integer,ForeignKey("employee.employee_id"),nullable=False)
    principal_amount:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    interest_rate:Mapped[Decimal]=mapped_column(Numeric(5,2),nullable=False)
    start_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    end_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True))
    status:Mapped[str]=mapped_column(String,nullable=False,server_default='ACTIVE')

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','PAID','CLOSED','DEFAULTED')",name="loan_status_check"),
        CheckConstraint("principal_amount>=0",name="loan_principal_amount_check"),
        CheckConstraint("interest_rate>=0",name="loan_interest_rate_check")
    )

    customer:Mapped["Customer"]=relationship(back_populates="loans")
    branch:Mapped["Branch"]=relationship(back_populates="loans")
    issued_by:Mapped["Employee"]=relationship(back_populates="issued_loans")
    payments:Mapped[list["LoanPayment"]]=relationship(back_populates="loan")
    collaterals:Mapped[list["LoanCollateral"]]=relationship(back_populates="loan")


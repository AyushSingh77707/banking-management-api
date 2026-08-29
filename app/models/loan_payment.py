from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .loan import Loan

class LoanPayment(Base):
    __tablename__="loan_payment"

    payment_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    loan_id:Mapped[int]=mapped_column(Integer,ForeignKey("loan.loan_id"),nullable=False)
    payment_amount:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    payment_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    due_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=True)
    remaining_balance:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    payment_status:Mapped[str]=mapped_column(String,nullable=False,default="PENDING")

    __table_args__=(
        CheckConstraint("payment_status IN ('PENDING','PAID','OVERDUE')",name="loan_payment_status_check"),
        CheckConstraint("remaining_balance >=0",name="remaining_balance_status_check")
    )

    loan:Mapped["Loan"]=relationship(back_populates="payments")
    
from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .loan import Loan

class LoanCollateral(Base):
    __tablename__="loan_collateral"

    collateral_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    loan_id:Mapped[int]=mapped_column(Integer,ForeignKey("loan.loan_id"),nullable=False)
    collateral_type:Mapped[str]=mapped_column(String,nullable=False)
    description:Mapped[str]=mapped_column(String)
    estimated_value:Mapped[Decimal]=mapped_column(Numeric,nullable=False)
    status:Mapped[str]=mapped_column(String,nullable=False,default="ACTIVE")

    __table_args__=(
        CheckConstraint("status IN ('ACTIVE','RELEASED','LIQUIDATED')",name="loan_collateral_status_check"),
        CheckConstraint("estimated_val0ue >0",name="loan_collateral_estimated_value_check")
    )

    loan:Mapped["Loan"]=relationship(back_populates="collaterals")



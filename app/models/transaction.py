from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .transaction_entry import TransactionEntry

class Transaction(Base):
    __tablename__="transaction"

    transaction_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    transaction_type:Mapped[str]=mapped_column(String,nullable=False)
    amount:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    transaction_date:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    status:Mapped[str]=mapped_column(String,nullable=False,default="SUCCESS")
    reference_no:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    description:Mapped[str|NotImplementedError]=mapped_column(String,nullable=True)

    __table_args__=(
        CheckConstraint("status IN ('SUCCESS','FAILED','PENDING')",name="transaction_status_check"),
        CheckConstraint("amount >0",name="transaction_amount_check"),
        CheckConstraint("transaction_type IN ('TRANSER','DEPOSIT','WITHDRAWAL','PAYMENT')")
    )

    entries:Mapped[list["TransactionEntry"]]=relationship(back_populates="transaction")
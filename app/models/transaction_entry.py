from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .transaction import Transaction

class TransactionEntry(Base):
    __tablename__="transaction_entry"

    entry_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    transaction_id:Mapped[int]=mapped_column(Integer,ForeignKey("transaction.transaction_id"),nullable=False)
    account_id:Mapped[int]=mapped_column(Integer,ForeignKey("account.account_id"),nullable=False)
    entry_type:Mapped[str]=mapped_column(String,nullable=False)
    amount:Mapped[Decimal]=mapped_column(Numeric(15,2),nullable=False)
    created_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())

    __table_args__=(
        CheckConstraint("amount >0",name="transaction_entry_amount_check"),
        CheckConstraint("entry_type IN ('CREDIT','DEBIT')")
    )

    transaction:Mapped["Transaction"]=relationship(back_populates="entries")


from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .customer import Customer

class SupportTicket(Base):
    __tablename__="support_ticket"

    ticket_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    customer_id:Mapped[int]=mapped_column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    ticket_type:Mapped[str]=mapped_column(String,nullable=False)
    subject:Mapped[str]=mapped_column(String,nullable=True)
    description:Mapped[str]=mapped_column(String,nullable=True)
    priority:Mapped[str]=mapped_column(String,nullable=False,default="MEDIUM")
    status:Mapped[str]=mapped_column(String,nullable=False,default="FALSE")
    created_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())
    resolved_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=True)

    __table_args__=(
        CheckConstraint("priority IN ('LOW','HIGH','URGENT','MEDIUM')",name="support_ticket_priority_check"),
        CheckConstraint("status IN ('OPEN','IN_PROGRESS','RESOLVED','CLOSED')",name="support_ticket_status_check")
    )

    customer:Mapped["Customer"]=relationship(back_populates="tickets")
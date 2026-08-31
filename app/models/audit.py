from app.core.database import Base
from sqlalchemy import String,Date,TIMESTAMP,func,CheckConstraint,Integer,ForeignKey,Numeric
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column,Mapped,relationship
from datetime import date,time,datetime
from decimal import Decimal


class AuditLog(Base):
    __tablename__="audit_log"

    audit_id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    table_name:Mapped[str]=mapped_column(String,nullable=False)
    record_id:Mapped[int]=mapped_column(Integer,nullable=False)
    operation:Mapped[str]=mapped_column(String,nullable=False)
    old_value:Mapped[dict|None]=mapped_column(JSONB)
    new_value:Mapped[dict|None]=mapped_column(JSONB)
    changed_by:Mapped[str|None]=mapped_column(String)
    changed_at:Mapped[datetime]=mapped_column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())

    __table_args__=(
        CheckConstraint("operation IN ('INSERT','UPDATE','DELETE')",name="audit_log_operation_check"),
    )
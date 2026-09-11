from pydantic import BaseModel,Field
from decimal import Decimal
from typing import Literal
from datetime import datetime

class AccountCreate(BaseModel):
    customer_id:int
    branch_id:int
    account_type_id:int
    balance:Decimal

class AccountUpdate(BaseModel):
    status:Literal["ACTIVE","CLOSED","BLOCKED"] | None =None

class AccountResponse(BaseModel):
    account_id:int
    account_number:str
    customer_id:int
    branch_id:int
    account_type_id:int
    balance:Decimal
    status:str
    opened_at:datetime

class AccountDeposit(BaseModel):
    account_id:int
    amount:Decimal=Field(gt=0)

class AccountWithdraw(AccountDeposit):
    pass

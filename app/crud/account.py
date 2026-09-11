from app.schemas.account import AccountCreate,AccountDeposit,AccountWithdraw
from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.models.account import Account
from app.models.branch import Branch
from app.models.account_type import AccountType
from fastapi import HTTPException
import random
from decimal import Decimal
from fastapi.responses import JSONResponse
from app.core.exception import CustomerNotFoundException

def account_create(db:Session,data:AccountCreate):
    c=db.get(Customer,data.customer_id)
    if not c:
        raise CustomerNotFoundException

    b=db.get(Branch,data.branch_id)
    if not b:
        raise HTTPException(status_code=404,detail="branch not found")

    acc_type=db.get(AccountType,data.account_type_id)
    if not acc_type:
        raise HTTPException(status_code=404,detail="account type not found")

    if data.balance < acc_type.minimum_balance:
        raise HTTPException(status_code=400,detail="min balance is not satisfied!")

    account=Account(
        **data.model_dump(),account_number=str(random.randint(1000000000,9000000000))
    )


    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def deposit_amount(db:Session,data:AccountDeposit):
    acc=db.get(Account,data.account_id)
    if not acc:
        raise HTTPException(status_code=404,detail="Account not found")

    acc.balance+=data.amount

    db.commit()
    db.refresh(acc)
    return JSONResponse(status_code=201,content="Amount deposited successfully")

def with_amount(db:Session,data:AccountWithdraw):
    acc=db.get(Account,data.account_id)
    if not acc:
        raise HTTPException(status_code=404,detail="account not found")

    if data.amount>acc.balance:
        raise HTTPException(status_code=400,detail="insufficient balance in account")

    acc.balance-=data.amount
    db.commit()
    db.refresh(acc)
    return JSONResponse(status_code=201,content="Amount withdrawal successfull")
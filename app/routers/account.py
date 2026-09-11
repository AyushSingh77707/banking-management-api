from fastapi import APIRouter,Depends,HTTPException,status,Path
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.account import AccountResponse,AccountCreate,AccountDeposit,AccountWithdraw
from app.crud.account import account_create,deposit_amount,with_amount
from decimal import Decimal


router=APIRouter(prefix="/accounts",tags=["Account"])

@router.post("/",response_model=AccountResponse,status_code=status.HTTP_201_CREATED)
def create_account(account_detail:AccountCreate,db:Session=Depends(get_db)):
    return account_create(db=db,data=account_detail)


@router.post("/{account_id}/deposit")
def deposit_money(data:AccountDeposit,
                  db:Session=Depends(get_db)):
    return deposit_amount(db=db,data=data)

@router.post("/{account_id}/withdraw")
def withdraw_money(data:AccountWithdraw,
                  db:Session=Depends(get_db)):
    return with_amount(db=db,data=data)




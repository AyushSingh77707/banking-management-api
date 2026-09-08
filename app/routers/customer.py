from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session 
from app.core.database import get_db
from app.crud.customer import create_customer,get_customer,get_all_customers,update_customer,delete_customer
from app.schemas.customer import CustomerCreate,CustomerResponse,CustomerUpdate


router=APIRouter(prefix="/customers",tags=["Customer"])


@router.post("/",response_model=CustomerResponse,status_code=status.HTTP_201_CREATED)
def customer_create_endpoint(data:CustomerCreate,db:Session=Depends(get_db)):
    return create_customer(customer=data,db=db)

@router.get("/",response_model=list[CustomerResponse])
def get_customers(db:Session=Depends(get_db)):
    return get_all_customers(db)

@router.get("/{id}",response_model=CustomerResponse)
def get_customer_by_id(id:int,db:Session=Depends(get_db)):

    c=get_customer(cust_id=id,db=db)

    if not c:
        raise HTTPException(status_code=404,detail="Customer with customer id {id} not found!")

    return c

@router.patch("/{id}",response_model=CustomerResponse)
def patch_customer(id:int,info:CustomerUpdate,db:Session=Depends(get_db)):
    return update_customer(cust_id=id,data=info,db=db)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_customer(id:int,db:Session=Depends(get_db)):
    return delete_customer(cust_id=id,db=db)


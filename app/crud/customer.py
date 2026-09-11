from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate,CustomerUpdate
from app.schemas.filter import CustomerQueryParameter
from app.core.database import get_db
from fastapi import HTTPException,status
from sqlalchemy import select,or_,asc,desc
from app.core.exception import CustomerNotFoundException
from fastapi.responses import JSONResponse

def create_customer(customer:CustomerCreate,db:Session):
    db_cust=Customer(**customer.model_dump())

    db.add(db_cust)
    db.commit()
    db.refresh(db_cust)
    return db_cust



def get_customer(cust_id:int , db:Session):
    return db.scalar(
        select(Customer).where(Customer.customer_id==cust_id)
    )

def get_all_customers(db:Session,parameters:CustomerQueryParameter):

    query=select(Customer)

    if parameters.search:
        query=query.where(
            or_(Customer.full_name.ilike(f"%{parameters.search}%"),
                Customer.mobile.ilike(f"%{parameters.search}%"))
        )

    if parameters.status:
        query=query.where(Customer.status==parameters.status)

    sort_column=Customer.full_name if parameters.sort_by=="full_name" else Customer.created_at

    query=query.order_by(
        desc(sort_column) if parameters.order=="desc" else asc(sort_column)
    )

    query=query.limit(parameters.limit).offset(parameters.offset)
    return db.scalars(query).all()





def update_customer(cust_id:int,data:CustomerUpdate,db:Session):
    c=db.scalar(select(Customer).where(Customer.customer_id==cust_id))
    if not c:
        raise CustomerNotFoundException(cust_id)

    update_data=data.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(c,key,value)

    db.commit()
    db.refresh(c)
    return c

def delete_customer(cust_id:int,db:Session):
    c=db.scalar(select(Customer).where(Customer.customer_id==cust_id))

    if not c:
        raise CustomerNotFoundException(cust_id)

    if c.accounts:
        raise HTTPException(status_code=400,detail="customer has active account,cannot delete")

    db.delete(c)
    db.commit()
    


    
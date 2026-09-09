from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate,CustomerUpdate
from app.core.database import get_db
from fastapi import HTTPException,status
from sqlalchemy import select

def create_customer(customer:CustomerCreate,db:Session):
    db_cust=Customer(**customer.model_dump())

    try:
        db.add(db_cust)
        db.commit()
        db.refresh(db_cust)
        return db_cust

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="Customer with same mobile or email exists!")


def get_customer(cust_id:int , db:Session):
    return db.scalar(
        select(Customer).where(Customer.customer_id==cust_id)
    )

def get_all_customers(db:Session,limit:int=10,offset:int=0):
    query=select(Customer).limit(limit).offset(offset)
    return db.scalars(query).all()

def update_customer(cust_id:int,data:CustomerUpdate,db:Session):
    c=db.scalar(select(Customer).where(Customer.customer_id==cust_id))
    if not c:
        raise HTTPException(status_code=404,detail="Customer with id {cust_id} not found!")

    update_data=data.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(c,key,value)

    db.commit()
    db.refresh(c)
    return c

def delete_customer(cust_id:int,db:Session):
    c=db.scalar(select(Customer).where(Customer.customer_id==cust_id))

    if not c:
        raise HTTPException(status_code=404,detail="Customer not found")

    if c.accounts:
        raise HTTPException(status_code=400,detail="customer has active account,cannot delete")

    db.delete(c)
    db.commit()
    


    
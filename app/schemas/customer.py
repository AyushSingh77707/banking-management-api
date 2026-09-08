from pydantic import BaseModel,Field,EmailStr,ConfigDict,field_validator
from datetime import date,datetime
from typing import Annotated,Literal

FullName=Annotated[str,Field(min_length=3,max_length=100,examples=["Rahul Kumar"])]
MobileNumber=Annotated[str,Field(min_length=10,max_length=10,examples=["1234567890"],pattern=r"^[6-9]\d{9}$")]

class CustomerBase(BaseModel):
    full_name:FullName
    date_of_birth:date
    gender:Literal["MALE","FEMALE","OTHER"]=None
    mobile:MobileNumber
    email:EmailStr|None=None
    occupation:str|None=None

    @field_validator("full_name")
    @classmethod
    def validate_name(cls,data:str):
        return data.title()
    
    @field_validator("date_of_birth")
    @classmethod
    def validate_dob(cls,data:date):
        if data > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return data
    
    @field_validator("mobile")
    @classmethod
    def validate_mobile(cls,data:str):
        return data.strip()

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    full_name:FullName|None =None
    mobile:MobileNumber|None =None
    email:EmailStr|None =None
    occupation:str|None =None

class CustomerResponse(CustomerBase):
    customer_id:int
    status:str
    created_at:datetime

    model_config=ConfigDict(from_attributes=True)

    
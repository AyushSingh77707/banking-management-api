from fastapi import HTTPException

class CustomerNotFoundException(HTTPException):
    def __init__(self,customer_id:int):
        super().__init__(
            status_code=404,
            detail=f"Customer with id {customer_id} not found"
        )
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from app.core.config import settings
from app.routers.customer import router as customer_router




app=FastAPI(title=settings.API_TITLE)

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request:Request,exc:IntegrityError):
    return JSONResponse(status_code=409,content={"detail":"duplicate or invalid database data"})

app.include_router(customer_router)
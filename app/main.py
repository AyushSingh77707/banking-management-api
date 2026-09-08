from fastapi import FastAPI
from app.core.config import settings
from app.routers.customer import router as customer_router


app=FastAPI(title=settings.API_TITLE)
app.include_router(customer_router)
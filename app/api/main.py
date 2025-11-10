# app/api/main.py
from fastapi import APIRouter
from app.api.routes.users import router as users_router  # ← Must be this

api_router = APIRouter()
api_router.include_router(users_router, prefix="/users", tags=["users"])
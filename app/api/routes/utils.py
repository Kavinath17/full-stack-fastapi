# login.py
from fastapi import APIRouter
router = APIRouter()
@router.get("/test")
def test_login():
    return {"message": "Login route works"}

# items.py
from fastapi import APIRouter
router = APIRouter()
@router.get("/test")
def test_items():
    return {"message": "Items route works"}

# utils.py
from fastapi import APIRouter
router = APIRouter()
@router.get("/test")
def test_utils():
    return {"message": "Utils route works"}

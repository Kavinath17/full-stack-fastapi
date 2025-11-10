from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@app.post("/api/v1/users/signup")
def signup(user: UserCreate):
    print("✅ Request reached /api/v1/users/signup")  # Add this
    try:
        print(f"DEBUG: User = {user}")
        print(f"DEBUG: Password length = {len(user.password)}")
        return {"message": "IT WORKS!", "email": user.email}
    except Exception as e:
        print(f"🔥 ERROR in signup route: {e}")
        raise HTTPException(status_code=500, detail=str(e))

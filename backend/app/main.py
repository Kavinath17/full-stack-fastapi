import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings


# ------------------------------
# Custom Route ID Generator
# ------------------------------
def custom_generate_unique_id(route: APIRoute) -> str:
    """
    Generates a unique ID for each route based on its first tag and name.
    Helps OpenAPI avoid duplicate operation IDs.
    """
    return f"{route.tags[0]}-{route.name}"


# ------------------------------
# Initialize Sentry (optional)
# ------------------------------
if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)


# ------------------------------
# Create FastAPI App
# ------------------------------
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


# ------------------------------
# CORS Configuration
# ------------------------------
# Allow frontend + localhost for testing.
# In production, restrict origins to your frontend URL(s).
allowed_origins = [
    "http://54.226.141.154",       # EC2 frontend
    "http://54.226.141.154:5173",  # Vite dev (if used)
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






# ------------------------------
# Include API Routes
# ------------------------------
app.include_router(api_router, prefix=settings.API_V1_STR)


from backend.constants import naming
from backend.database.session import engine
from backend.dependencies.database import init_db
from backend.dependencies.rate_limiting import limiter
from backend.exceptions.database import DATABASE_UNAVAILABLE_EXCEPTION
from backend.routers.messages import router as messages_router
from backend.routers.certificates import router as certificates_router
from backend.routers.projects import router as projects_router
from backend.routers.experiences import router as experiences_router
from backend.routers.auth import router as auth_router
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlalchemy import text
from typing import Dict

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title=naming.PROJECT_TITLE,
    description=naming.PROJECT_DESCRIPTION,
    version=naming.PROJECT_VERSION,
    lifespan=lifespan,
    redoc_url=None
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://yashantportfolio.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/", response_model=Dict[str, str], tags=["Public Routes"])
@limiter.limit("5/minute")
async def root(request: Request) -> Dict[str, str]:
    return {"detail": f"{naming.PROJECT_TITLE} running..."}

@app.get("/health", response_model=Dict[str, str], tags=["Public Routes"])
@app.head("/health", response_model=None, tags=["Public Routes"])
@limiter.limit("5/minute")
async def health(request: Request) -> Dict[str, str]:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        raise DATABASE_UNAVAILABLE_EXCEPTION
    return {"detail": "healthy"}

app.include_router(messages_router, prefix=naming.MAIN_API_PREFIX)
app.include_router(projects_router, prefix=naming.MAIN_API_PREFIX)
app.include_router(experiences_router, prefix=naming.MAIN_API_PREFIX)
app.include_router(certificates_router, prefix=naming.MAIN_API_PREFIX)
app.include_router(auth_router, prefix=naming.MAIN_API_PREFIX)

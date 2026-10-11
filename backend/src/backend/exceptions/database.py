
from fastapi import HTTPException, status

DATABASE_UNAVAILABLE_EXCEPTION = HTTPException(
    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    detail="Database is currently unavailable"
)

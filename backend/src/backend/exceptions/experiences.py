
from fastapi import HTTPException, status

CANNOT_FIND_EXPERIENCE_BY_ID_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Cannot find any experience with the provided ID"
)

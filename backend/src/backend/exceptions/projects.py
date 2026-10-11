
from fastapi import HTTPException, status

PROJECT_WITH_TITLE_ALREADY_EXISTS_EXCEPTION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Project with the provided title already exists"
)

CANNOT_FIND_PROJECT_BY_ID_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Project with the provided ID not found"
)

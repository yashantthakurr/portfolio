
from fastapi import HTTPException, status

CERTIFICATE_WITH_NAME_ALREADY_EXISTS_EXCEPTION = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Certificate with the provided name already exists"
)

CANNOT_FIND_CERTIFICATE_BY_ID_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Certificate with the provided ID not found"
)
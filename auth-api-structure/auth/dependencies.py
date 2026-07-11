# auth/dependencies.py
# Reusable dependency to protect routes - extracts and validates the current user from a JWT

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.security import decode_access_token, is_token_blacklisted
from auth.service import get_user_by_username

# tells FastAPI/Swagger where the login endpoint lives, powers the "Authorize" button in /docs
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Dependency used on protected routes.
    Validates the JWT, checks blacklist, and returns the current user record.
    Raises 401 if anything is invalid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been logged out. Please login again.",
        )

    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    username: str | None = payload.get("sub")
    if username is None:
        raise credentials_exception

    user = get_user_by_username(username)
    if user is None:
        raise credentials_exception

    return user
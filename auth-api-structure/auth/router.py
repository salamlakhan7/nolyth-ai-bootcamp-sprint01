# auth/router.py
# Authentication routes: register, login, logout

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth.schemas import UserRegister, UserOut, Token
from auth.service import register_user, authenticate_user
from auth.security import create_access_token, blacklist_token
from auth.dependencies import oauth2_scheme

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister):
    """Register a new user account."""
    try:
        new_user = register_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return new_user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login with username/password (OAuth2 standard form fields).
    Returns a JWT access token on success.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    """Logout by blacklisting the current token."""
    blacklist_token(token)
    return {"message": "Successfully logged out."}
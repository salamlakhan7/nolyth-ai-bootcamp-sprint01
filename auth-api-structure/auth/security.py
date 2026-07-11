# auth/security.py
# Core security utilities: password hashing and JWT token creation/verification

from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext

# ----- Config -----
# In a real production app, SECRET_KEY comes from an environment variable (.env),
# never hardcoded. Kept as a constant here since this is a training sprint project.
SECRET_KEY = "sprint01-dev-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ----- Password hashing context (bcrypt, same family Django uses) -----
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Hash a plain-text password before storing it."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plain-text password against its stored hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a signed JWT containing the given data (typically {'sub': username}),
    with an expiry timestamp embedded in the payload.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict | None:
    """
    Decode and verify a JWT. Returns the payload if valid,
    or None if invalid/expired/tampered.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


# ----- Logout support (stateless JWT can't be revoked server-side by default) -----
# Simple in-memory blacklist - same concept as Django's token blacklist app,
# simplified since we have no persistent storage yet (arrives Days 11-12).
blacklisted_tokens: set[str] = set()


def blacklist_token(token: str) -> None:
    """Add a token to the blacklist (called on logout)."""
    blacklisted_tokens.add(token)


def is_token_blacklisted(token: str) -> bool:
    """Check if a token has been blacklisted (logged out)."""
    return token in blacklisted_tokens
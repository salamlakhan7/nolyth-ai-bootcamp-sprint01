# auth/service.py
# Business logic layer: user registration and authentication
# (in-memory storage for now - persistent DB arrives Days 11-12)

from auth.security import hash_password, verify_password
from auth.schemas import UserRegister

# ----- In-memory "database" -----
users_db: dict[str, dict] = {}   # keyed by username
user_id_counter = 0


def get_user_by_username(username: str) -> dict | None:
    """Fetch a stored user record by username."""
    return users_db.get(username)


def register_user(user_data: UserRegister) -> dict:
    """
    Register a new user: checks for duplicates, hashes password, stores record.
    Raises ValueError if username already exists (handled as HTTP error in router).
    """
    global user_id_counter

    if get_user_by_username(user_data.username):
        raise ValueError("Username already registered.")

    user_id_counter += 1
    new_user = {
        "id": user_id_counter,
        "username": user_data.username,
        "email": user_data.email,
        "hashed_password": hash_password(user_data.password),
    }
    users_db[user_data.username] = new_user
    return new_user


def authenticate_user(username: str, password: str) -> dict | None:
    """
    Verify username/password combination.
    Returns the user record if valid, None if invalid.
    """
    user = get_user_by_username(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user
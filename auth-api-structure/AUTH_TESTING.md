# Auth & API Structure Testing - Sprint 01 (Days 8-10)

This document covers the authentication implementation: JWT-based login, protected routes,
organized routers/services/schemas structure, and error handling.

All flows were tested live using FastAPI's Swagger UI (`/docs`).

---

## Project Structure

    auth-api-structure/
    ├── main.py                 (app instance, includes routers)
    ├── auth/
    │   ├── schemas.py           (UserRegister, UserLogin, UserOut, Token, TokenData)
    │   ├── security.py          (password hashing, JWT create/decode, blacklist)
    │   ├── service.py           (register_user, authenticate_user)
    │   ├── dependencies.py      (get_current_user - protects routes)
    │   └── router.py            (/auth/register, /auth/login, /auth/logout)
    ├── tasks/
    │   ├── schemas.py           (NewTask, TaskOut - now owner-aware)
    │   ├── service.py           (task CRUD, scoped per user)
    │   └── router.py            (/tasks routes, all protected)

Routes stay thin (just call services). Services hold logic. Schemas define shape.
This separation is what "organized FastAPI project structure" means in the sprint brief.

---

## Auth Flow Implemented

| Step    | Endpoint                            |                            Purpose                |
|------   |------------------------------------ |-------------------------------------------------- |
| 1       | `POST /auth/register`               | Create a new user (password hashed with bcrypt)   |
| 2       | `POST /auth/login`                  | Verify credentials, return JWT access token       |
| 3       | `POST /tasks` and other task routes | Require valid JWT via `Depends(get_current_user)` |
| 4       | `POST /auth/logout`                 | Blacklist the current token                       |

---

## 1. Register

Creates a new user account. Password is hashed with bcrypt before storage - never stored
or returned in plain text.

**Request body:**

```
{
  "username": "abdulhaq",
  "email": "abdultest@example.com",
  "password": "test1234"
}
```

Returns `201 Created` with user data (no password/hash included in response).

![Register](Screenshots/1%20register.JPG)

---

## 2. Login

Standard OAuth2 password flow - credentials sent as form-data (`username`, `password`),
not JSON, per OAuth2 spec. Returns a signed JWT access token on success.

![Login](Screenshots/2%20login.JPG)

**Note:** Logging in through Swagger's "Try it out" only displays the token - it does not
attach it to other requests. To actually authenticate subsequent calls in Swagger UI, login
must be done through the lock icon (Authorize popup), which is what was used for the
protected-route tests below.

---

## 3. Authorize (Swagger UI)

Using the Authorize popup with valid credentials attaches the JWT automatically to all
protected requests made afterward.

![Authorize Popup](Screenshots/3%20popup_authorize.JPG)

---

## 4. Create Task (Protected Route)

With a valid token attached, `POST /tasks` succeeds and the created task includes an
`owner` field tied to the logged-in user - confirming tasks are scoped per user, not global.

**Request body:**

```
{
  "title": "Prepare Sprint 01 demo walkthrough",
  "notes": "Cover auth flow, protected routes, and JWT validation",
  "priority": 1,
  "due_date": "2026-07-18",
  "is_done": false
}
```

Returns `201 Created` with the task, including `"owner": "abdulhaq"`.

![Authorized Create Task](Screenshots/4%20authorized_create_task.JPG)

---

## 5. Logout + Rejected Access (Blacklist Working)

After calling `POST /auth/logout`, the token is added to an in-memory blacklist.
Attempting `POST /tasks` again with that same (now-blacklisted) token correctly returns
`401 Unauthorized` with a specific message - not just a generic auth failure, confirming
the blacklist check itself is functioning, not just missing-token handling.

**Response:**

```
{
  "detail": "Token has been logged out. Please login again."
}
```

![Unauthorized After Logout](Screenshots/5%20unauthorized_after_logout.JPG)

---

## Server Logs (Live Evidence)

Terminal output confirming the full real request cycle during testing:

```
INFO:  "POST /auth/login HTTP/1.1" 200 OK
INFO:  "POST /tasks HTTP/1.1" 201 Created
INFO:  "POST /tasks HTTP/1.1" 401 Unauthorized
```

Sequence shown: successful login, authorized task creation, then rejected request after logout.

---

## Key Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Stateless JWT + in-memory blacklist for logout | JWTs can't be invalidated server-side by default. A blacklist set is the standard workaround, kept in-memory since persistent storage arrives in Days 11-12. |
| Separate input/output schemas | `UserRegister` (input) and `UserOut` (output) ensure the hashed password never leaks in a response. |
| 72-byte bcrypt limit | Password field capped at `max_length=72` to avoid silent truncation by bcrypt's underlying byte limit. |
| Tasks are user-scoped | Every task stores an `owner` field; list/get endpoints filter by the current authenticated user, not global storage. |
| In-memory storage (users + tasks) | Consistent with sprint pacing; SQLAlchemy and persistent storage replace this in Days 11-12. |

---

## Known Environment Note

During setup, `passlib` (last updated 2020) failed to detect newer `bcrypt` (5.0.0) releases
correctly, throwing a misleading "password too long" error regardless of actual password
length. Resolved by pinning `bcrypt==4.0.1`, a known compatible version. Documented here since
it's a real dependency-compatibility issue, not a validation bug - worth knowing for future
environment setups.

---

*Part of Nolyth AI Bootcamp Sprint 01 - Days 8-10 (Auth + API Structure).*

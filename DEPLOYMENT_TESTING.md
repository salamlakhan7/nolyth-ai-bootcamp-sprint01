#  Deployment Testing - Personal Task Tracker

### Sprint 01, Days 13-14 - Nolyth AI Bootcamp - Abdul Salam

This document verifies the full production deployment of the Personal Task Tracker: a live FastAPI backend, a persistent PostgreSQL database, and a deployed Streamlit UI - all connected and working together, not just running locally.

> **Note:** Public deployment of the backend and database was not explicitly required by the sprint brief (only a local demo or demo video was expected). It was done anyway to prove the system works end-to-end in a real production environment.

---

## 🧱 Architecture

```
Streamlit Cloud (UI)  →  Render (FastAPI backend)  →  Neon (PostgreSQL database)
```

| Layer | Service | Live URL |
|---|---|---|
| Frontend | Streamlit Community Cloud | https://nolyth-task-tracker.streamlit.app |
| Backend | Render (Web Service) | https://nolyth-ai-bootcamp-sprint01.onrender.com |
| Database | Neon (Serverless Postgres) | *(private connection, not public-facing)* |

---

## 1. Backend - Live on Render

The FastAPI backend was deployed as a Render Web Service, reading `SECRET_KEY` and `DATABASE_URL` from environment variables (never hardcoded/committed).

**Render dashboard confirming the service is live and healthy:**

![Render dashboard - live deployment](streamlit-ui/screenshots/0%20render_dashboard_showing_live_deployed.JPG)

**Swagger UI (`/docs`) - auto-generated API documentation, confirming all routes deployed correctly:**

![Swagger overview](streamlit-ui/screenshots/1%20nolyth-ai-bootcamp-sprint01_onrendercom_docs%20overall%20lookup.JPG)

---

## 2. Backend - Auth Endpoints Tested Live

Tested directly against the deployed backend (not localhost) via Swagger UI.

**`POST /auth/register` - 201 Created:**

![Register on live backend](streamlit-ui/screenshots/2%20auth_register_on_backend_side.JPG)

**`POST /auth/login` - 200 OK, real JWT access token returned:**

![Login on live backend](streamlit-ui/screenshots/3%20auth_login_on_backend_side.JPG)

This confirms the backend isn't just "running" - it's correctly issuing tokens and validating credentials in production.

---

## 3. Database - Persistence Proof (Neon PostgreSQL)

The strongest proof of persistence isn't a successful API response - it's the actual data sitting in the database afterward.

**`SELECT * FROM users;` - real registered user data stored in Postgres:**

![Neon users query](streamlit-ui/screenshots/6%20neon_sql_editor_get_all_user_query.JPG)

**`SELECT * FROM tasks;` - real task data stored, matching what was created via the UI:**

![Neon tasks query](streamlit-ui/screenshots/7%20neon_sql_editor_get_all_tasks_query.JPG)

**Tables view - schema created automatically via SQLAlchemy on startup:**

![Neon stored user data](streamlit-ui/screenshots/5%20neon_stored_user_data.JPG)
![Neon stored task data](streamlit-ui/screenshots/4%20neon_stored_task_data.JPG)

This confirms data survives independently of the API - it's genuinely persisted, not held in memory.

---

## 4. Frontend - Streamlit UI (Deployed)

The Streamlit app is deployed on Streamlit Community Cloud and calls the **live Render backend** (not localhost) via an environment-based `API_URL`, using `os.getenv("API_URL", "http://127.0.0.1:8000")` - so the same codebase runs locally *or* in production with no code changes.

**Register:**

![Streamlit register](streamlit-ui/screenshots/9%20streamlit_register_ui.JPG)

**Login:**

![Streamlit login](streamlit-ui/screenshots/8%20streamlit_login.JPG)

**Add Task form:**

![Streamlit add task](streamlit-ui/screenshots/10%20streamlit_input_add_task_data.JPG)

**Task list - priorities, filters, and status all rendering correctly from live data:**

![Streamlit task list](streamlit-ui/screenshots/11%20streamlit_task_List_data_ui.JPG)

---

## 5. Known Limitations (Honest Notes)

- **Render free-tier cold start:** the backend spins down after inactivity. The **first** login/register request after idle time can take 30–50 seconds to respond while the service wakes up. This is expected behavior on Render's free tier, not a bug - subsequent requests are fast. Worth knowing ahead of a live demo, so it doesn't look like something's broken during that first request.
- **SQLite vs Postgres:** locally the app falls back to SQLite (see `DATABASE_NOTES.md`); in production it uses Neon Postgres via `DATABASE_URL`, following the same environment-based pattern as the API URL.
- **Neon free tier:** database may pause after inactivity as well, with a similar brief wake-up delay on first query.

---

## Summary

| Piece | Status |
|---|---|
| FastAPI backend deployed publicly | ✅ Render |
| Database persistence verified with real queries | ✅ Neon Postgres |
| Auth flow (register/login/JWT) tested on live backend | ✅ |
| Streamlit UI deployed and calling live API | ✅ Streamlit Cloud |
| Environment-based config (no hardcoded secrets/URLs) | ✅ |

Full pipeline - UI → API → Database - is live, connected, and verified with real data at every layer.
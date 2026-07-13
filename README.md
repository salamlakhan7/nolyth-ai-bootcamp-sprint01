# Nolyth AI Bootcamp - Sprint 01: Backend Foundations

This repository documents my progress through **Sprint 01** of the Nolyth AI Bootcamp (Associate AI Engineer Training Program). The sprint focuses on backend foundations: Python core skills, Git/GitHub workflow, FastAPI, database integration, and a Streamlit interface - built incrementally with daily commits.

**Sprint 01 is complete** - auth, database persistence, API, UI, and full production deployment, all connected end-to-end.

## Program Info

**Program:** Nolyth AI Bootcamp - Associate AI Engineer Training
**Sprint:** 01 - Backend Foundations
**Duration:** 2 Weeks (Days 1-14)
**Stack:** Python, Git & GitHub, FastAPI, SQLAlchemy, PostgreSQL, Streamlit

## Live Demo

| Layer | Service | URL |
|---|---|---|
| Frontend (Streamlit) | Streamlit Community Cloud | https://nolyth-task-tracker.streamlit.app |
| Backend (FastAPI) | Render | https://nolyth-ai-bootcamp-sprint01.onrender.com |
| API Docs | Render (Swagger UI) | https://nolyth-ai-bootcamp-sprint01.onrender.com/docs |

> Note: the backend runs on Render's free tier, which spins down after inactivity. The first request may take 30-50 seconds while it wakes up - expected behavior, not a bug.

Public deployment of the backend and database was not required by the sprint brief (a local demo or demo video was sufficient), but was done anyway to prove the system works end-to-end in a real production environment. See `DEPLOYMENT_TESTING.md` for full verification with screenshots.

## Topics Covered

| Day | Topic | File / Folder | Status |
|-----|-------|----------------|--------|
| 1 | Functions (args, kwargs, defaults) | `01_functions.py` | Done |
| 1 | Loops (for, while, nested, break/continue) | `02_loops.py` | Done |
| 1 | Lists, Dictionaries, Sets | `03_lists_dicts_sets.py` | Done |
| 2 | OOP (Classes, Inheritance, Polymorphism, Encapsulation) | `04_oop.py` | Done |
| 2 | Error Handling & File Handling | `05_error_file_handling.py` | Done |
| 3 | Git & GitHub - repos, staging, commits, branches, merge vs rebase, PRs, issue tracking | `GIT_WORKFLOW.md` | Done |
| 5-7 | FastAPI Basics - routes, path/query params, request/response models, Pydantic validation, status codes, API docs | `fastapi-basics/` | Done |
| 8-10 | Auth + API Structure - JWT login/logout, routers, services, schemas, protected routes | `auth-api-structure/` | Done |
| 11-12 | Databases - SQLAlchemy models, persistent CRUD, sessions, SQLite/PostgreSQL, migrations concepts | `auth-api-structure/` (`database.py`, `DATABASE_NOTES.md`) | Done |
| 13-14 | Streamlit UI + Full Deployment - forms, task list, filters, live production deployment | `streamlit-ui/`, `DEPLOYMENT_TESTING.md` | Done |

## Sprint Project

**Task/To-Do Manager with Login** - a full-stack project covering authentication, database-backed CRUD APIs, and a Streamlit interface, built end-to-end using the Sprint 01 stack and deployed live across three connected services (Streamlit Cloud, Render, Neon PostgreSQL).

## Repo Structure

Each Python fundamentals topic is kept in its own file, and each subsequent phase (FastAPI basics, Auth + structure, Streamlit UI) is kept in its own dedicated folder with its own testing documentation and screenshots - committed and pushed individually to maintain a clean, incremental commit history, as required by the sprint guidelines.

- `auth-api-structure/` - FastAPI backend: auth, tasks, database layer, deployed on Render
  - `DATABASE_NOTES.md` - SQLite vs PostgreSQL, sessions, migrations
  - `AUTH_TESTING.md` - JWT auth flow testing
- `streamlit-ui/` - Streamlit front-end, deployed on Streamlit Community Cloud
- `DEPLOYMENT_TESTING.md` - full-stack deployment verification (backend, database, frontend) with screenshots
- `06 GIT_WORKFLOW.md` - Git/GitHub concepts in detail

## Progress Approach

Followed an incremental build-and-commit workflow throughout: one topic → one file/folder → one commit → push → next topic. No batch pushes.

---
*Nolyth AI Bootcamp Sprint 01 submission - complete.*

#  Database Notes - Sprint 01 (Days 11-12)
### Personal Task Tracker - Auth Edition

This sprint moved the API from in-memory Python dictionaries to a real, persistent database layer using **SQLAlchemy** + **SQLite**. These notes cover the *why* behind the choices made, not just the *what*.

---

## 1. Why Persistence Matters

Before this sprint, every `User` and `Task` lived in a plain Python `dict`. That meant:

-  Restarting the server wiped all data
-  No real concurrency - a dict isn't safe under simultaneous writes
-  Fine for prototyping, unusable for anything real

Swapping to a database layer means data now survives restarts, supports proper querying, and scales toward a real production setup.

---

## 2. SQLite vs PostgreSQL — Why SQLite Now

| | **SQLite** (used here) | **PostgreSQL** |
|---|---|---|
| Setup | Zero config - it's a single file | Needs a running server/service |
| Best for | Local dev, small apps, learning | Production, multi-user, high concurrency |
| Concurrency | Limited (file-level locking) | Excellent (built for concurrent writes) |
| Data types | Simplified/dynamic | Strict, rich types (JSON, arrays, etc.) |
| Portability | One `.db` file, easy to move | Requires a hosted instance |

**Why SQLite for this sprint:** the goal was to prove out the *persistence layer* - real models, real queries, real sessions - without the overhead of standing up a separate database server. SQLite gives 100% of the learning value with 0% of the infrastructure friction.

**The upgrade path is intentionally trivial.** Because SQLAlchemy abstracts the database engine, moving to PostgreSQL later is a **one-line change**:

```python
# Today:
SQLALCHEMY_DATABASE_URL = "sqlite:///./sprint01.db"

# Later, in production:
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@host/dbname"
```

Everything else - models, queries, routes - stays exactly the same. That's the entire point of an ORM.

---

## 3. What an ORM Actually Buys You

**ORM = Object-Relational Mapper.** Instead of writing raw SQL strings, you define Python classes (`User`, `Task`) that map to database tables, and SQLAlchemy translates your Python code into SQL behind the scenes.

```python
# Instead of writing SQL like:
# SELECT * FROM tasks WHERE owner = 'salam' AND is_done = 0

# You write Python:
db.query(Task).filter(Task.owner == "salam", Task.is_done == False).all()
```

Benefits:
- Type-safe, autocomplete-friendly queries
- Database-agnostic code (same code works on SQLite *or* Postgres)
- Less room for SQL injection bugs, since inputs are parameterized automatically

---

## 4. Why Sessions Matter

A **session** is a temporary workspace between your code and the database - it tracks changes, batches them, and commits them as a single transaction.

```python
db.add(new_user)      # stage the change (not saved yet)
db.commit()            # actually write it to the database
db.refresh(new_user)   # reload it, picking up DB-generated fields (like the id)
```

Why not just write directly to the database on every line?

-  **Atomicity**   : if something fails mid-operation, you can roll back instead of leaving half-written data
-  **Performance** : changes are batched instead of hitting the disk on every single line
-  **Isolation**   : each request gets its own session, so concurrent requests don't corrupt each other's in-progress work

In this project, a fresh session is created **per request** via a FastAPI dependency (`get_db`), used for that request's queries, and closed automatically afterward — no leaked connections, no shared state between users.

---

## 5. Migrations - Managing Schema Change Over Time

Right now, tables are created with:

```python
Base.metadata.create_all(bind=engine)
```

This works great for a *brand-new* database - it looks at your models and creates matching tables. But it has a hard limit: **it will never alter an existing table.** If you add a new column to `User` next sprint, `create_all` will silently do nothing, and the old table stays as-is.

That's the exact problem **migration tools** solve. The most common one in the SQLAlchemy ecosystem is **Alembic**.

**What Alembic does:**
- Compares your current models against the live database schema
- Auto-generates a versioned script describing the *difference* (e.g. "add column `email_verified` to `users`")
- Lets you apply (`upgrade`) or undo (`downgrade`) that change safely
- Keeps a full history of every schema change your project has ever made - like version control, but for your database structure

**Why this matters beyond a training sprint:** in a real production system, you can't just drop and recreate tables every time the schema changes - that would destroy live user data. Migrations let schema evolve *safely, incrementally, and reversibly* alongside the codebase.

---

## 6. Summary

| Concept | Role in this project |
|---|---|
| **SQLAlchemy** | ORM - turns Python classes into database tables and queries |
| **SQLite** | Lightweight file-based database used for this sprint |
| **Engine** | The connection point between SQLAlchemy and the actual database file |
| **Session** | Per-request workspace for staging and committing changes safely |
| **Models** (`User`, `Task`) | Python classes defining table structure |
| **Migrations (Alembic)** | Tool for evolving the schema safely over time (not yet added - noted here as the natural next step) |

This sprint's database layer is intentionally scoped: real persistence, real sessions, real queries - without over-engineering infrastructure that isn't needed yet. The architecture is already shaped so that swapping in PostgreSQL and Alembic later requires configuration changes, not a rewrite.

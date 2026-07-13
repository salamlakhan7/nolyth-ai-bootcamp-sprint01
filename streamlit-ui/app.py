# app.py
# Nolyth AI Bootcamp - Sprint 01 (Days 13-14)
# Streamlit front-end for the Personal Task Tracker API
import os
import streamlit as st
import requests


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


st.set_page_config(page_title="Personal Task Tracker", page_icon="✅", layout="centered")

# ----- Session state setup -----
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None


def auth_header():
    return {"Authorization": f"Bearer {st.session_state.token}"}


# ----- LOGIN / REGISTER SCREEN -----
def show_auth_screen():
    st.title("✅ Personal Task Tracker")
    st.caption("Sprint 01 - Nolyth AI Bootcamp - Abdul Salam")

    tab_login, tab_register = st.tabs(["Login", "Register"])

    with tab_login:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

            if submitted:
                response = requests.post(
                    f"{API_URL}/auth/login",
                    data={"username": username, "password": password},
                )
                if response.status_code == 200:
                    st.session_state.token = response.json()["access_token"]
                    st.session_state.username = username
                    st.success("Logged in successfully.")
                    st.rerun()
                else:
                    detail = response.json().get("detail", "Login failed.")
                    st.error(detail)

    with tab_register:
        with st.form("register_form"):
            new_username = st.text_input("Choose a username")
            new_email = st.text_input("Email")
            new_password = st.text_input("Choose a password", type="password")
            submitted = st.form_submit_button("Register")

            if submitted:
                response = requests.post(
                    f"{API_URL}/auth/register",
                    json={
                        "username": new_username,
                        "email": new_email,
                        "password": new_password,
                    },
                )
                if response.status_code == 201:
                    st.success("Account created. Please log in from the Login tab.")
                else:
                    detail = response.json().get("detail", "Registration failed.")
                    st.error(detail)


# ----- TASK DASHBOARD -----
def show_dashboard():
    st.title("✅ My Tasks")
    st.caption(f"Logged in as **{st.session_state.username}**")

    if st.button("Logout"):
        requests.post(f"{API_URL}/auth/logout", headers=auth_header())
        st.session_state.token = None
        st.session_state.username = None
        st.rerun()

    st.divider()

    # ----- Add Task Form -----
    with st.expander("➕ Add New Task", expanded=False):
        with st.form("add_task_form", clear_on_submit=True):
            title = st.text_input("Title")
            notes = st.text_area("Notes", height=80)
            col1, col2 = st.columns(2)
            with col1:
                priority = st.selectbox("Priority", [1, 2, 3], index=1,
                                         format_func=lambda p: {1: "High", 2: "Medium", 3: "Low"}[p])
            with col2:
                due_date = st.date_input("Due Date")

            submitted = st.form_submit_button("Add Task")
            if submitted:
                if not title.strip():
                    st.error("Title is required.")
                else:
                    payload = {
                        "title": title,
                        "notes": notes or None,
                        "priority": priority,
                        "due_date": str(due_date),
                        "is_done": False,
                    }
                    response = requests.post(f"{API_URL}/tasks", json=payload, headers=auth_header())
                    if response.status_code == 201:
                        st.success("Task added.")
                        st.rerun()
                    else:
                        st.error(response.json().get("detail", "Could not add task."))

    st.divider()

    # ----- Filters -----
    st.subheader("📋 Task List")
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        status_filter = st.selectbox("Filter by status", ["All", "Done", "Not Done"])
    with filter_col2:
        priority_filter = st.selectbox("Filter by priority", ["All", "High", "Medium", "Low"])

    params = {}
    if status_filter != "All":
        params["is_done"] = (status_filter == "Done")
    if priority_filter != "All":
        params["priority"] = {"High": 1, "Medium": 2, "Low": 3}[priority_filter]

    response = requests.get(f"{API_URL}/tasks", params=params, headers=auth_header())

    if response.status_code != 200:
        st.error("Could not load tasks.")
        return

    tasks = response.json()

    if not tasks:
        st.info("No tasks found. Add one above.")
        return

    priority_labels = {1: "🔴 High", 2: "🟡 Medium", 3: "🟢 Low"}

    for task in tasks:
        with st.container(border=True):
            col1, col2, col3, col4 = st.columns([4, 2, 1, 1])
            with col1:
                status_icon = "✅" if task["is_done"] else "⬜"
                st.markdown(f"{status_icon} **{task['title']}**")
                if task["notes"]:
                    st.caption(task["notes"])
                if task["due_date"]:
                    st.caption(f"Due: {task['due_date']}")
            with col2:
                st.write(priority_labels.get(task["priority"], "—"))
            with col3:
                if st.button("Toggle", key=f"toggle_{task['task_id']}"):
                    requests.patch(f"{API_URL}/tasks/{task['task_id']}", headers=auth_header())
                    st.rerun()
            with col4:
                if st.button("🗑️", key=f"delete_{task['task_id']}"):
                    requests.delete(f"{API_URL}/tasks/{task['task_id']}", headers=auth_header())
                    st.rerun()


# ----- MAIN ROUTER -----
if st.session_state.token is None:
    show_auth_screen()
else:
    show_dashboard()
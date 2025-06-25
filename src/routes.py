import streamlit as st


pages = {
    "Home": [
        st.Page("main/pages/home_page.py", title="Página inicial", icon=":material/home:")
    ],
    "Usuários": [
        st.Page("users/pages/user_page.py", title="Gerenciar usuários", icon=":material/group:", url_path="users")
    ],
    "Tarefas": [
        st.Page("tasks/pages/task_page.py", title="Gerenciar tarefas", icon=":material/edit:", url_path="tasks")
    ],
}

import streamlit as st
import main.pages.home_page as home_page
import users.pages.user_page as user_page
import tasks.pages.task_page as task_page


def deslogar():
    for chave in list(st.session_state.keys()):
        del st.session_state[chave]

    st.rerun()


pages = {
    "Home": [
        st.page_link(home_page.run, title="Página inicial", icon="🏠", default=True)
    ],
    "Usuários": [
        st.page_link(user_page.run, title="Gerenciar usuários", icon="👥", url_path="users")
    ],
    "Tarefas": [
        st.page_link(task_page.run, title="Gerenciar tarefas", icon="📝", url_path="tasks")
    ]
}

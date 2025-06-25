import streamlit as st
from database.connection import SessionLocal
from users.services.authentication_service import AuthenticationService


def login(email: str, senha: str):
    db = SessionLocal()
    auth_service = AuthenticationService(db)

    usuario = auth_service.autenticar_usuario(email, senha)

    if usuario:
        st.session_state["nome_usuario"] = usuario["nome"]
        st.session_state["id_usuario"] = usuario["id"]
        st.session_state["logado"] = True
        st.rerun()
    else:
        st.error("Email ou senha inválidos.")

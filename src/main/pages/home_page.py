import streamlit as st


def run():
    st.title("📋 Bem-vindo ao Sistema de Tarefas")
    st.markdown(
        """
        Este é um aplicativo Streamlit com suporte a múltiplos usuários e controle de tarefas.

        ### O que você pode fazer:
        - 👤 Criar e gerenciar usuários
        - ✅ Criar e atualizar tarefas

        Navegue pelas opções no menu lateral para começar!
        """
    )

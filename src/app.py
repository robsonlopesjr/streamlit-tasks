import streamlit as st
from routes import pages, deslogar
from database.init_db import inicializar_banco
from utils.log import setup_logging
from users.pages.login_page import login


def init():
    inicializar_banco()

    # Inicializa sessão
    if "logado" not in st.session_state:
        st.session_state["logado"] = False


def main():
    # 🔐 Tela de login
    if not st.session_state["logado"]:

        st.title("🔐 Login")
        with st.form("form_login"):
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar")
            if submit:
                login(email, senha)

        st.stop()  # Evita que o menu e as páginas carreguem

    else:
        # 🔓 Sidebar com logout e usuário logado
        with st.sidebar:
            st.markdown(f"👤 {st.session_state.get('nome_usuario', 'Usuário')}")
            if st.button("🚪 Sair do Sistema"):
                # Desloga e interrompe a execução
                deslogar()
                st.stop()

        # 📁 Mostra o menu se estiver logado
        pg = st.navigation(pages)
        pg.run()


if __name__ == '__main__':
    setup_logging()
    init()
    main()

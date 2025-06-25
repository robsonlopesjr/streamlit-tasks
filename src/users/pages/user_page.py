import streamlit as st
import users.controllers.user_controller as controller


def run():
    st.title("👥 Cadastro de Usuários")

    # ⬅️ Detecta e limpa campos no início
    if st.session_state.get("limpar_form"):
        st.session_state["input_nome"] = ""
        st.session_state["input_email"] = ""
        st.session_state["input_senha"] = ""
        st.session_state["limpar_form"] = False
        st.rerun()

    # Inicializa os campos se ainda não existem
    if "input_nome" not in st.session_state:
        st.session_state["input_nome"] = ""
    if "input_email" not in st.session_state:
        st.session_state["input_email"] = ""
    if "input_senha" not in st.session_state:
        st.session_state["input_senha"] = ""

    st.subheader("➕ Novo Usuário")
    with st.form("form_usuario"):
        nome = st.text_input("Nome", key="input_nome")
        email = st.text_input("Email", key="input_email")
        senha = st.text_input("Senha", type="password", key="input_senha")

        if st.form_submit_button("Cadastrar"):
            erros = []
            if not nome.strip():
                erros.append("O nome não pode estar vazia.")

            if not email.strip():
                erros.append("O email não pode estar vazia.")

            if not senha.strip():
                erros.append("A senha não pode estar vazia.")

            if erros:
                for erro in erros:
                    st.warning(erro)
            else:
                try:
                    controller.criar_usuario(nome, email, senha)
                    st.success("Usuário cadastrado com sucesso!")
                    st.rerun()
                except ValueError as e:
                    st.warning(str(e))

    st.divider()
    st.subheader("📋 Usuários Cadastrados")

    for u in controller.carregar_usuarios():
        with st.expander(f"👤 {u.nome} | 📧 {u.email}"):
            with st.form(f"form_edit_{u.id}"):
                nome = st.text_input("Nome", value=u.nome, key=f"n_{u.id}")
                email = st.text_input("Email", value=u.email, key=f"e_{u.id}")
                senha = st.text_input("Senha", value=u.senha, key=f"s_{u.id}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("✏️ Atualizar", use_container_width=True):
                        try:
                            controller.salvar_edicao(u.id, nome, email, senha)
                            st.success("Usuário atualizado!")
                            st.rerun()
                        except ValueError as e:
                            st.warning(str(e))
                with col2:
                    if st.form_submit_button("🗑️ Excluir", use_container_width=True):
                        controller.excluir_usuario(u.id)
                        st.success("Usuário excluído!")
                        st.rerun()

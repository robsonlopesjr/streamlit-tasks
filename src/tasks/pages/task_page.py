from datetime import date
import streamlit as st
import tasks.controllers.task_controller as controller


def run():
    st.title("📝 CRUD de Tarefas")

    # ⬅️ Detecta e limpa campos no início
    if st.session_state.get("limpar_form"):
        st.session_state["input_data"] = date.today()
        st.session_state["input_descricao"] = ""
        st.session_state["input_concluido"] = False
        st.session_state["limpar_form"] = False
        st.rerun()

    # Inicializa os campos se ainda não existem
    if "input_data" not in st.session_state:
        st.session_state["input_data"] = date.today()
    if "input_descricao" not in st.session_state:
        st.session_state["input_descricao"] = ""
    if "input_concluido" not in st.session_state:
        st.session_state["input_concluido"] = False

    # FORMULÁRIO
    with st.form("form_tarefa"):
        st.subheader("➕ Nova Tarefa")

        data = st.date_input("Data", key="input_data")
        descricao = st.text_input("Descrição", key="input_descricao")
        concluido = st.checkbox("Concluída?", key="input_concluido")

        submitted = st.form_submit_button("Adicionar")

        if submitted:
            erros = []

            if not descricao.strip():
                erros.append("A descrição não pode estar vazia.")
            if data < date(2000, 1, 1):  # opcional
                erros.append("Data inválida.")

            if erros:
                for erro in erros:
                    st.warning(erro)
            else:
                controller.criar_tarefa(data, descricao, concluido)
                st.success("Tarefa adicionada!")

                # Limpar os campos
                st.session_state["limpar_form"] = True
                st.rerun()

    st.divider()
    st.subheader("📋 Lista de Tarefas")

    tarefas = controller.carregar_tarefas()

    if not tarefas:
        st.info("Nenhuma tarefa cadastrada.")
        return

    for t in controller.carregar_tarefas():
        with st.expander(f"🗓️ {t.data.strftime('%d/%m/%Y')} | 📌 {t.descricao} | {'✅' if t.concluido else '❌'}", expanded=False):
            with st.form(f"form_{t.id}"):
                data = st.date_input("Data", value=t.data, key=f"d_{t.id}")
                descricao = st.text_input("Descrição", value=t.descricao, key=f"de_{t.id}")
                concluido = st.checkbox("Concluída?", value=t.concluido, key=f"c_{t.id}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("✏️ Atualizar", use_container_width=True):
                        controller.salvar_edicao(t.id, data, descricao, concluido)
                        st.success("Tarefa editada!")
                        # Limpar os campos
                        st.session_state["limpar_form"] = True
                        st.rerun()
                with col2:
                    if st.form_submit_button("🗑️ Excluir", use_container_width=True):
                        controller.excluir_tarefa(t.id)
                        st.success("Tarefa apagada!")
                        # Limpar os campos
                        st.session_state["limpar_form"] = True
                        st.rerun()

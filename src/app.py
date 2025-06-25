import streamlit as st
from datetime import date

st.set_page_config(page_title="CRUD de Tarefas", layout="centered")

# Inicializa a lista de tarefas
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

st.title("📝 CRUD de Tarefas")

# Formulário para adicionar nova tarefa
with st.form("form_tarefa", clear_on_submit=True):
    data = st.date_input("Data", value=date.today())
    descricao = st.text_input("Descrição da tarefa")
    concluido = st.checkbox("Concluída?")
    enviar = st.form_submit_button("Adicionar")

    if enviar and descricao:
        nova_tarefa = {"data": data, "descricao": descricao, "concluido": concluido}
        st.session_state.tarefas.append(nova_tarefa)
        st.success("Tarefa adicionada com sucesso!")

# Exibição das tarefas
st.subheader("📋 Lista de Tarefas")

if st.session_state.tarefas:
    for i, tarefa in enumerate(st.session_state.tarefas):
        cols = st.columns([2, 4, 2, 1])
        cols[0].write(tarefa["data"].strftime("%d/%m/%Y"))
        cols[1].write(tarefa["descricao"])
        tarefa["concluido"] = cols[2].checkbox("Concluído", value=tarefa["concluido"], key=f"check_{i}")
        if cols[3].button("🗑️", key=f"delete_{i}"):
            st.session_state.tarefas.pop(i)
            st.rerun()
else:
    st.info("Nenhuma tarefa cadastrada.")

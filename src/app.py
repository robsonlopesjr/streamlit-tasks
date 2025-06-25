import streamlit as st
from routes import pages


def exibir():
    pg = st.navigation(pages)

    # Roda a página selecionada no menu
    pg.run()


if __name__ == '__main__':
    exibir()

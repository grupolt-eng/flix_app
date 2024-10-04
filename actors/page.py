import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Leonardo di Caprio'
    },
    {
        'id': 2,
        'name': 'Will Smith'
    },
    {
        'id': 3,
        'name': 'Chris Rock'
    },
]


def show_actors():
    st.write('LISTA DE ATORES: ')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True, key='actors_grid',
    )

    st.title('Cadastrar novo Ator')
    name = st.text_input('Nome do novo ator')
    if st.button('Cadastrar'):
        st.success(f'Genero "{name}" cadastrado com sucesso!')

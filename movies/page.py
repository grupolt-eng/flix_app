import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Senhor dos Anéis'
    },
    {
        'id': 3,
        'name': 'Rambo'
    },
]


def show_movies():
    st.write('LISTA DE FILMES: ')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True, key='movies_grid',
    )

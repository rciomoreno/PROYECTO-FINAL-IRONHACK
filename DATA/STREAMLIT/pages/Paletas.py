import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_card import card
from markdownlit import mdlit
from streamlit_extras.badges import badge
from streamlit_extras.stoggle import stoggle


st.set_page_config(page_title='Paleta', page_icon="https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f484@2x.png", layout="wide", initial_sidebar_state="auto", menu_items=None)

stoggle('¡Sígueme!', ' ' )

badge(type="github", name="rciomoreno")
badge(type="twitter", name="rciomoreno")

colored_header(
    label='    ',
    description = '     ',
    color_name="red-50",
)

st.markdown("<h1 style='text-align: center; color: white;'>TU PALETA ES:</h1>", unsafe_allow_html=True)



reco = pd.read_csv('../STREAMLIT/pages/recomendaciones_csv.v2.csv')
res = pd.read_csv('../STREAMLIT/pages/resultados/resultado.csv')




var = res.PALETAS.values[0]

card(
        title = var,
        text = '  ',
        image = 'https://data.whicdn.com/images/332265316/original.jpg',
        url = 'https://www.canva.com/design/DAFU04J4k2g/s4uS8QGFfzFdBkiIV5eObg/edit#', #presentación de canva
    )

col1, col2, col3 = st.columns([ 1, 1, 1])

with col2:
    def elegir_estacion(var):
        if var == 'OTOÑO':
            return st.image('OTOÑO2-removebg-preview.png')
        elif var == 'VERANO':
            return st.image('VERANO2-removebg-preview.png')
        elif var == 'INVIERNO':
            return st.image('INVIERNO2-removebg-preview (1).png')
        else:
            return st.image('PRIMAVERA2-removebg-preview.png')

    elegir_estacion(var)

var2 = reco[reco['PALETA'].str.contains(var)][['NOMBRE', 'PRODUCTO', 'TIENDA', 'LINK', 'PRECIO (€)']]
valor = st.slider('Elige un rango de precio', var2['PRECIO (€)'].min(),  var2['PRECIO (€)'].max())
filtered_df = dataframe_explorer((var2[var2['PRECIO (€)']<=valor]))
st.dataframe(filtered_df, use_container_width=True)

boton = st.button('Volver')
if boton:
    switch_page('Colores')
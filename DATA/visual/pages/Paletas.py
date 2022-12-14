import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_card import card



st.set_page_config(layout='wide')

colored_header(
    label='    ',
    description = '     ',
    color_name="red-50",
)

st.markdown("<h1 style='text-align: center; color: white;'>TU PALETA ES:</h1>", unsafe_allow_html=True)



reco = pd.read_csv('../visual/pages/recomendaciones_csv.v2.csv')
res = pd.read_csv('../visual/pages/resultados/resultado.csv')

var = res.PALETAS.values[0]
card(
    title = var,
    text = '  ',
    image = 'https://data.whicdn.com/images/332265316/original.jpg',
    url = ' ', #poner Tableau 
)
var2 = reco[reco['PALETA'].str.contains(var)][['NOMBRE', 'PRODUCTO', 'TIENDA', 'LINK', 'PRECIO (€)']]
valor = st.slider('Elige un rango de precio', var2['PRECIO (€)'].min(),  var2['PRECIO (€)'].max())
filtered_df = dataframe_explorer((var2[var2['PRECIO (€)']<=valor]))
st.dataframe(filtered_df, use_container_width=True)

boton = st.button('Volver')
if boton:
    switch_page('Colores')
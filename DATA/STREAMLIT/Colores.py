import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge
from streamlit_extras.stoggle import stoggle



st.set_page_config(page_title='Colores', page_icon="https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f484@2x.png", layout="wide", initial_sidebar_state="auto", menu_items=None)

stoggle('¡Sígueme!', ' ' )

badge(type="github", name="rciomoreno")
badge(type="twitter", name="rciomoreno")

colored_header(
    label='    ',
    description = '     ',
    color_name="red-50",
)
st.markdown("<h1 style='text-align: center; color: white;'>MAQUÍLLATE SEGÚN TU COLORIMETRÍA FACIAL</h1>", unsafe_allow_html=True)

card(
    title='ELIGE TUS COLORES',
    text='¡Lo más parecido posible!',
    image='https://data.whicdn.com/images/332265316/original.jpg',
    url='https://www.canva.com/design/DAFU04J4k2g/s4uS8QGFfzFdBkiIV5eObg/edit#', #presentación de Canva
)




combinaciones = pd.read_csv('../STREAMLIT/combinaciones_final.csv')
recomendaciones = pd.read_csv('../STREAMLIT/recomendaciones_csv.v2.csv')


cabello, croma_cab = st.columns(2)
ojos, croma_ojo = st.columns(2)
piel,croma_piel= st.columns(2)

with cabello:
    cabello = st.selectbox('Elige tu color de cabello', combinaciones.CABELLO.unique())

with croma_cab:
    croma_cab = st.radio('Un color de cabello (brillante) o más de 1 color (suave)', combinaciones.CROMA_CAB.unique())

with ojos:
    ojos = st.selectbox('Elige tu color de ojos', combinaciones.OJOS.unique())

with croma_ojo:
    croma_ojo = st.radio('Un color de ojos (brillante) o más de 1 color (suave)', combinaciones.CROMA_OJOS.unique())

with piel:
    piel = st.selectbox('Elige tu color de piel', combinaciones.PIEL.unique())

with croma_piel:
    croma_piel = st.radio('Un color de piel (brillante) o más de 1 color (suave)', combinaciones.CROMA_PIEL.unique())



    resultado = combinaciones[(combinaciones.CABELLO == cabello) &
                (combinaciones.OJOS == ojos) &
                (combinaciones.PIEL == piel) &
                (combinaciones.CROMA_CAB == croma_cab) &
                (combinaciones.CROMA_OJOS == croma_ojo) &
                (combinaciones.CROMA_PIEL == croma_piel) &
                combinaciones.PALETAS]


resultado.to_csv('../STREAMLIT/pages/resultados/resultado.csv')

boton = st.button('Calcular paleta')
if boton:
    switch_page('Paletas')



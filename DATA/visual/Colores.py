import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge


st.set_page_config(layout='wide')

badge(type="github", name="rciomoreno")


#add_logo("https://cdn-icons-png.flaticon.com/512/6491/6491243.png")

colored_header(
    label='    ',
    description = '     ',
    color_name="red-50",
)
st.markdown("<h1 style='text-align: center; color: white;'>MAQUÍLLATE SEGÚN TU COLOMETRÍA FACIAL</h1>", unsafe_allow_html=True)

card(
    title='ELIGE TUS COLORES',
    text='¡Lo más parecido posible!',
    image='https://data.whicdn.com/images/222110080/original.jpg',
    url='https://www.google.com', #poner Tableau 
)




combinaciones = pd.read_csv('../visual/combinaciones_final_csv.csv')
recomendaciones = pd.read_csv('../visual/recomendaciones_csv.v2.csv')


cabello, croma_cab = st.columns(2)
ojos, croma_ojo = st.columns(2)
piel,croma_piel= st.columns(2)

with cabello:
    cabello = st.selectbox('Elige tu color de cabello', combinaciones.CABELLO.unique())

with croma_cab:
    croma_cab = st.radio('1 color de cabello (brillante) o más de 1 color (suave)', combinaciones.CROMA_CAB.unique())

with ojos:
    ojos = st.selectbox('Elige tu color de ojos', combinaciones.OJOS.unique())

with croma_ojo:
    croma_ojo = st.radio('1 solo color de ojos (brillante) o más de 1 color (suave)', combinaciones.CROMA_OJOS.unique())

with piel:
    piel = st.selectbox('Elige tu color de piel', combinaciones.PIEL.unique())

with croma_piel:
    croma_piel = st.radio('1 solo color de piel (brillante) o más de 1 color (suave)', combinaciones.CROMA_PIEL.unique())



    resultado = combinaciones[(combinaciones.CABELLO == cabello) &
                (combinaciones.OJOS == ojos) &
                (combinaciones.PIEL == piel) &
                (combinaciones.CROMA_CAB == croma_cab) &
                (combinaciones.CROMA_OJOS == croma_ojo) &
                (combinaciones.CROMA_PIEL == croma_piel) &
                combinaciones.PALETAS]


resultado.to_csv('../visual/pages/resultados/resultado.csv')

boton = st.button('Calcular paleta')
if boton:
    switch_page('Paletas')



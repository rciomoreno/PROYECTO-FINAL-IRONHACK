import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('ELIGE TUS COLORES')
st.header('Proyecto Final: Aprende a maquillarte en función de tu colometría')

combinaciones = pd.read_csv('../DATA/TABLA_BASE/combinaciones_final_csv.csv')

cabello, croma_cab = st.columns(2)
ojos, croma_ojo = st.columns(2)
piel,croma_piel= st.columns(2)

with cabello:
    cabello = st.selectbox('Elige tu color de cabello', combinaciones.CABELLO.unique())

with croma_cab:
    croma_cab = st.radio('1 color de pelo o más de 1 color', combinaciones.CROMA_CAB.unique())

with ojos:
    ojos = st.selectbox('Elige tu color de ojos', combinaciones.OJOS.unique())

with croma_ojo:
    croma_ojo = st.radio('1 solo color de ojos o más de 1 color', combinaciones.CROMA_OJOS.unique())

with piel:
    piel = st.selectbox('Elige tu color de piel', combinaciones.PIEL.unique())

with croma_piel:
    croma_piel = st.radio('1 solo color de piel o más de 1 color', combinaciones.CROMA_PIEL.unique())


resultado = combinaciones[(combinaciones.CABELLO == cabello) &
              (combinaciones.OJOS == ojos) &
              (combinaciones.PIEL == piel) &
              (combinaciones.CROMA_CAB == croma_cab) &
              (combinaciones.CROMA_OJOS == croma_ojo) &
              (combinaciones.CROMA_PIEL == croma_piel) &
              combinaciones.PALETAS]

#Para quitar el indice de la tabla 

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

st.table(resultado.PALETAS)





recomendaciones = pd.read_csv('../DATA/TABLA_RECOMENDACIONES/prod_recomendados_csv.csv')

precio = st.columns(1)

with precio:
    precio = st.slider('Rango de precios', recomendaciones['PRECIO (€)'])

resultados2 = recomendaciones[(recomendaciones.NOMBRE) &
                        (recomendaciones['PRECIO (€)'] == precio) &
                        (recomendaciones.LINK) &
                        (recomendaciones.PRODUCTO) &
                        (recomendaciones.TIENDA) &
                        (recomendaciones.PALETA)]

if res in recomendaciones.PALETA:
    st.table(resultados2)
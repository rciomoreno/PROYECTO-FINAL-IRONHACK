import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('ELIGE TUS COLORES')
st.header('Proyecto Final: Aprende a maquillarte en función de tu colometría')

combinaciones = pd.read_csv('../DATA/TABLA_BASE/combinaciones_final_csv.csv')
recomendaciones = pd.read_csv('../DATA/TABLA_RECOMENDACIONES/prod_recomendados_csv.csv')


cabello, croma_cab = st.columns(2)
ojos, croma_ojo = st.columns(2)
piel,croma_piel= st.columns(2)

with cabello:
    cabello = st.sidebar.selectbox('Elige tu color de cabello', combinaciones.CABELLO.unique())

with croma_cab:
    croma_cab = st.sidebar.radio('1 color de pelo o más de 1 color', combinaciones.CROMA_CAB.unique())

with ojos:
    ojos = st.sidebar.selectbox('Elige tu color de ojos', combinaciones.OJOS.unique())

with croma_ojo:
    croma_ojo = st.sidebar.radio('1 solo color de ojos o más de 1 color', combinaciones.CROMA_OJOS.unique())

with piel:
    piel = st.sidebar.selectbox('Elige tu color de piel', combinaciones.PIEL.unique())

with croma_piel:
    croma_piel = st.sidebar.radio('1 solo color de piel o más de 1 color', combinaciones.CROMA_PIEL.unique())



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

if st.button('Calcular paleta'):
    var = resultado.PALETAS[0]
    st.header(var)
    st.dataframe(recomendaciones[recomendaciones['PALETA'].str.contains(var)][['NOMBRE', 'PRODUCTO', 'TIENDA', 'LINK', 'PRECIO (€)']])
    #nuevo = st.slider('hola', 0,200,0)
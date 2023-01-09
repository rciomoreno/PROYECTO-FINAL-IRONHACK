# PROYECTO: MAQUÍLLATE EN FUNCIÓN DE TU COLORIMETRÍA FACIAL

## ABOUT ##

  Las personas que nos maquillamos siempre nos hemos hecho la misma pregunta para elegir algunos productos, sobre todo las paletas de sombras de ojos, 
  pintalabios y colorete:
  
  *¿Qué color me queda bien?*
  
  En este proyecto, vamos a poner respuesta a tan repetida pregunta. Para ello, mediante la creación de un programa, asignaremos una paleta de colores a 
  los usuarios en función de los colores de su cabello, ojos y piel. Esta asignación, estará basada en dos teorías:
  
  **TEORÍA DE LAS ESTACIONES** 🌺 ⛱ ❄️ 🍂
  
  Cada paleta de colores está asignada a una estación del año. Dentro de la carpeta 'IMG' podrás encontrar qué paleta corresponde a cada estación.
  
  **TEORÍA DE LAS CARACTERÍSTICAS** 🌡 ▼ ✨ 
  
  Después de hacer un intensivo estudio de cómo asignar cada paleta, econtramos que la empresa de asesoría de imagen "IMAGEN EXCELLENCE", considera que 
  cada color cuenta con un valor (*claro u oscuro*), una temperatura (*frío o cálido*) y un croma (*suave o brillante*) y que, en función de ello, se 
  asignará la paleta y su estación.   
 
  Por ello, debemos tener en cuenta las siguientes consideraciones:
  
  - PRIMAVERA = CÁLIDO, CLARO Y BRILLANTE
  - INVIERNO = FRÍO, CLARO Y SUAVE
  - VERANO = CÁLIDO, OSCURO Y BRILLANTE
  - OTOÑO = FRÍO, OSCURO Y BRILLANTE
  
## OBJETIVOS ##

  🎯 Crear un programa para la asignación de la paleta de colores que mejor quede al usuario. 
  
  🎯 Ser capaz de recomendar mediante el nuevo programa productos de maquillaje tales como sombras, pintalabios y colorete clasificados por paleta.
  
## PASOS SEGUIDOS ## 

  1. En primer lugar, se creó la tabla 'COMBINACIONES' utilizando los lenguages de Python y SQL. Para ello, se creó una fila para todos los posibles      
  colores de cabello, ojos y piel con sus respectivos valores, temperaturas y cromas. De esta forma, cuando la fila cumpliera con la condición de tener en 
  términos totales las características que hemos nombrado anteriormente, se asignó su paleta.
  
  2. Posteriormente, una vez teniendo todas las combinaciones, se pasó a la extracción de datos para las recomendaciones. Esta se basó en el scrapping de     las siguientes tiendas y marcas:
  
  - *PRIMOR*
  - *URBAN DECAY*
  - *HUDA BEAUTY*
  - *BENEFIT*
  - *NARS*
  - *BOBBI BROWN*
  - *KAT VON D*
  - *CHARLOTTE TILBURY* 
  - *KIKO MILANO*
  
  Siendo estas las marcas mejor valoradas para los productos que queríamos recomendar. De ellas, obtuvimos nombre de producto, precio, link de compra y       posteriormente asignamos la paleta para cada uno después de su estudio. 
  
  3. Una vez obtenidas ambas tablas, procedimos a crear el programa en Streamlit. En él, pedimos de forma interactiva al usuario que nos proporcione el 
  color de su cabello, ojos y piel, así como sus cromas (brillante = 1 solo color, suave = más de 1 color). Una vez nos da la información pedida, debe 
  hacer 'click' sobre el botón de cálculo y aparecerá su paleta, la gama de colores y una tabla donde podrá encontrar y filtrar todos los productos 
  recomendados:
  
  <img width="1345" alt="streamlit1" src="https://user-images.githubusercontent.com/115650089/207962910-231e51f2-c53c-458b-b720-2f30bd109ded.png">
  
  <img width="1281" alt="streamlit2" src="https://user-images.githubusercontent.com/115650089/207962924-662c0d2b-bc57-4768-b717-5af47ad27497.png">
  
  <img width="1282" alt="streamlit3" src="https://user-images.githubusercontent.com/115650089/207962970-4580aaae-207b-4fac-ab11-5ce265e4895a.png">

  <img width="1327" alt="streamlit4" src="https://user-images.githubusercontent.com/115650089/207962998-d96b92e2-027e-4a36-aa95-05dd07730cd4.png">

## PRÓXIMOS PASOS A SEGUIR ## 

 → Actualizar el programa creado para que éste sea capaz de detectar los colores de las facciones necesarias mediante el reconocimiento de 
 colores por cámara.
 
 → Incrementar la base de datos de productos recomendados para ofrecer la mayor variedad posible al usuario.
 
 
 → Incrementar las opciones de colores de pelo, ojos y piel para que cualquier persona pueda utilizar el programa.
 
 

  
  

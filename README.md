# PROYECTO FINAL: MAQUILLAJE EN FUNCIÓN DE LA COLORIMETRÍA / FINAL PROJECT: MAKE UP BASED ON COLORIMETRY

🇪🇸 

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
  
  2. Posteriormente, una vez teniendo todas las combinaciones, se pasó a la extracción de datos para las recomendaciones. Esta se basó en el scrapping de 
  las siguientes tiendas y marcas:
  
  - *PRIMOR*
  - *URBAN DECAY*
  - *HUDA BEAUTY*
  - *BENEFIT*
  - *NARS*
  - *BOBBI BROWN*
  - *KAT VON D*
  - *CHARLOTTE TILBURY* 
  - *KIKO MILANO*
  
  Siendo estas las marcas mejor valoradas para los productos que queríamos recomendar. De ellas, obtuvimos nombre de producto, precio, link de compra y   
  posteriormente asignamos la paleta para cada uno después de su estudio. 
  
  3. Una vez obtenidas ambas tablas, procedimos a crear el programa en Streamlit. En él, pedimos de forma interactiva al usuario que nos proporcione el 
  color de su cabello, ojos y piel, así como sus cromas (brillante = 1 solo color, suave = más de 1 color). Una vez nos da la información pedida, debe 
  hacer 'click' sobre el botón de cálculo y aparecerá su paleta, la gama de colores y una tabla donde podrá encontrar y filtrar todos los productos 
  recomendados.

## PRÓXIMOS PASOS A SEGUIR ## 

 → Actualizar el programa creado para que éste sea capaz de detectar los colores de las facciones necesarias mediante el reconocimiento de 
 colores por cámara.
 
 → Incrementar la base de datos de productos recomendados para ofrecer la mayor variedad posible al usuario.
 
 
 → Incrementar las opciones de colores de pelo, ojos y piel para que cualquier persona pueda utilizar el programa.
 
 
 🇬🇧
  
 ## ABOUT ##
 
People who wear makeup have always done themselves the same question when they have to choose their products, specifically eyeshadows palettes, lipsticks 
and blushes:

*What color suits me best?*

In this project, we will answer this common question. For that purpose, through a program development, we will able to assign a color palette to each user 
depending on their hair, eyes and skin color. I based this assignation on two theories:

**SEASONS THEORY** 🌺 ⛱ ❄️ 🍂

Each color palette is assigned to a season. In the ‘IMG’ folder you will be able to find the colors that match each season.

**FEATURES THEORY** 🌡 ▼ ✨ 

After doing a research about how to assign each palette, I found that the personal image consulting ‘IMAGEN EXCELLENCE’ considers that each color has a 
value (light or dark), a temperature (cold or warm) and a chroma (soft or bright). Using these features, the company assigns the color palettes to their 
customers, as I did in this project.

Taking into account both theories, we have the following categories:

- SPRING = WARM, LIGHT AND BRIGHT
- WINTER = COLD, LIGHT AND SOFT
- SUMMER = WARM, DARK AND BRIGHT
- AUTUMN = COLD, DARK AND BRIGHT

## GOALS ##

🎯 Creating a program to assign a color palette which suits best the user.

🎯 Make the program capable of recommending makeup products (eyeshadows palettes, lipsticks and blushes) previously classified according to the in season-
based palettes defined before.

## STEPS ##

1. Firstly, I created the ‘COMBINATIONS’ table using Python and SQL languages. For this purpose, I created a row for each hair, eyes and skin colors plus 
their respective values, temperatures and chromas. In this way, when any row fulfilled in total terms all the features mentioned, I could assign their 
palette.

2. Then, once having all the combinations possible, I extracted data for creating the  ‘RECOMMENDATIONS’ table, based on the scrapping of the following 
shops and brands:

  - *PRIMOR*
  - *URBAN DECAY*
  - *HUDA BEAUTY*
  - *BENEFIT*
  - *NARS*
  - *BOBBI BROWN*
  - *KAT VON D*
  - *CHARLOTTE TILBURY* 
  - *KIKO MILANO*

These are the best valued brands and shops for the products that I wanted to recommend. I got their names, prices and links.

3. I created a program using Streamlit. In it, we ask in an interactive way the user to choose their hair, eyes and skin color, and their chromas (bright 
= 1 color, soft = more than 1 color). Once we have the information required, the user must ‘click’ on the calculate button and their palette will appear, 
as well as the colors and a table where they can find and filter a list of recommended products.

## FOLLOWING STEPS ##

→ I am working on color detection using any device with a camera. Thus, the program will be more efficient and easier to use. 

→ I will extend the product recommendation database, in order to offer more variety for the user.

→ I will extend the options of hair, eyes and skin colors. Thus, any user will be able to use the program.

  
  <img width="1345" alt="streamlit1" src="https://user-images.githubusercontent.com/115650089/207962910-231e51f2-c53c-458b-b720-2f30bd109ded.png">
  
  <img width="1281" alt="streamlit2" src="https://user-images.githubusercontent.com/115650089/207962924-662c0d2b-bc57-4768-b717-5af47ad27497.png">
  
  <img width="1282" alt="streamlit3" src="https://user-images.githubusercontent.com/115650089/207962970-4580aaae-207b-4fac-ab11-5ce265e4895a.png">

  <img width="1327" alt="streamlit4" src="https://user-images.githubusercontent.com/115650089/207962998-d96b92e2-027e-4a36-aa95-05dd07730cd4.png">

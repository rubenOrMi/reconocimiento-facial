# Proyecto de Reconocimiento Facial con OpenCV en Python

En este proyecto, implementamos un sistema de reconocimiento facial utilizando la biblioteca OpenCV en Python. El objetivo es reconocer rostros humanos en imágenes o videos.

## Descripción del Proyecto

El proyecto consiste en:

- La captura de imágenes faciales.
- La extracción de características faciales utilizando tres algoritmos diferentes: Eigenface, Fisherface y LBPHFace.
- El entrenamiento de un modelo de reconocimiento facial utilizando las características extraídas.
- La detección y reconocimiento de rostros en tiempo real utilizando la cámara web.

## Algoritmos Utilizados

### Eigenface

El algoritmo Eigenface es una técnica de reconocimiento facial basada en PCA (Análisis de Componentes Principales). Se utiliza para reducir la dimensionalidad de las imágenes faciales y luego realizar la comparación de rostros mediante la distancia euclidiana en el espacio de características reducido.

#### Resultados
Se pudo lograr el reconocimiento pero en cierto ángulo y distancia.

<img src="https://github.com/rubenOrMi/reconocimiento-facial/assets/44560480/16d55f95-d3e3-4117-b4c1-35faff46bd7b" alt="detección rostro Ruben" width="200" height="150">

### Fisherface

El algoritmo Fisherface, también conocido como Análisis Discriminante de Fisher (FDA), es una técnica de reconocimiento facial similar a Eigenface pero que se basa en el análisis discriminante lineal. Fisherface busca maximizar la variabilidad entre las clases de rostros y minimizar la variabilidad dentro de cada clase.

#### Resultados
Con este algoritmo el reconocimiento no fue exitoso, encontrándome siempre como desconocido.

<img src="https://github.com/rubenOrMi/reconocimiento-facial/assets/44560480/a41b43e8-af77-46f9-8423-d037dcb8c60d" alt="detección rostro Ruben" width="200" height="150">

### LBPHFace

El algoritmo LBPH (Local Binary Patterns Histograms) es un método de reconocimiento facial que se basa en la textura local de las imágenes faciales. LBPHFace divide la imagen en regiones locales y calcula un descriptor basado en los patrones binarios locales de cada región. Luego, utiliza un histograma para representar la distribución de estos patrones en toda la imagen.

#### Resultados

Con este algoritmo se consiguió una mejor detección en distintos ángulos y distancias, siendo este con el que mayor facilidad se encuentra al sujeto en un ambiente con ruido. Como desventaja se observa que el reconocimiento facial provoca algo de lag en la imagen.

<img src="https://github.com/rubenOrMi/reconocimiento-facial/assets/44560480/0fa156f2-de9d-486f-b247-d87b77d302bb" alt="detección rostro Ruben" width="200" height="150">
<img src="https://github.com/rubenOrMi/reconocimiento-facial/assets/44560480/31ecd10d-9b28-4ed1-ab07-514fef103251" alt="detección rostro Ruben" width="200" height="150">


## Implementación

El proyecto se implementa en Python utilizando la biblioteca OpenCV para el procesamiento de imágenes y la implementación de los algoritmos de reconocimiento facial. Se utilizan las siguientes etapas:

1. Captura de imágenes faciales: esta fase se realiza en el archivo **capturarPersona.py** usando el algoritmo **haarcascade-frontalface_alt.xml**.
2. Preprocesamiento de imágenes (como la normalización y el ajuste de tamaño): a continuación las imágenes son tratadas para que todas tengan el mismo tamaño a través del método **resize** de **OpenCV**, realizando este proceso también en el archivo **capturarPersona.py**.
3. Extracción de características faciales utilizando los algoritmos **Eigenface**, **Fisherface** y **LBPHFace**: A continuación, tenemos tres archivos **.py** distintos para la generación de los modelos dependiendo del algoritmo a utilizar siendo los siguientes:
    * eigenface.py
    * fisherface.py
    * LBPHface.py
4. Entrenamiento del modelo de reconocimiento facial con las características extraídas: a través del método **train** se entrena el modelo en cada uno de los algoritmos seleccionados.
5. Detección y reconocimiento de rostros en tiempo real utilizando la cámara web: por último, se tienen tres archivos **.py** distintos para cada modelo, teniendo un valor numérico distinto según sea el modelo a utilizar. Los valores son los siguientes:
    * Eigenface -> 2800
    * Fisherface -> 500
    * LBPHface -> 70

## Conclusiones

En este proyecto, exploramos diferentes técnicas de reconocimiento facial utilizando OpenCV en Python. Los algoritmos Eigenface, Fisherface y LBPHFace son métodos populares y efectivos para el reconocimiento facial, cada uno con sus propias ventajas y desventajas en términos de precisión y eficiencia. La elección del algoritmo adecuado depende de los requisitos específicos de la aplicación. En este caso, el algoritmo que mejor se adaptó a las necesidades de la práctica fue, como se ha comentado anteriormente, el **LBPHFace**, ya que fue el que mejor reconocimiento facial tuvo en la realización de las distintas pruebas.

## Referencias

- [OpenCV Documentation](https://docs.opencv.org/)
- [Reconocimiento Facial con OpenCV y Python](https://realpython.com/face-recognition-with-python/)


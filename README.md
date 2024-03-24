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

### Fisherface

El algoritmo Fisherface, también conocido como Análisis Discriminante de Fisher (FDA), es una técnica de reconocimiento facial similar a Eigenface pero que se basa en el análisis discriminante lineal. Fisherface busca maximizar la variabilidad entre las clases de rostros y minimizar la variabilidad dentro de cada clase.

### LBPHFace

El algoritmo LBPH (Local Binary Patterns Histograms) es un método de reconocimiento facial que se basa en la textura local de las imágenes faciales. LBPHFace divide la imagen en regiones locales y calcula un descriptor basado en los patrones binarios locales de cada región. Luego, utiliza un histograma para representar la distribución de estos patrones en toda la imagen.

## Implementación

El proyecto se implementa en Python utilizando la biblioteca OpenCV para el procesamiento de imágenes y la implementación de los algoritmos de reconocimiento facial. Se utilizan las siguientes etapas:

1. Captura de imágenes faciales.
2. Preprocesamiento de imágenes (como la normalización y el ajuste de tamaño).
3. Extracción de características faciales utilizando los algoritmos Eigenface, Fisherface y LBPHFace.
4. Entrenamiento del modelo de reconocimiento facial con las características extraídas.
5. Detección y reconocimiento de rostros en tiempo real utilizando la cámara web.

## Conclusiones

En este proyecto, exploramos diferentes técnicas de reconocimiento facial utilizando OpenCV en Python. Los algoritmos Eigenface, Fisherface y LBPHFace son métodos populares y efectivos para el reconocimiento facial, cada uno con sus propias ventajas y desventajas en términos de precisión y eficiencia. La elección del algoritmo adecuado depende de los requisitos específicos de la aplicación.

## Referencias

- [OpenCV Documentation](https://docs.opencv.org/)
- [Reconocimiento Facial con OpenCV y Python](https://realpython.com/face-recognition-with-python/)


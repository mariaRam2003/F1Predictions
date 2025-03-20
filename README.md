# **Predicción de Carreras de F1 2025** 🏎️🏁

Este proyecto tiene como objetivo desarrollar un **modelo de aprendizaje automático** para predecir los resultados de las **carreras de la temporada 2025 de la Fórmula 1**. Utiliza datos históricos recopilados desde 1950 hasta 2024, provenientes de un dataset de Kaggle. El enfoque principal es predecir el rendimiento de los pilotos y constructores basándose en las tendencias pasadas.

## **🎯 Objetivo**

Crear un modelo de **machine learning** que prediga los resultados de las carreras de la temporada 2025 de la Fórmula 1, utilizando datos históricos sobre pilotos, equipos, resultados de calificación, tiempos por vuelta, pit stops, y otros factores.

## **🛠️ Tecnologías Utilizadas**

- **Python**: Lenguaje principal de programación.
- **Pandas**: Para la manipulación y limpieza de datos.
- **Scikit-Learn**: Para la implementación del modelo de machine learning.
- **Kaggle API**: Para la descarga del dataset desde Kaggle.
- **Miniconda**: Entorno de desarrollo para gestionar las dependencias y el ambiente de ejecución.

## **📁 Estructura del Proyecto**

El proyecto está dividido en varios archivos que realizan tareas específicas:

- **`data_loader.py`**: Este archivo contiene funciones para descargar el dataset de Kaggle y cargar los archivos CSV en **DataFrames de Pandas**.
- **`data_cleaning.py`**: Contiene el código para limpiar los datos. Reemplaza valores nulos, elimina duplicados y convierte columnas a tipos de datos adecuados.
- **`model.py`**: Aquí se entrenará el modelo de machine learning (aún por desarrollar).
- **`predictor.py`**: Este archivo será responsable de realizar las predicciones basadas en el modelo entrenado.

## **📊 Dataset**

El dataset utilizado contiene datos completos de la **Fórmula 1** desde 1950 hasta 2024, con la siguiente información:

- **Races**: Detalles sobre las carreras (fecha, lugar, circuito, etc.).
- **Drivers**: Información sobre los pilotos (nombre, nacionalidad, número, etc.).
- **Constructors**: Datos de los equipos de F1 (nombre, país, etc.).
- **Qualifying**: Información sobre las posiciones de clasificación de cada carrera.
- **Results**: Resultados de las carreras.
- **Lap Times**: Tiempos de vuelta de cada piloto durante una carrera.
- **Pit Stops**: Detalles de las paradas en pits durante las carreras.

Puedes acceder al dataset completo en [Kaggle](https://www.kaggle.com/datasets).

### **🚀 Cargar y Limpiar los Datos**

1. **Cargar Datos**: Usa `data_loader.py` para descargar el dataset de Kaggle y cargar los archivos CSV en un DataFrame de Pandas.
   
2. **Limpieza de Datos**: En `data_cleaning.py`, se realiza la limpieza de datos, eliminando valores nulos, reemplazando valores erróneos y corrigiendo tipos de datos.

### **🧹 Limpieza de Datos**

Se lleva a cabo una limpieza de los datos para asegurarse de que no haya valores faltantes ni datos erróneos. En este proceso:

1. Se reemplazan los valores `\N` por `NaN` en las columnas relevantes de los archivos `constructor_results.csv`, `drivers.csv` y `qualifying.csv`.
2. Se eliminan los registros duplicados en todos los archivos.
3. Se corrigen los tipos de datos, especialmente las columnas de fechas y números.

### **🤖 Modelo de Machine Learning**

El siguiente paso será entrenar un modelo de **machine learning** utilizando los datos de las temporadas anteriores (hasta 2024) para predecir los resultados de las carreras de la temporada 2025. Este modelo utilizará características como los tiempos de calificación, los resultados anteriores, y el rendimiento de los pilotos y constructores.

## **💻 Instalación**

### **Requisitos del Sistema**

Este proyecto está diseñado para ser ejecutado en un entorno de desarrollo con **Miniconda**.

1. Crea un entorno de Conda:
```bash
conda create --name f1-prediction python=3.8
```

2. Activa el entorno:
```bash
conda activate f1-prediction
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## **🚀Uso**
1. Descargar los datos: Ejecuta `data_loader.py` para descargar el dataset de Kaggle.

2. Limpiar los datos: Ejecuta `data_cleaning.py` para limpiar y procesar los datos del dataset.

3. Entrenamiento del modelo: Corre el script de entrenamiento del modelo para realizar las predicciones de las carreras.

## **📜 Licencia**
Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

> "Races are won at the track. Championships are won at the factory." - Mercedes (2019) 🏁
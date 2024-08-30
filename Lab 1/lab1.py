# -*- coding: utf-8 -*-
"""Lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GSmA9z6RtEa2UUQHRxtWzP8F4VYRlo0B
"""

from google.colab import drive
drive.mount('/content/drive/')

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/MyDrive/UCSP/IX CICLO/topicos de IA/'
!ls

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('creditcard_2023.csv')
# Mostrar las primeras filas para verificar la carga
df.head()

# ANÁLISIS DE DATOS
def analisis_estadistico(df):
    stats = df.describe()
    for columna in df.columns:
        if df[columna].dtype in ['int64', 'float64']:
            print(f"\nEstadísticas para {columna}:")
            print(f"Cantidad de elementos: {stats[columna]['count']}")
            print(f"Máximo: {stats[columna]['max']}")
            print(f"Mínimo: {stats[columna]['min']}")
            print(f"Promedio: {stats[columna]['mean']}")

            plt.figure(figsize=(6, 2))
            plt.hist(df[columna], bins=30)
            plt.title(f'Histograma de {columna}')
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.show()

analisis_estadistico(df)

# LIMPIEZA DE DATOS
def limpieza_datos(df):
    # Verificar datos faltantes
    datos_faltantes = df.isnull().sum()
    print("Datos faltantes por columna:")
    print(datos_faltantes)

    # Imputar datos faltantes con la media
    df_imputado = df.copy()
    for columna in df.columns:
        if df[columna].dtype in ['int64', 'float64']:
            media = df[columna].mean()
            df_imputado[columna].fillna(media, inplace=True)

    # Verificar ruido con gráfica de dispersión
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df_imputado['Amount'], df_imputado['V1'],
                          c=df_imputado['Class'], cmap='viridis',
                          edgecolors='red', linewidths=0.5, alpha=0.75)
    plt.title('Gráfica de dispersión: Amount vs V1')
    plt.xlabel('Amount')
    plt.ylabel('V1')
    plt.colorbar(scatter, label='Class')
    plt.show()

    return df_imputado

df_limpio = limpieza_datos(df)

# NORMALIZACIÓN DE DATOS
def normalizar_datos(df):
    print("\nNORMALIZACIÓN DE DATOS")
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    df_normalizado = df.copy()

    for columna in columnas_numericas:
        if columna != 'Class':  # No normalizamos la variable objetivo
            df_normalizado[columna] = (df[columna] - df[columna].min()) / (df[columna].max() - df[columna].min())

    return df_normalizado

df_normalizado = normalizar_datos(df_limpio)

# CORRELACIÓN
def calcular_correlacion(df):
    print("\nCORRELACIÓN")
    corr_matrix = df.corr()

    plt.figure(figsize=(10, 6))
    plt.imshow(corr_matrix, cmap='coolwarm', aspect='auto')
    plt.colorbar()
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.title('Matriz de Correlación')
    plt.tight_layout()
    plt.show()

    return corr_matrix

matriz_correlacion = calcular_correlacion(df_normalizado)
# Mostrar la matriz de correlación
print(matriz_correlacion)
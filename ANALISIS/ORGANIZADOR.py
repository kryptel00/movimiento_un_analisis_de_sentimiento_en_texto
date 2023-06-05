import pandas as pd
import numpy as np

# Cargar el archivo de Excel
archivo_excel = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA_STOPWORDS_NCR.xlsx"
dataframe = pd.read_excel(archivo_excel)

# Crear un diccionario para almacenar las emociones por canción
emociones_por_cancion = {}

# Iterar por cada fila del DataFrame
for index, row in dataframe.iterrows():
    cancion = row['cancion']
    emociones = row['emociones']

    # Verificar si las emociones son un valor válido o NaN
    if isinstance(emociones, str):
        emociones = emociones.split(';')  # Separar las emociones por ";"
    elif isinstance(emociones, float) and np.isnan(emociones):
        emociones = []

    # Agregar las emociones a la lista correspondiente a la canción en el diccionario
    if cancion in emociones_por_cancion:
        emociones_por_cancion[cancion].extend(emociones)
    else:
        emociones_por_cancion[cancion] = emociones

# Imprimir las emociones clasificadas por canción
for cancion, emociones in emociones_por_cancion.items():
    print("Canción:", cancion)
    print("Emociones:", emociones)
    print()

# Crear un nuevo DataFrame con las emociones clasificadas por canción
resultados_df = pd.DataFrame(emociones_por_cancion.items(), columns=['cancion', 'emociones'])

# Guardar el DataFrame en un archivo de Excel
ruta_resultados = r"C:\Users\peral\Documents\Documentos para TFG\BITACORA_4.xlsx"
resultados_df.to_excel(ruta_resultados, index=False)

import pandas as pd

# Rutas de los archivos Excel
archivo_entrada_rosalia = 'C:\\Users\\peral\\Documents\\TFG REPOSITORIO\\LETRAS\\ROSALIA_TOKENIZADA.xlsx'
archivo_entrada_diccionario = 'C:\\Users\\peral\\Documents\\TFG REPOSITORIO\\ANALISIS\\NRC.xlsx'
archivo_salida = 'C:\\Users\\peral\\Documents\\TFG REPOSITORIO\\ANALISIS\\resultado.xlsx'

# Cargar los archivos Excel
df_rosalia = pd.read_excel(archivo_entrada_rosalia)
df_diccionario = pd.read_excel(archivo_entrada_diccionario)

# Obtener las columnas relevantes del diccionario
columnas_emociones = df_diccionario.columns[11:]

# Función para buscar las emociones de una palabra
def buscar_emociones(palabra):
    emociones = []
    for _, row in df_diccionario.iterrows():
        if palabra in [row['Spanish Word'], row['English Word']]:
            emociones.extend(columna for columna in columnas_emociones if row[columna] == 1)
    return emociones

# Procesar las palabras de la hoja ROSALIA_TOKENIZADA
nuevas_filas = []
for _, row in df_rosalia.iterrows():
    palabra = row['letra']
    emociones_encontradas = buscar_emociones(palabra)
    for emocion in emociones_encontradas:
        nuevas_filas.append({'song': row['song'], 'letra': palabra, 'Emoción encontrada': emocion})

# Crear un nuevo DataFrame con los resultados
df_resultado = pd.DataFrame(nuevas_filas, columns=['song', 'letra', 'Emoción encontrada'])

# Guardar el nuevo DataFrame en un archivo Excel
df_resultado.to_excel(archivo_salida, index=False)

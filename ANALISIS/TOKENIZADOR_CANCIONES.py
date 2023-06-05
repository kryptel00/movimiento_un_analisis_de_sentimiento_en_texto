import pandas as pd
import re

# Ruta del archivo Excel de entrada y salida
archivo_entrada = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION.xlsx"
archivo_salida = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA.xlsx"

# Nombre de la columnas en el archivo Excel
columna_letra = 'letra'
columna_song = 'song'

# Cargar el archivo Excel (la primera hoja por defecto)
df = pd.read_excel(archivo_entrada)

# Función para tokenizar un párrafo en palabras
def tokenizar(parrafo):
    palabras = re.findall(r'\w+', parrafo.lower())
    return palabras

# Tokenizar los párrafos y crear un nuevo DataFrame
nuevas_filas = []
for _, row in df.iterrows():
    letras = row[columna_letra]
    song = row[columna_song]
    palabras = tokenizar(letras)
    for palabra in palabras:
        nuevas_filas.append({columna_song: song, columna_letra: palabra})

df_nuevo = pd.DataFrame(nuevas_filas)

# Guardar el nuevo DataFrame en un archivo Excel
df_nuevo.to_excel(archivo_salida, index=False)

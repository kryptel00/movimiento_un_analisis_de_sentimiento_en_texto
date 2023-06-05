import pandas as pd
import re
import spacy

# Ruta del archivo Excel de entrada y salida
archivo_entrada = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION.xlsx"
archivo_salida = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA.xlsx"

# Nombre de la columnas en el archivo Excel
columna_letra = 'letra'
columna_song = 'song'

# Cargar el archivo Excel (la primera hoja por defecto)
df = pd.read_excel(archivo_entrada)

# Cargar el modelo de SpaCy para el idioma español
nlp = spacy.load('es_core_news_sm')

# Función para tokenizar un párrafo en palabras y lematizar cada palabra
def tokenizar(parrafo):
    doc = nlp(parrafo.lower())
    lemas = [token.lemma_ for token in doc if token.is_alpha]
    return lemas

# Tokenizar los párrafos, lematizar las palabras y crear un nuevo DataFrame
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

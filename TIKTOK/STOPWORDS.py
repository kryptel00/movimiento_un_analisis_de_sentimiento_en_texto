import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar las stopwords y modelos necesarios si no están descargados
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Ruta del archivo Excel de entrada
archivo_entrada = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA.xlsx"

# Ruta del archivo Excel de salida
archivo_salida = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA_STOPWORDS.xlsx"

# Cargar el archivo Excel
df = pd.read_excel(archivo_entrada)

# Cargar las stopwords en español
stopwords_lista = stopwords.words('spanish')

# Función para filtrar las palabras stopwords y eliminar filas con palabras en inglés
def filtrar_stopwords_y_ingles(texto):
    tokens = word_tokenize(texto, language='spanish')
    tokens_filtrados = [palabra for palabra in tokens if palabra.lower() not in stopwords_lista]
    texto_filtrado = ' '.join(tokens_filtrados)
    if any("_" in palabra for palabra in tokens_filtrados):
        return None
    return texto_filtrado

# Aplicar el filtro de stopwords y eliminación de filas con palabras en inglés
df['columna_filtrada'] = df['letra'].apply(filtrar_stopwords_y_ingles)  # Reemplazar 'columna' por el nombre de la columna que deseas filtrar

# Eliminar filas donde la columna 'columna_filtrada' es nula
df = df.dropna(subset=['columna_filtrada'])

# Guardar el DataFrame filtrado en un nuevo archivo Excel
df.to_excel(archivo_salida, index=False)

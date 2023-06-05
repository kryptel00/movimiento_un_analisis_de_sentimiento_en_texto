import pandas as pd

# Cargar el archivo de Excel
archivo_excel = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA_STOPWORDS.xlsx"
dataframe = pd.read_excel(archivo_excel)

# Obtener las columnas relevantes
columnas_emociones = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']
columna_palabra = 'Palabra'
columna_spanish_word = 'Spanish Word'

# Función para buscar las emociones asociadas a una palabra
def buscar_emociones(palabra):
    emociones = []
    for i, valor in enumerate(dataframe[columna_spanish_word]):
        if valor == palabra:
            for emocion in columnas_emociones:
                if dataframe.loc[i, emocion] == 1:
                    emociones.append(emocion)
            break
    return emociones

# Analizar cada palabra y buscar las emociones asociadas
emociones_resultantes = []
for palabra in dataframe[columna_palabra]:
    emociones = buscar_emociones(palabra)
    emociones_resultantes.append(";".join(emociones))

# Agregar las emociones al DataFrame
dataframe['Emociones'] = emociones_resultantes

# Guardar el DataFrame actualizado en un nuevo archivo de Excel
ruta_resultados = r"C:\Users\peral\Documents\TFG REPOSITORIO\LLYLM\CANCION_TOKENIZADA_STOPWORDS_NCR.xlsx"
dataframe.to_excel(ruta_resultados, index=False)

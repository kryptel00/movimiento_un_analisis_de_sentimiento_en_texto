import pandas as pd

# Ruta del archivo Excel de entrada
archivo_entrada = r"C:\Users\peral\Documents\Documentos para TFG\BITACORA_4.xlsx"

# Cargar el archivo Excel
df = pd.read_excel(archivo_entrada)

# Lista de emociones a contar
emociones = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness', 'surprise', 'trust']

# Crear un diccionario para almacenar los resultados
resultados = {'Cancion': df['cancion']}

# Contar las ocurrencias de cada emoción en la columna "emocion"
for emocion in emociones:
    conteo_emocion = df['emocion'].str.count(emocion)
    resultados[emocion] = conteo_emocion

# Crear un DataFrame con los resultados
df_resultados = pd.DataFrame(resultados)

# Guardar el DataFrame en un archivo Excel
archivo_salida = r"C:\Users\peral\Documents\Documentos para TFG\LLYLM_RESULTADO.xlsx"
df_resultados.to_excel(archivo_salida, index=False)

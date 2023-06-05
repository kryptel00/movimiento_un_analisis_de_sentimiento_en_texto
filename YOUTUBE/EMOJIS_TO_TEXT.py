import pandas as pd
import emoji
import nltk
from nltk.tokenize import word_tokenize

# Ruta del archivo de entrada
ruta_entrada = input("C:\\Users\\peral\\Desktop\\COMENTARIOS_TIKTOK_TOKEN.xlsx")

# Leer el archivo de Excel de entrada
df = pd.read_excel(ruta_entrada)

# Limpia los emojis de los comentarios
df['COMENTARIO'] = df['COMENTARIO'].apply(lambda x: emoji.demojize(x))

# Tokeniza los comentarios
df['Tokens'] = df['COMENTARIO'].apply(lambda x: word_tokenize(x))

# Generar la ruta de salida del archivo de Excel
ruta_salida = ruta_entrada.split('.xlsx')[0] + '_limpio.xlsx'

# Guardar el DataFrame con los resultados en un nuevo archivo de Excel
df.to_excel(ruta_salida, index=False)

# Mensaje de finalización y ubicación del archivo de salida
print("Proceso completado. El archivo de Excel resultante se encuentra en la siguiente ubicación:")
print(ruta_salida)

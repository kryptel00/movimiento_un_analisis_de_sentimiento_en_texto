from googleapiclient.discovery import build
from openpyxl import Workbook

# Definir las credenciales de la API de YouTube
api_key = 'AIzaSyDQSE_NFO4cdjvmlyQwGLoUD549s2iCdX8'

# Definir el ID del video de YouTube del cual deseas obtener los comentarios
video_id = 'rPG4XX_X9rs'  # Video ID de "LLYLM" de Rosalía

# Crear el objeto de servicio de la API de YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

# Obtener la lista de comentarios del video
response = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=100,  # Número máximo de comentarios a obtener (puedes ajustarlo según tus necesidades)
).execute()

# Crear un archivo de Excel para almacenar los comentarios
wb = Workbook()
ws = wb.active
ws.title = 'Comentarios'
ws.append(['Autor', 'Comentario', 'Fecha'])

# Recorrer los comentarios y guardarlos en el archivo de Excel
while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        author = comment['authorDisplayName']
        text = comment['textDisplay']
        date = comment['publishedAt']
        ws.append([author, text, date])

    # Verificar si hay más páginas de comentarios disponibles
    if 'nextPageToken' in response:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            pageToken=response['nextPageToken'],
            maxResults=100
        ).execute()
    else:
        break

# Guardar el archivo de Excel
output_file = '../YOUTUBE/comentarios_rosalia.xlsx'
wb.save(output_file)

print(f"Los comentarios se han guardado correctamente en '{output_file}'.")

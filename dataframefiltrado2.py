import pandas as pd
import openpyxl
from io import BytesIO
import requests

# URL del archivo Excel en GitHub
url = 'https://github.com/lukilu123/ACGPROYECTO/raw/main/TERMOGRAFIAS.xlsx'

# Descarga el archivo Excel desde la URL
response = requests.get(url)

# Lee el archivo Excel desde la respuesta
wb = openpyxl.load_workbook(BytesIO(response.content))

# Selecciona la hoja de trabajo que deseas leer
sheet = wb.active

# Convierte la hoja de trabajo en un DataFrame
df = pd.DataFrame(sheet.values)

# Establece la primera fila como encabezados
df.columns = df.iloc[0]

# Elimina la primera fila (encabezados duplicados)
df = df.iloc[1:]

# Asegúrate de que el nombre de la columna sea exacto y sin espacios en blanco
column_name = 'MEDICION N°1 AM 26.08'  # Ajusta el nombre de la columna según corresponda

# Convierte la columna a números (ahora los valores no numéricos son NaN)
df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

# Filtra las filas en las que el valor de la columna 'MEDICION N°1 AM 26.08' sea mayor que 30
df = df[df[column_name] > 30]

# Reemplazar 'NaN' por espacios en blanco en todo el DataFrame
df = df.fillna(' ')

# Convierte el DataFrame en un archivo HTML
df.to_html('dataframe_explorable.html', index=False)

print("El DataFrame se ha convertido a HTML. Puedes encontrar el archivo 'dataframe_explorable.html' en tu directorio actual.")

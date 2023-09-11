import pandas as pd
import numpy as np

# Lee el archivo Excel, especificando que la primera fila contiene encabezados
df = pd.read_excel(r"C:\Users\diazl\Desktop\ACGPROYECTO\MATRIZFILTRADA\TERMOGRAFIAS.xlsx", header=0)

# Asegúrate de que el nombre de la columna sea exacto y sin espacios en blanco
column_name = 'MEDICION N°1 AM 26.08'  # Ajusta el nombre de la columna según corresponda

# Convierte la columna a números (ahora los valores no numéricos son NaN)
df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

# Crear una lista de columnas que deben cumplir la regla "mayor que treinta"
columnas_a_filtrar = [col for col in df.columns if not any(suffix in col for suffix in [' R', ' S', ' T'])]

# Aplicar la comparación solo a las columnas numéricas y reemplazar los valores que no cumplen con espacios en blanco
for col in columnas_a_filtrar:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: ' ' if (pd.notna(x) and isinstance(x, (int, float)) and x <= 30) else x)

# Reemplazar 'NaN' por espacios en blanco en todo el DataFrame
df = df.fillna(' ')

# Configura la opción para mostrar todas las filas verticalmente
pd.set_option('display.max_rows', None)

# Imprime el DataFrame filtrado
print(df)
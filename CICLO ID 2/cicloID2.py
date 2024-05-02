import pandas as pd

# Cargar el archivo JSON en un DataFrame de pandas
data = pd.read_json('C:/Users/Gabri/OneDrive/Documentos/U Cenfotec/Digital NAO/tweets_extraction.json')

# Exportar el DataFrame a un archivo CSV
data.to_csv('tweets.csv', index=False)

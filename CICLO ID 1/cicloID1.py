import json

archivo_json = 'tweets_extraction.json'

with open(archivo_json, 'r') as archivo:
    datos_json = archivo.read()
    
tweets = json.loads(datos_json)[:10]

#Ahora se imprimen los datos de los tweets
for tweet in tweets:
    print("ID:", tweet['id'])
    print("Texto:", tweet["texto"])
    print("Usuario:", tweet["usuario"])
    print("Hashtags:", tweet["hashtags"])
    print("Fecha:", tweet["fecha"])
    print("Retweets:", tweet["retweets"])
    print("Favoritos:", tweet["favoritos"])
    print()

# Verificar tipos de datos y estructura de datos
for tweet in tweets:
    print("Tipo de datos:")
    for key, value in tweet.items():
        print(key, ":", type(value))
    print()

# Verificar estructura de datos
print("Estructura de datos:")
print(tweets[0].keys())
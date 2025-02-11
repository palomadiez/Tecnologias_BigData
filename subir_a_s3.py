import os
import boto3

# Configuración de AWS
#AWS_ACCESS_KEY = "ASIAXEFUNO4ZNZFMLGTL"
#AWS_SECRET_KEY = "c1gsdAz9s29CtXJqSDDYDNSNAtUy7J6rQ5IctqMT"
AWS_REGION = "eu-south-2"  # Cambia esto si usas otra región
BUCKET_NAME = "cryptodataicai2025"
LOCAL_FOLDER = ""
AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEJD//////////wEaCmV1LXNvdXRoLTIiRjBEAiA6jacXcTtWGaGEQSxszC3uwKB+/DmSPDS1BY7223z42wIgXj+n2aIImonxBVQBLJWeQyDyVghn0ktintcJgEzuuNIq6QIIMhAAGgw0OTAwMDQ2NDE1ODYiDNCQnf9KZrgf/eH+1SrGArydJImzr663PBetD4WBhzCqNCIgUdbmaVlKjzPK0wWFcP42O84PFCdecX+ZOAdo9TSwWPMIXnh+yFkoeDs0SsCmPSpp3PU6XbE8+q6bgh/3Ws+Tztoo+VwkdIxW8RjARPhP02ZDlRLv19mNOUnYEnoMbluzisO523CYHIGOtx0kAsPZL6fhNb6ZO2+TzZ4z0Jwnr2OFuYU1N7zEodP8OZ2gHpBgypsU7byauoP+oYosRD2YaE+rc+cRC+R3x7pR3RphCjgJZEo2qQkz3xQRIOOauoB5JEMZxqvLS70aoX4ILB1a0hnOWNSo4J5vanV1+utldxNVxqFju+8qUE40XIiM5BqRyr7ZPMN5W+gt0Ax7fZMirUP8ff55Q+m87HVDKJkmYRJQMAiJBPBts8L75SmUjHVffklPkmG4Dr0Y18L5kmoVvksdMKCXib0GOqgBXlUZTasvXCSKksUYb9Lz4vSIgOsEoBLkabHUOtaUX5aKzFVf+CFtnfpf6HQqy8eSJX4LX8QN8YbHXgGPmL4tPfeKUle6HUMbFmA2PXcYHxdLLDadgVuhdeHBFIgff/3m42TrFXR0FckNs5RacK9HNZTAWo+fypbYNGOsNsgSZts+5Yh7xBXyh0plpctNY5ceA/OFh4g71Sp7DALAcC23ZbQlBaV1Mv4k"

monedas = {"AAVEUSD":"Aave",
           "BTCUSD": "Bitcoin",
           "ADAUSD":"Cardano",
           "DOGEUSD":"Dogecoin", 
           "ETHUSD":"Ethereum",
           "DOTUSD":"Polkadot",
           "XRPUSD":"Ripple",
           "SHIBUSD":"ShibaInu",
           "SOLUSD":"Solana",
           "XLMUSD":"Stellar"}

# Crear cliente S3 con credenciales
s3 = boto3.client(
    "s3"
)

def subir_archivos():
    for year in range(2021, 2026):  # Iteramos por los años 2021-2025
        year_folder = os.path.join(str(year))
        if not os.path.isdir(year_folder):
            print(f"⚠ La carpeta {year_folder} no existe, saltando...")
            continue

        for moneda_local in os.listdir(year_folder):  # Iteramos por cada moneda
            moneda_folder = os.path.join(year_folder, moneda_local)

            if os.path.isfile(moneda_folder):  # Asegurar que es un archivo
                s3_key = f"{year}/{monedas[moneda_local[:-4]]}/{monedas[moneda_local[:-4]]}.csv"  # Ruta en S3
                archivo = os.path.join(str(year),moneda_local)
                s3.upload_file(archivo, BUCKET_NAME, s3_key)

    print("✅ Todos los archivos han sido subidos correctamente.")

# Ejecutar la función
if __name__ == "__main__":
    subir_archivos()
import os
import boto3

AWS_REGION = "eu-south-2"  # Cambia esto si usas otra región
BUCKET_NAME = "cryptodataicai2025"
LOCAL_FOLDER = ""
aws_access_key_id="ASIAXEFUNO4ZANGQNH33"
aws_secret_access_key="51J57OOjrpymUf7FT/DI/XsP8YkP/DkTlOpRcC4U"
aws_session_token="IQoJb3JpZ2luX2VjEDgaCmV1LXNvdXRoLTIiRjBEAiAP3PzCT0xjR/KetSf1eMsy9vn8VLWfIowjkCv1peL/VQIgQcsrsZ8hEjnUHwBLC02lTF4QpmiKLi91EnK1MltTy88q8gII2v//////////ARAAGgw0OTAwMDQ2NDE1ODYiDIdtvrmmmwO0gT8v5irGAtAWrrcjCgUVYFeZdWzzcxX+WB9JbZtR0CB1BfGInBfBO3Xv4GL+9Efn2gcFDFf3M5xRBENzAQhy57Z/t+qZMEAwhv6Pr0vDtF5fbHeXicoTljChziGj9HxY+Vp3MMFJ3vbQb7N8PsHFOhFMiEy7N69bpM0AGW/FRSeh9L6IxfOuLh0x6ltutxOcZ0W2iJzjL9sR9aXAen1FgdjgZarlNGDt/6KEGXqBkkssaJgUm2eG5ipiZJ5X0WGhDVLgiqhbKwvrsnUcK654rkWzwBPG+olpua2KBconb9Vot+ttI2t5OZ/SCezlXEojFlJ7r7PMsu6mO+wSiTF7qUXTWuAhG1T4V+HQ5k/Qc+578j/h4tjxoHifV2gvasOHb03KBrQDLTPq9jquOsV2dX6nxFZUa8/xSMHkQ7mNPSj3Z1ynJmdCPoLCRbKgMK2Nrr0GOqgBq3CR9RJWsbrntscYRUxUY/c/nJSeXGSS1jPwI/ikz5Tvva6MGQ46dpSV4g9DjoYqvBTkTecFFWU2v1kjMwzOZiek93FcfowQBvZ9I59/QmLRksU/Ukj/iuz2CP/+1JaDpIFr7rXqA8ST+zJfK6C//n+XLvm/f6PR3eeCGLyiQiWLiCYkMJ6GjOfhjavbu5Po9VwvA0SB3Y0Si8+nPOApJOQAsksNohSS"

DATABASE_NAME = "trade_data_imat3a04"  # Nombre de la base de datos
CRAWLER_NAME = "trade_data_crawler_04"
S3_TARGET_PATH = "s3://cryptodataicai2025/"  # Cambia con tu bucket
IAM_ROLE = "arn:aws:iam::490004641586:role/service-role/AWSGlueServiceRole-sprint1"  # Cambia con tu rol de Glue


glue_client = boto3.client('glue', region_name=AWS_REGION,
                           aws_access_key_id = aws_access_key_id,
                           aws_secret_access_key = aws_secret_access_key,
                           aws_session_token = aws_session_token
                           )

# 1. Crear la base de datos en AWS Glue Data Catalog
def create_database():
    try:
        glue_client.create_database(
            DatabaseInput={
                'Name': DATABASE_NAME,
                'Description': 'Base de datos para almacenar metadatos de datos históricos en S3'
            }
        )
        print(f"Base de datos '{DATABASE_NAME}' creada.")
    except glue_client.exceptions.AlreadyExistsException:
        print(f"La base de datos '{DATABASE_NAME}' ya existe.")

# 2. Crear el AWS Glue Crawler
def create_crawler():
    try:
        glue_client.create_crawler(
            Name=CRAWLER_NAME,
            Role=IAM_ROLE,
            DatabaseName=DATABASE_NAME,
            Targets={'S3Targets': [{'Path': S3_TARGET_PATH}]},
            TablePrefix="trade_data_"
        )
        print(f"Crawler '{CRAWLER_NAME}' creado.")
    except glue_client.exceptions.AlreadyExistsException:
        print(f"El crawler '{CRAWLER_NAME}' ya existe.")

# 3. Ejecutar el Crawler
def start_crawler():
    glue_client.start_crawler(Name=CRAWLER_NAME)
    print(f"Crawler '{CRAWLER_NAME}' iniciado.")

# Ejecutar las funciones
create_database()
create_crawler()
start_crawler()

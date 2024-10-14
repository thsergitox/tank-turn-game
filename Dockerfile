FROM python:3.12-slim

# Establecer el directorio de trabajo en /src
WORKDIR /src

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo el contenido del directorio game al contenedor
COPY src/ .

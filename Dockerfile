FROM python:3.12-slim

# Establecer el directorio de trabajo en /src
WORKDIR /src

# Copiar los archivos de requerimientos del backend
COPY backend/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt


# Copiar todo el contenido del directorio game al contenedor
COPY backend/src/ .

#behave tests
# RUN behave

# Ejecutar pytest
# RUN python -m pytest tests/

# Comando para correr la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
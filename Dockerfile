# Usamos una imagen base de Python
FROM python:3.10-slim-bullseye

# Establecemos un directorio de trabajo
WORKDIR /app

# Mejora: Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Mejora: Evita que Python use el búfer para la salida de stdout/stderr (facilita la visualización de logs)
ENV PYTHONUNBUFFERED 1

# Copiamos los requisitos de nuestra aplicación
COPY requirements.txt requirements.txt

# Instalamos los requisitos de nuestra aplicación, solucionamos el problema con psycopg2-binary y aseguramos tener ca-certificates
RUN apt-get update && apt-get install -y libpq-dev gcc ca-certificates \
    && pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && apt-get autoremove -y gcc

# Copiamos los archivos de nuestra aplicación
COPY . .

# Indicamos el puerto en el que se expondrá la aplicación
EXPOSE 8000

# Ejecutamos nuestra aplicación con Gunicorn
CMD ["gunicorn", "-b", ":8000", "api.wsgi:application"]

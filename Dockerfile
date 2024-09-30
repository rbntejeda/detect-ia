# Utiliza la imagen base de YOLOv5
FROM ultralytics/yolov5:v7.0-cpu

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar los scripts de la aplicación a la imagen
COPY app.py .
# Instalar Flask
RUN pip install flask

# Exponer el puerto 5000 para el servicio REST
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["python3", "app.py"]

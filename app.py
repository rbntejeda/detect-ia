from flask import Flask, request, jsonify
import torch
from PIL import Image
import io

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el modelo de YOLOv5
# El modelo se puede cambiar a 'yolov5m', 'yolov5l', etc., según sea necesario.
MODEL_PATH = "yolov5s.pt"  # Cambia a tu modelo deseado
model = torch.hub.load('./', 'custom', path=MODEL_PATH, source='local', force_reload=True)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No se encontró ninguna imagen en la solicitud'}), 400

    # Obtener la imagen del request
    image_file = request.files['image'].read()
    image = Image.open(io.BytesIO(image_file))

    # Realizar la detección
    results = model(image)

    # Obtener el resultado en formato JSON
    return jsonify(results.pandas().xyxy[0].to_dict(orient="records"))

if __name__ == '__main__':
    # Ejecutar el servidor Flask en el puerto 5000
    app.run(host='0.0.0.0', port=5000)

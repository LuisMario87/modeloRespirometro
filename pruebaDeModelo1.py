from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Cargar el modelo entrenado
model = YOLO("C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\runs\\detect\\train3\\weights\\best.pt")
#Desde test Dataset completo
test_image = "C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\DatasetCompleto\\test\images\\Stone-Standardization-283_png.rf.faac1aad4202291dff13a0ebb6f953b4.jpg"

# Ruta de la imagen de prueba
#test_image = "C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\imagenesPrueba\\grafica_manual13_640x640.png"

# Realizar la detección
results = model(test_image)

# Mostrar la imagen con las detecciones
for result in results:
    result.show()  # Muestra la imagen con las predicciones

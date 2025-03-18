from ultralytics import YOLO

# Ruta al archivo data.yaml
DATA_YAML = "C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\DatasetCompleto\\data.yaml"


model = YOLO("yolov8n.pt")  

# Entrenar el modelo
model.train(
    data=DATA_YAML,
    epochs=50,  
    imgsz=640,  
    batch=8,
    augment=True,    
    device='cpu'  
)

# Guardar el modelo entrenado
trained_model_path = "C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\2doModelo\\best.pt"


model.export(format="onnx", dynamic=True)  

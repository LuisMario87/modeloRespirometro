import pandas as pd

# Ruta del archivo de métricas
results_path = "C:\\Users\\luism\\OneDrive\\Escritorio\\Modelo Pulmon\\runs\detect\\train3\\results.csv"

# Leer los resultados
df = pd.read_csv(results_path)

# Última fila tiene los valores finales del entrenamiento
print(df.tail(1)[["epoch", "metrics/precision(B)", "metrics/recall(B)", "metrics/mAP50(B)", "metrics/mAP50-95(B)"]])

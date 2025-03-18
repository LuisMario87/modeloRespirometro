import matplotlib.pyplot as plt
import math
import random
import pandas as pd

# Función para generar una respiración realista
def generar_respiracion(tiempo):
    y = []
    apnea = False  # Indica si estamos en una apnea
    duracion_apnea = 0  # Duración de la apnea actual
    for t in tiempo:
        if not apnea:
            # Base sinusoidal con amplitud variable
            amplitud = 2.8 + random.uniform(-0.5, 0.5)  # Amplitud variable
            valor = amplitud * math.sin(2 * math.pi * t / 6)  # Período de 6 segundos
            valor += random.uniform(-0.2, 0.2)  # Ruido aleatorio
            y.append(valor)
            
            # Introducir una apnea aleatoria
            if random.random() < 0.01:  # 1% de probabilidad de empezar una apnea
                apnea = True
                duracion_apnea = random.uniform(1, 3)  # Duración de la apnea (1 a 3 segundos)
        else:
            # Durante la apnea, el valor es cercano a 0
            y.append(random.uniform(-0.2, 0.2))  # Pequeñas fluctuaciones durante la apnea
            duracion_apnea -= 0.1  # Reducir la duración de la apnea
            if duracion_apnea <= 0:
                apnea = False  # Terminar la apnea
    return y

# Crear una figura con tamaño 640x640 píxeles
#plt.figure(figsize=(6.4, 6.4))  # Tamaño en pulgadas (6.4x6.4 pulgadas a 100 dpi = 640x640 píxeles)
#archivo_excel = 'C:\\Users\\luism\\\Downloads\\testReal2.xlsx'  # Cambia esto por la ruta de tu archivo Excel
#df = pd.read_excel(archivo_excel)
# Datos manuales
x = x = [i * 0.1 for i in range(60001)]  # Valores de 0.0 a 60.0 en pasos de 0.1# Valores de tiempo (eje X)


y = generar_respiracion(x) # Simula una respiración con un período de 6 segundos# Valores correspondientes (eje Y)
#x = df['X']
#y = df['Y']
# Crear la gráfica con una línea continua y sin marcadores
plt.plot(x, y, linestyle='-', color='b', linewidth=2)  # Línea continua azul

# Ajustar los límites y los intervalos de los ejes
plt.xlim(0, 60)  # Límites del eje X (tiempo)
plt.ylim(-3, 3)  # Límites del eje Y (valores)
plt.xticks([0, 15, 30, 45, 60])  # Marcas en el eje X
plt.yticks([-3, -2, -1, 0, 1, 2, 3])  # Marcas en el eje Y

# Añadir título y etiquetas
plt.title('230609 Stone 273', fontsize=14)
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Standardization Value', fontsize=12)

# Guardar la gráfica como imagen
plt.savefig('grafica_manual12_640x640.png', dpi=100)  # Guardar con resolución de 100 dpi para obtener 640x640 píxeles

# Mostrar la gráfica
plt.show()
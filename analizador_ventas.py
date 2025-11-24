import pandas as pd

# Cargar datos
df = pd.read_csv('ventas.csv')

# Calcular métricas
promedio_ventas = df['ventas'].mean()
print(f"Promedio de ventas: {promedio_ventas}")

# Función para detectar outliers por producto
def detectar_outliers_por_producto(dataframe):
    ventas_producto = df[df['producto'] == producto]['ventas']
    media = ventas_producto.mean()
    desviacion_estandar = ventas_producto.std()
    limite_inferior = media - 3 * desviacion_estandar
    limite_superior = media + 3 * desviacion_estandar
    outliers = ventas_producto[(ventas_producto < limite_inferior) | (ventas_producto > limite_superior)]
    return outliers
    
    

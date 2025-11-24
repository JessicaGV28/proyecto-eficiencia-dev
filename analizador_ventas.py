import pandas as pd

# Cargar datos
df = pd.read_csv('ventas.csv')

# Calcular métricas
promedio_ventas = df['ventas'].mean()
print(f"Promedio de ventas: {promedio_ventas}")


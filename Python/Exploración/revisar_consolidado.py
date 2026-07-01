import pandas as pd

df = pd.read_csv("Datos/sinim_ingresos_consolidado.csv")

print(df.shape)

print("\nPrimeras 30 columnas:")
print(df.columns[:30].tolist())

print("\nPrimeras 5 filas:")
print(df.head())
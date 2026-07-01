from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

RUTA_SINIM = BASE_DIR / "Datos" / "Datos municipales (SINIM)"
SALIDA = BASE_DIR / "Datos" / "inventario_sinim.csv"

registros = []

for carpeta in RUTA_SINIM.iterdir():
    if carpeta.is_dir():
        categoria = carpeta.name

        for archivo in carpeta.glob("*.xlsx"):
            try:
                df = pd.read_excel(archivo, nrows=10, header=None)

                registros.append({
                    "categoria": categoria,
                    "archivo": archivo.name,
                    "ruta": str(archivo),
                    "filas_muestra": df.shape[0],
                    "columnas_muestra": df.shape[1],
                    "error": ""
                })

            except Exception as e:
                registros.append({
                    "categoria": categoria,
                    "archivo": archivo.name,
                    "ruta": str(archivo),
                    "filas_muestra": None,
                    "columnas_muestra": None,
                    "error": str(e)
                })

inventario = pd.DataFrame(registros)
inventario.to_csv(SALIDA, index=False, encoding="utf-8-sig")

print("Inventario generado en:")
print(SALIDA)

print("\nResumen:")
print(inventario)
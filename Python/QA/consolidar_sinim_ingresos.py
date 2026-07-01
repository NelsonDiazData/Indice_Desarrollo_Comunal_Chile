from pathlib import Path
import pandas as pd
import re

BASE_DIR = Path(__file__).resolve().parents[1]
RUTA_SINIM = BASE_DIR / "Datos" / "Datos municipales (SINIM)"
SALIDA = BASE_DIR / "Datos" / "sinim_ingresos_consolidado.csv"

CATEGORIAS = [
    "Ingresos Educación",
    "Ingresos Municipales",
    "Ingresos Salud"
]

def extraer_anio(nombre_archivo):
    match = re.search(r"(20\d{2})", nombre_archivo)
    return int(match.group(1)) if match else None

def limpiar_columnas(cols):
    nuevas = []
    for col in cols:
        col = str(col).strip()
        col = re.sub(r"\s+", " ", col)
        nuevas.append(col)
    return nuevas

registros = []

for categoria in CATEGORIAS:
    carpeta = RUTA_SINIM / categoria

    for archivo in sorted(carpeta.glob("*.xlsx")):
        anio = extraer_anio(archivo.name)

        print(f"Leyendo: {categoria} - {archivo.name}")

        try:
            df = pd.read_excel(archivo, header=4)
            df.columns = limpiar_columnas(df.columns)

            # Eliminar filas tipo "Región de ..."
            if "Código" in df.columns:
                df = df[pd.to_numeric(df["Código"], errors="coerce").notna()]
            else:
                print(f"ADVERTENCIA: no encontré columna Código en {archivo.name}")
                continue

            df["anio"] = anio
            df["categoria"] = categoria
            df["archivo_origen"] = archivo.name

            registros.append(df)

        except Exception as e:
            print(f"ERROR leyendo {archivo.name}: {e}")

consolidado = pd.concat(registros, ignore_index=True, sort=False)

consolidado.to_csv(SALIDA, index=False, encoding="utf-8-sig")

print("\nConsolidado generado:")
print(SALIDA)

print("\nShape final:")
print(consolidado.shape)

print("\nColumnas finales:")
print(len(consolidado.columns))

print("\nRegistros por categoría y año:")
print(consolidado.groupby(["categoria", "anio"]).size())
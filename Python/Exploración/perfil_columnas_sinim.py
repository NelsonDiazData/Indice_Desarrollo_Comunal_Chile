from pathlib import Path
import pandas as pd
import re

BASE_DIR = Path(__file__).resolve().parents[1]
RUTA_SINIM = BASE_DIR / "Datos" / "Datos municipales (SINIM)"
SALIDA = BASE_DIR / "Datos" / "perfil_columnas_sinim.csv"

def extraer_anio(nombre_archivo):
    match = re.search(r"(20\d{2})", nombre_archivo)
    return int(match.group(1)) if match else None

registros = []

for carpeta in RUTA_SINIM.iterdir():
    if not carpeta.is_dir():
        continue

    categoria = carpeta.name

    for archivo in carpeta.glob("*.xlsx"):
        anio = extraer_anio(archivo.name)

        try:
            df = pd.read_excel(archivo, header=None, nrows=8)

            for i, fila in df.iterrows():
                valores = [str(x).strip() for x in fila.tolist() if pd.notna(x)]

                registros.append({
                    "categoria": categoria,
                    "archivo": archivo.name,
                    "anio": anio,
                    "fila_excel": i + 1,
                    "cantidad_valores_no_nulos": len(valores),
                    "primeros_valores": " | ".join(valores[:12])
                })

        except Exception as e:
            registros.append({
                "categoria": categoria,
                "archivo": archivo.name,
                "anio": anio,
                "fila_excel": None,
                "cantidad_valores_no_nulos": None,
                "primeros_valores": "",
                "error": str(e)
            })

perfil = pd.DataFrame(registros)
perfil.to_csv(SALIDA, index=False, encoding="utf-8-sig")

print("Perfil generado en:")
print(SALIDA)

print("\nPrimeras filas del perfil:")
print(perfil.head(40))
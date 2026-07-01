from pathlib import Path
import re
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

RUTA_DATOS = BASE_DIR / "Datos"
RUTA_SINIM = RUTA_DATOS / "Datos municipales (SINIM)"
RUTA_CATALOGO = RUTA_DATOS / "catalogo_indicadores_sinim.csv"

SALIDA = RUTA_DATOS / "sinim_indicadores_consolidado.csv"

CARPETAS = {
    "Educacion": "Ingresos Educación",
    "Municipal": "Ingresos Municipales",
    "Salud": "Ingresos Salud",
}

COLUMNAS_BASE = ["Código", "Comuna", "Sector", "Trimestre"]


def extraer_anio(nombre_archivo: str) -> int | None:
    match = re.search(r"(20\d{2})", nombre_archivo)
    return int(match.group(1)) if match else None


def normalizar_codigo(codigo):
    if pd.isna(codigo):
        return None
    return str(codigo).strip()


def limpiar_valor(valor):
    if pd.isna(valor):
        return 0
    if isinstance(valor, str):
        valor = valor.strip()
        if valor.lower() in ["sin servicio", ""]:
            return 0
        valor = valor.replace(".", "").replace(",", ".")
    try:
        return float(valor)
    except Exception:
        return 0


catalogo = pd.read_csv(RUTA_CATALOGO)
catalogo["codigo_indicador"] = catalogo["codigo_indicador"].apply(normalizar_codigo)

registros = []

for sector, carpeta_nombre in CARPETAS.items():
    carpeta = RUTA_SINIM / carpeta_nombre
    catalogo_sector = catalogo[catalogo["sector"] == sector]

    for archivo in sorted(carpeta.glob("*.xlsx")):
        anio = extraer_anio(archivo.name)
        print(f"Leyendo {sector} - {anio} - {archivo.name}")

        # Fila 4 Excel = códigos -> header=None, row index 3
        codigos = pd.read_excel(archivo, header=None, nrows=4).iloc[3].tolist()
        codigos = [normalizar_codigo(c) for c in codigos]

        # Fila 5 Excel = nombres columnas reales -> header=4
        df = pd.read_excel(archivo, header=4)

        # Eliminar filas de región y filas no comunales
        df = df[pd.to_numeric(df["Código"], errors="coerce").notna()].copy()

        for _, indicador in catalogo_sector.iterrows():
            codigo_objetivo = indicador["codigo_indicador"]
            nombre_indicador = indicador["nombre_indicador"]

            posiciones = [
                i for i, c in enumerate(codigos)
                if c == codigo_objetivo
            ]

            if not posiciones:
                print(f"  ADVERTENCIA: no encontrado {codigo_objetivo} en {archivo.name}")
                continue

            pos = posiciones[0]
            columna_valor = df.columns[pos]

            temp = df[COLUMNAS_BASE].copy()
            temp["anio"] = anio
            temp["sector_modelo"] = sector
            temp["codigo_indicador"] = codigo_objetivo
            temp["indicador"] = nombre_indicador
            temp["valor"] = df[columna_valor].apply(limpiar_valor)
            temp["archivo_origen"] = archivo.name

            temp = temp.rename(columns={
                "Código": "codigo_comuna",
                "Comuna": "comuna",
                "Sector": "sector_origen",
                "Trimestre": "trimestre"
            })

            registros.append(temp)

consolidado = pd.concat(registros, ignore_index=True)

consolidado = consolidado[
    [
        "anio",
        "codigo_comuna",
        "comuna",
        "sector_modelo",
        "sector_origen",
        "trimestre",
        "codigo_indicador",
        "indicador",
        "valor",
        "archivo_origen"
    ]
]

consolidado.to_csv(SALIDA, index=False, encoding="utf-8-sig")

print("\nConsolidado generado:")
print(SALIDA)

print("\nShape:")
print(consolidado.shape)

print("\nRegistros por sector:")
print(consolidado.groupby("sector_modelo").size())

print("\nRegistros por año y sector:")
print(consolidado.groupby(["sector_modelo", "anio"]).size())
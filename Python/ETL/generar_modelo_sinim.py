from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq

BASE_DIR = Path(__file__).resolve().parents[2]

RUTA_DATOS = BASE_DIR / "Datos"
RUTA_CENSO = RUTA_DATOS / "Datos Censo 2024"
RUTA_SINIM = RUTA_DATOS / "Staging" / "sinim_indicadores_consolidado.csv"

SALIDA_DIM_COMUNA = RUTA_DATOS / "Modelo" / "dim_comuna.csv"
SALIDA_DIM_INDICADOR = RUTA_DATOS / "Modelo" / "dim_indicador.csv"
SALIDA_FACT_INGRESOS = RUTA_DATOS / "Modelo" / "fact_ingresos_sinim.csv"


def generar_dim_comuna():
    archivo_censo = RUTA_CENSO / "viviendas_censo2024.parquet"

    columnas = ["region", "provincia", "comuna"]

    tabla = pq.read_table(archivo_censo, columns=columnas)
    df_censo = tabla.to_pandas()

    dim = (
        df_censo.drop_duplicates()
        .rename(columns={
            "region": "codigo_region",
            "provincia": "codigo_provincia",
            "comuna": "codigo_comuna"
        })
    )

    sinim = pd.read_csv(RUTA_SINIM)

    nombres_comuna = (
        sinim[sinim["codigo_comuna"] != 11111][["codigo_comuna", "comuna"]]
        .drop_duplicates()
        .sort_values(["codigo_comuna", "comuna"])
        .groupby("codigo_comuna", as_index=False)
        .first()
        .rename(columns={"comuna": "nombre_comuna"})
    )

    nombres_comuna = nombres_comuna[nombres_comuna["codigo_comuna"] != 11111]

    dim = dim.merge(
        nombres_comuna,
        on="codigo_comuna",
        how="left"
    )

    regiones = pd.DataFrame([
        [1, "Tarapacá"],
        [2, "Antofagasta"],
        [3, "Atacama"],
        [4, "Coquimbo"],
        [5, "Valparaíso"],
        [6, "Libertador General Bernardo O'Higgins"],
        [7, "Maule"],
        [8, "Biobío"],
        [9, "La Araucanía"],
        [10, "Los Lagos"],
        [11, "Aysén del General Carlos Ibáñez del Campo"],
        [12, "Magallanes y de la Antártica Chilena"],
        [13, "Metropolitana de Santiago"],
        [14, "Los Ríos"],
        [15, "Arica y Parinacota"],
        [16, "Ñuble"],
    ], columns=["codigo_region", "nombre_region"])

    dim = dim.merge(
        regiones,
        on="codigo_region",
        how="left"
    )

    dim = dim[
        [
            "codigo_comuna",
            "nombre_comuna",
            "codigo_provincia",
            "codigo_region",
            "nombre_region"
        ]
    ].sort_values(["codigo_region", "codigo_provincia", "codigo_comuna"])

    dim.to_csv(SALIDA_DIM_COMUNA, index=False, encoding="utf-8-sig")

    print("Dim_Comuna generada:")
    print(SALIDA_DIM_COMUNA)
    print(dim.shape)


def generar_dim_indicador_y_fact():
    df = pd.read_csv(RUTA_SINIM)

    df = df[df["codigo_comuna"] != 11111].copy()

    dim_indicador = (
        df[[
            "sector_modelo",
            "codigo_indicador",
            "indicador"
        ]]
        .drop_duplicates()
        .sort_values(["sector_modelo", "codigo_indicador"])
    )

    dim_indicador.to_csv(SALIDA_DIM_INDICADOR, index=False, encoding="utf-8-sig")

    fact = df[[
        "anio",
        "codigo_comuna",
        "sector_modelo",
        "codigo_indicador",
        "valor"
    ]].copy()

    fact.to_csv(SALIDA_FACT_INGRESOS, index=False, encoding="utf-8-sig")

    print("\nDim_Indicador generada:")
    print(SALIDA_DIM_INDICADOR)
    print(dim_indicador.shape)

    print("\nFact_Ingresos generada:")
    print(SALIDA_FACT_INGRESOS)
    print(fact.shape)


if __name__ == "__main__":
    generar_dim_comuna()
    generar_dim_indicador_y_fact()
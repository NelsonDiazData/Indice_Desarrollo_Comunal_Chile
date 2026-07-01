from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq

BASE_DIR = Path(__file__).resolve().parents[2]

RUTA_DATOS = BASE_DIR / "Datos"
RUTA_CENSO = RUTA_DATOS / "Datos Censo 2024"
RUTA_MODELO = RUTA_DATOS / "Modelo"

SALIDA_PERSONAS = RUTA_MODELO / "fact_censo_personas_comunal.csv"
SALIDA_HOGARES = RUTA_MODELO / "fact_censo_hogares_comunal.csv"
SALIDA_VIVIENDAS = RUTA_MODELO / "fact_censo_viviendas_comunal.csv"


def porcentaje_valido(serie, condicion):
    total_validos = serie.notna().sum()
    if total_validos == 0:
        return pd.NA
    return condicion.sum() / total_validos * 100


def agregar_personas():
    archivo = RUTA_CENSO / "personas_censo2024.parquet"

    columnas = [
        "comuna",
        "edad",
        "discapacidad",
        "escolaridad",
        "p37_alfabet"
    ]

    tabla = pq.read_table(archivo, columns=columnas)
    df = tabla.to_pandas()

    df["edad"] = df["edad"].replace(-66, pd.NA)
    df["escolaridad"] = df["escolaridad"].replace(-99, pd.NA)
    df["discapacidad"] = df["discapacidad"].replace(-99, pd.NA)
    df["p37_alfabet"] = df["p37_alfabet"].replace(-99, pd.NA)

    df = df.rename(columns={"comuna": "codigo_comuna"})

    agg = (
        df.groupby("codigo_comuna")
        .agg(
            poblacion_total=("codigo_comuna", "size"),
            promedio_edad=("edad", "mean"),
            porcentaje_menores_15=("edad", lambda x: porcentaje_valido(x, x < 15)),
            porcentaje_adultos_mayores=("edad", lambda x: porcentaje_valido(x, x >= 65)),
            porcentaje_discapacidad=("discapacidad", lambda x: porcentaje_valido(x, x == 1)),
            promedio_escolaridad=("escolaridad", "mean"),
            porcentaje_alfabetizacion=("p37_alfabet", lambda x: porcentaje_valido(x, x == 1)),
        )
        .reset_index()
        .sort_values("codigo_comuna")
    )

    agg.to_csv(SALIDA_PERSONAS, index=False, encoding="utf-8-sig")

    print("Fact Censo Personas Comunal generada:")
    print(SALIDA_PERSONAS)
    print(agg.shape)

    return agg


def agregar_hogares():
    archivo = RUTA_CENSO / "hogares_censo2024.parquet"

    columnas = [
        "comuna",
        "p15b_serv_compu",
        "p15d_serv_internet_fija",
        "p15e_serv_internet_movil"
    ]

    tabla = pq.read_table(archivo, columns=columnas)
    df = tabla.to_pandas()

    df = df.rename(columns={"comuna": "codigo_comuna"})

    agg = (
        df.groupby("codigo_comuna")
        .agg(
            total_hogares=("codigo_comuna", "size"),
            porcentaje_computador=("p15b_serv_compu", lambda x: (x == 1).mean() * 100),
            porcentaje_internet_fija=("p15d_serv_internet_fija", lambda x: (x == 1).mean() * 100),
            porcentaje_internet_movil=("p15e_serv_internet_movil", lambda x: (x == 1).mean() * 100),
        )
        .reset_index()
        .sort_values("codigo_comuna")
    )

    agg.to_csv(SALIDA_HOGARES, index=False, encoding="utf-8-sig")

    print("\nFact Censo Hogares Comunal generada:")
    print(SALIDA_HOGARES)
    print(agg.shape)

    return agg


def agregar_viviendas():
    archivo = RUTA_CENSO / "viviendas_censo2024.parquet"

    columnas = [
        "comuna",
        "cant_per",
        "indice_hacinamiento",
        "p6_fuente_agua",
        "p8_serv_hig",
        "p9_fuente_elect"
    ]

    tabla = pq.read_table(archivo, columns=columnas)
    df = tabla.to_pandas()

    df = df.rename(columns={"comuna": "codigo_comuna"})

    agg = (
        df.groupby("codigo_comuna")
        .agg(
            total_viviendas=("codigo_comuna", "size"),
            promedio_personas_vivienda=("cant_per", "mean"),
            porcentaje_hacinamiento=("indice_hacinamiento", lambda x: (x > 1).mean() * 100),
            porcentaje_agua_red=("p6_fuente_agua", lambda x: (x == 1).mean() * 100),
            porcentaje_saneamiento=("p8_serv_hig", lambda x: (x == 1).mean() * 100),
            porcentaje_electricidad=("p9_fuente_elect", lambda x: (x == 1).mean() * 100),
        )
        .reset_index()
        .sort_values("codigo_comuna")
    )

    agg.to_csv(SALIDA_VIVIENDAS, index=False, encoding="utf-8-sig")

    print("\nFact Censo Viviendas Comunal generada:")
    print(SALIDA_VIVIENDAS)
    print(agg.shape)

    return agg


def generar_modelo_censo():
    print("Agregando personas...")
    agregar_personas()

    print("\nAgregando hogares...")
    agregar_hogares()

    print("\nAgregando viviendas...")
    agregar_viviendas()

    print("\nProceso Censo finalizado.")


if __name__ == "__main__":
    generar_modelo_censo()
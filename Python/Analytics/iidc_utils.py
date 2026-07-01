import pandas as pd

from Utils.config import ANIO_INDICE
from Utils.database import escribir_sql, leer_sql


def obtener_dataset_iidc() -> pd.DataFrame:
    query = f"""
    SELECT *
    FROM fact.vw_indice_desarrollo_historico
    WHERE anio = {ANIO_INDICE}
    """

    df = leer_sql(query)

    df["nombre_region"] = (
        df["nombre_region"]
        .astype(str)
        .str.replace("\r", "", regex=False)
        .str.strip()
    )

    print("Dataset IIDC cargado:")
    print(df.shape)

    return df


def validar_dataset_iidc(df: pd.DataFrame) -> pd.DataFrame:
    print("\n" + "=" * 70)
    print("VALIDACIÓN DATASET IIDC")
    print("=" * 70)

    print(f"Filas: {len(df):,}")
    print(f"Columnas: {len(df.columns):,}")

    print("\nDuplicados exactos:")
    print(df.duplicated().sum())

    print("\nDuplicados por codigo_comuna:")
    print(df["codigo_comuna"].duplicated().sum())

    print("\nValores nulos:")
    print(df.isna().sum())

    print("\nAños disponibles:")
    print(df["anio"].unique())

    print("\nRegiones:")
    print(df["nombre_region"].sort_values().unique())

    return df


def seleccionar_variables_iidc(df: pd.DataFrame) -> pd.DataFrame:
    columnas = [
        "anio",
        "codigo_comuna",
        "nombre_comuna",
        "codigo_region",
        "nombre_region",
        "poblacion_total",

        "ingresos_municipales",
        "ingresos_educacion",
        "ingresos_salud",

        "promedio_escolaridad",
        "porcentaje_alfabetizacion",

        "porcentaje_agua_red",
        "porcentaje_saneamiento",
        "porcentaje_electricidad",
        "porcentaje_hacinamiento",
        "promedio_personas_vivienda",

        "porcentaje_computador",
        "porcentaje_internet_fija",
        "porcentaje_internet_movil",
    ]

    df_iidc = df[columnas].copy()

    print("\nVariables seleccionadas para IIDC:")
    print(df_iidc.shape)
    print(df_iidc.columns.tolist())

    
    return df_iidc

def transformar_variables_iidc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["ingresos_municipales_pc"] = (
        df["ingresos_municipales"] / df["poblacion_total"]
    )

    df["ingresos_educacion_pc"] = (
        df["ingresos_educacion"] / df["poblacion_total"]
    )

    df["ingresos_salud_pc"] = (
        df["ingresos_salud"] / df["poblacion_total"]
    )

    print("\nVariables derivadas creadas:")
    print([
        "ingresos_municipales_pc",
        "ingresos_educacion_pc",
        "ingresos_salud_pc"
    ])

    print("\nVista previa ingresos per cápita:")
    print(
        df[
            [
                "codigo_comuna",
                "nombre_comuna",
                "poblacion_total",
                "ingresos_municipales_pc",
                "ingresos_educacion_pc",
                "ingresos_salud_pc",
            ]
        ].head()
    )

    return df

def normalizar_minmax(serie: pd.Series) -> pd.Series:
    minimo = serie.min()
    maximo = serie.max()

    if maximo == minimo:
        return pd.Series(0, index=serie.index)

    return ((serie - minimo) / (maximo - minimo)) * 100


def normalizar_variables_iidc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    variables_positivas = [
        "ingresos_municipales_pc",
        "ingresos_educacion_pc",
        "ingresos_salud_pc",
        "promedio_escolaridad",
        "porcentaje_alfabetizacion",
        "porcentaje_agua_red",
        "porcentaje_saneamiento",
        "porcentaje_electricidad",
        "porcentaje_computador",
        "porcentaje_internet_fija",
        "porcentaje_internet_movil",
    ]

    variables_negativas = [
        "porcentaje_hacinamiento",
        "promedio_personas_vivienda",
    ]

    for columna in variables_positivas:
        df[f"{columna}_norm"] = normalizar_minmax(df[columna])

    for columna in variables_negativas:
        df[f"{columna}_inv"] = df[columna].max() - df[columna]
        df[f"{columna}_norm"] = normalizar_minmax(df[f"{columna}_inv"])

    print("\nVariables normalizadas creadas.")
    print("Columnas actuales:", len(df.columns))

    return df


def calcular_dimensiones_iidc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["score_economico"] = df[
        [
            "ingresos_municipales_pc_norm",
            "ingresos_educacion_pc_norm",
            "ingresos_salud_pc_norm",
        ]
    ].mean(axis=1)

    df["score_capital_humano"] = df[
        [
            "promedio_escolaridad_norm",
            "porcentaje_alfabetizacion_norm",
        ]
    ].mean(axis=1)

    df["score_infraestructura"] = df[
        [
            "porcentaje_agua_red_norm",
            "porcentaje_saneamiento_norm",
            "porcentaje_electricidad_norm",
        ]
    ].mean(axis=1)

    df["score_habitabilidad"] = df[
        [
            "porcentaje_hacinamiento_norm",
            "promedio_personas_vivienda_norm",
        ]
    ].mean(axis=1)

    df["score_conectividad"] = df[
        [
            "porcentaje_computador_norm",
            "porcentaje_internet_fija_norm",
            "porcentaje_internet_movil_norm",
        ]
    ].mean(axis=1)

    print("\nScores por dimensión creados:")
    print([
        "score_economico",
        "score_capital_humano",
        "score_infraestructura",
        "score_habitabilidad",
        "score_conectividad",
    ])

    return df


def calcular_iidc(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["iidc"] = df[
        [
            "score_economico",
            "score_capital_humano",
            "score_infraestructura",
            "score_habitabilidad",
            "score_conectividad",
        ]
    ].mean(axis=1)

    df["ranking_iidc"] = df["iidc"].rank(
        ascending=False,
        method="dense"
    ).astype(int)

    df["percentil_iidc"] = df["iidc"].rank(
        pct=True
    ) * 100

    def categorizar(valor):
        if valor >= 80:
            return "Muy alto"
        elif valor >= 65:
            return "Alto"
        elif valor >= 50:
            return "Medio"
        elif valor >= 35:
            return "Bajo"
        else:
            return "Crítico"

    df["categoria_iidc"] = df["iidc"].apply(categorizar)

    print("\nIIDC calculado.")
    print("\nTop 10 comunas por IIDC:")
    print(
        df[
            [
                "ranking_iidc",
                "codigo_comuna",
                "nombre_comuna",
                "nombre_region",
                "iidc",
                "categoria_iidc",
            ]
        ]
        .sort_values("ranking_iidc")
        .head(10)
    )

    return df


def exportar_dataset_iidc(df: pd.DataFrame) -> pd.DataFrame:
    ruta_salida = "Datos/Final/iidc_final.csv"

    df.to_csv(
        ruta_salida,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nDataset IIDC exportado correctamente en: {ruta_salida}")

    return df

def cargar_iidc_sql(df):

    escribir_sql(
        df=df,
        nombre_tabla="iidc_comunal",
        esquema="mart"
    )

    return df
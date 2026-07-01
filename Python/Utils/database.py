import pandas as pd
from sqlalchemy import create_engine
from Utils.config import SQL_SERVER, SQL_DATABASE


def crear_conexion():
    connection_string = (
        f"mssql+pyodbc://@{SQL_SERVER}/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)


def leer_sql(query: str) -> pd.DataFrame:
    engine = crear_conexion()

    with engine.connect() as conn:
        df = pd.read_sql(query, conn)

    return df

def escribir_sql(
    df: pd.DataFrame,
    nombre_tabla: str,
    esquema: str = "dbo",
    if_exists: str = "replace",
):
    """
    Escribe un DataFrame en SQL Server.
    """

    engine = crear_conexion()

    df.to_sql(
        name=nombre_tabla,
        con=engine,
        schema=esquema,
        if_exists=if_exists,
        index=False,
    )

    print(
        f"\nTabla [{esquema}].[{nombre_tabla}] cargada correctamente."
    )
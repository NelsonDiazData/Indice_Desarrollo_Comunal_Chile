from pathlib import Path
import json
import pandas as pd

from Utils.database import leer_sql


BASE_DIR = Path(__file__).resolve().parents[2]
RUTA_GEOJSON = BASE_DIR / "Datos" / "Geografia" / "chile_comunas.geojson"


def validar_mapa_comunas():
    with open(RUTA_GEOJSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    codigos_mapa = []

    for feature in data["features"]:
        codigo = feature["properties"].get("codigo_comuna")
        codigos_mapa.append(str(codigo).zfill(5))

    df_mapa = pd.DataFrame({"codigo_comuna_mapa": codigos_mapa}).drop_duplicates()

    query = """
    SELECT DISTINCT codigo_comuna
    FROM mart.iidc_comunal
    """

    df_iidc = leer_sql(query)
    df_iidc["codigo_comuna_mapa"] = (
        df_iidc["codigo_comuna"]
        .astype(int)
        .astype(str)
        .str.zfill(5)
    )

    codigos_geo = set(df_mapa["codigo_comuna_mapa"])
    codigos_iidc = set(df_iidc["codigo_comuna_mapa"])

    faltan_en_mapa = sorted(codigos_iidc - codigos_geo)
    sobran_en_mapa = sorted(codigos_geo - codigos_iidc)

    print("\n" + "=" * 70)
    print("VALIDACIÓN CARTOGRÁFICA")
    print("=" * 70)

    print(f"Comunas en GeoJSON ............. {len(codigos_geo)}")
    print(f"Comunas en MART_IIDC ........... {len(codigos_iidc)}")
    print(f"Coincidencias .................. {len(codigos_geo & codigos_iidc)}")

    if not faltan_en_mapa and not sobran_en_mapa:
        print("\nEstado .......................... OK ✓")
    else:
        print("\nEstado .......................... ERROR")

        print("\nComunas faltantes en GeoJSON:")
        print(faltan_en_mapa)

        print("\nComunas sobrantes en GeoJSON:")
        print(sobran_en_mapa)


if __name__ == "__main__":
    validar_mapa_comunas()
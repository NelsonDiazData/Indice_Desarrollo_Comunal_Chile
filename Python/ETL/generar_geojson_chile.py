from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parents[2]
RUTA_GEOGRAFIA = BASE_DIR / "Datos" / "Geografia"

ARCHIVO_SALIDA = RUTA_GEOGRAFIA / "chile_comunas.geojson"


def generar_geojson_chile():
    features = []

    for i in range(1, 17):
        archivo = RUTA_GEOGRAFIA / f"r{i:02d}.geojson"

        print(f"Leyendo {archivo.name}...")

        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        features.extend(data["features"])

    geojson_chile = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        json.dump(geojson_chile, f, ensure_ascii=False)

    print("\nGeoJSON nacional generado correctamente.")
    print(f"Archivo: {ARCHIVO_SALIDA}")
    print(f"Total comunas: {len(features)}")


if __name__ == "__main__":
    generar_geojson_chile()
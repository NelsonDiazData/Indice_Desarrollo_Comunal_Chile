from pathlib import Path
import requests

BASE_DIR = Path(__file__).resolve().parents[2]
RUTA_GEOGRAFIA = BASE_DIR / "Datos" / "Geografia"
RUTA_GEOGRAFIA.mkdir(parents=True, exist_ok=True)

BASE_URL = (
    "https://raw.githubusercontent.com/"
    "pachadotdev/chilemapas/master/data_geojson/comunas"
)

def descargar_geojson_comunas():
    for i in range(1, 17):
        codigo_region = f"r{i:02d}"
        nombre_archivo = f"{codigo_region}.geojson"
        url = f"{BASE_URL}/{nombre_archivo}"
        ruta_salida = RUTA_GEOGRAFIA / nombre_archivo

        print(f"Descargando {nombre_archivo}...")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        ruta_salida.write_text(response.text, encoding="utf-8")

        print(f"Guardado en: {ruta_salida}")

    print("\nDescarga de mapas comunales finalizada.")

if __name__ == "__main__":
    descargar_geojson_comunas()
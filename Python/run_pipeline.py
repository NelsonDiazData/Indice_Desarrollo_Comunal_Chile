from pathlib import Path

from ETL.generar_geojson_chile import generar_geojson_chile
from build_iidc import main as construir_iidc
from QA.validar_mapa_comunas import validar_mapa_comunas


BASE_DIR = Path(__file__).resolve().parents[1]
RUTA_GEOJSON_NACIONAL = BASE_DIR / "Datos" / "Geografia" / "chile_comunas.geojson"

def run_pipeline():
    print("\n" + "=" * 70)
    print("PIPELINE DE CONSTRUCCIÓN DEL IIDC")
    print("=" * 70)

    print("\n[1/3] Verificando cartografía nacional...")

    if RUTA_GEOJSON_NACIONAL.exists():
        print("[OK] GeoJSON nacional disponible.")
    else:
        print("[INFO] GeoJSON nacional no encontrado.")
        print("[INFO] Generando cartografía nacional...")
        generar_geojson_chile()
        print("[OK] Cartografía nacional generada.")

    print("\n[2/3] Construyendo Índice Integrado de Desarrollo Comunal...")
    construir_iidc()

    print("\n[3/3] Validando consistencia entre cartografía y Data Mart...")
    validar_mapa_comunas()

    print("\n" + "=" * 70)
    print("PIPELINE FINALIZADO CORRECTAMENTE")
    print("=" * 70)


if __name__ == "__main__":
    run_pipeline()
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RUTA_DATOS = BASE_DIR / "Datos"
RUTA_MODELO = RUTA_DATOS / "Modelo"
RUTA_DOCUMENTACION = BASE_DIR / "Documentación"

SQL_SERVER = "NELSONDIAZ"
SQL_DATABASE = "IndiceDesarrolloComunal_CHILE"

ANIO_INDICE = 2025
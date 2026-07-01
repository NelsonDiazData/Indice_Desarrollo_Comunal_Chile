# Pipeline de Construcción del Índice Integrado de Desarrollo Comunal (IIDC)

## Objetivo

Automatizar el proceso completo de construcción del Índice Integrado de Desarrollo Comunal (IIDC), desde la validación de la cartografía hasta la actualización del Data Mart utilizado por Power BI.

---

# Flujo del Pipeline

```
                run_pipeline.py
                       │
                       ▼
        Verificar cartografía nacional
                       │
                       ▼
      Construcción del GeoJSON nacional
          (solo si no existe)
                       │
                       ▼
         Construcción del IIDC
                       │
                       ▼
       Validaciones de calidad
                       │
                       ▼
      Exportación del dataset final
                       │
                       ▼
  Actualización de mart.iidc_comunal
                       │
                       ▼
 Validación entre cartografía y Data Mart
                       │
                       ▼
                Power BI
```

---

# Componentes del Pipeline

## ETL

Responsable de generar la cartografía nacional unificada a partir de los GeoJSON regionales.

Archivo:

```
ETL/generar_geojson_chile.py
```

---

## Analytics

Construye el Índice Integrado de Desarrollo Comunal.

Incluye:

- transformación de variables
- normalización Min-Max
- construcción de dimensiones
- cálculo del IIDC
- ranking
- categorías
- exportación CSV
- actualización del Data Mart

Archivo:

```
build_iidc.py
```

---

## QA

Valida la consistencia entre la cartografía utilizada por Power BI y las comunas existentes en el Data Mart.

Archivo:

```
QA/validar_mapa_comunas.py
```

Validaciones realizadas:

- cantidad de comunas
- códigos comunales
- comunas faltantes
- comunas sobrantes

---

# Ejecución

Todo el proceso se ejecuta mediante un único comando.

```bash
python Python/run_pipeline.py
```

---

# Resultado

Al finalizar el pipeline se obtiene:

- GeoJSON nacional actualizado (si es necesario)
- Dataset IIDC normalizado
- Archivo CSV final
- Tabla `mart.iidc_comunal`
- Validación cartográfica
- Modelo listo para ser consumido por Power BI

---

# Arquitectura

```
Fuentes de datos
        │
        ▼
Python (ETL + Analytics + QA)
        │
        ▼
SQL Server
(Data Mart)
        │
        ▼
Power BI
```

---

# Beneficios

- Proceso completamente reproducible.
- Automatización del cálculo del IIDC.
- Separación entre ETL, Analytics y QA.
- Validación automática de la cartografía.
- Integración directa con SQL Server y Power BI.
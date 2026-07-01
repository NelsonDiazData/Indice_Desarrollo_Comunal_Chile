# 06 - Notas del Modelo SQL

## Proyecto
Índice de Desarrollo Comunal de Chile (IDC)

## Modelo dimensional

Base de datos: `IndiceDesarrolloComunal_CHILE`

Esquemas:
- `dim`: dimensiones.
- `fact`: tablas de hechos y vistas analíticas.
- `stg`: staging o futuras cargas intermedias.

## Tablas

### Dimensiones
- `dim.comuna`: comuna, provincia, región y nombres geográficos.
- `dim.indicador`: catálogo de indicadores SINIM seleccionados.

### Hechos SINIM
- `fact.ingresos_sinim`: ingresos SINIM 2015-2025 en formato largo.

### Hechos Censo
- `fact.censo_personas_comunal`: indicadores agregados desde personas.
- `fact.censo_hogares_comunal`: indicadores agregados desde hogares.
- `fact.censo_viviendas_comunal`: indicadores agregados desde viviendas.

## Vistas
- `fact.vw_ingresos_sinim_detalle`: detalle de ingresos con comuna, región, indicador y valor_limpio.
- `fact.vw_censo_comunal_integrado`: integración de las tres facts censales por comuna.
- `fact.vw_indice_desarrollo_base`: base analítica para el IDC.

## Reglas de limpieza

### SINIM
- Se excluyó `codigo_comuna=11111`, `comuna=SUBDERE_`.
- Los valores negativos se conservan en tabla base y se limpian en vistas mediante:

```sql
CASE WHEN valor < 0 THEN NULL ELSE valor END AS valor_limpio
```

### Censo 2024
Se detectaron códigos especiales en la fuente:
- `edad = -66`
- `escolaridad = -99`
- `discapacidad = -99`
- `p37_alfabet = -99`

Estos valores se transforman a NULL antes de calcular indicadores comunales.

## Validaciones esperadas
- `dim.comuna`: 346 registros.
- `dim.indicador`: 12 registros.
- `fact.ingresos_sinim`: 45.594 registros.
- `fact.censo_personas_comunal`: 346 registros.
- `fact.censo_hogares_comunal`: 346 registros.
- `fact.censo_viviendas_comunal`: 346 registros.
- Sin comunas huérfanas en hechos.
- Sin indicadores huérfanos en ingresos SINIM.

## Mejora pendiente
Crear `Python/config.py` para centralizar rutas y constantes del proyecto.

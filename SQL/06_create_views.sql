USE IndiceDesarrolloComunal_CHILE;
GO

DROP VIEW IF EXISTS fact.vw_indice_desarrollo_base;
GO

DROP VIEW IF EXISTS fact.vw_censo_comunal_integrado;
GO

DROP VIEW IF EXISTS fact.vw_ingresos_sinim_detalle;
GO

CREATE VIEW fact.vw_ingresos_sinim_detalle AS
SELECT
    f.anio,
    f.codigo_comuna,
    c.nombre_comuna,
    c.codigo_provincia,
    c.codigo_region,
    c.nombre_region,
    f.sector_modelo,
    f.codigo_indicador,
    i.indicador,
    f.valor AS valor_original,
    CASE
        WHEN f.valor < 0 THEN NULL
        ELSE f.valor
    END AS valor_limpio
FROM fact.ingresos_sinim f
INNER JOIN dim.comuna c
    ON f.codigo_comuna = c.codigo_comuna
INNER JOIN dim.indicador i
    ON f.sector_modelo = i.sector_modelo
    AND f.codigo_indicador = i.codigo_indicador;
GO

CREATE VIEW fact.vw_censo_comunal_integrado AS
SELECT
    c.codigo_comuna,
    c.nombre_comuna,
    c.codigo_provincia,
    c.codigo_region,
    c.nombre_region,

    p.poblacion_total,
    p.promedio_edad,
    p.porcentaje_menores_15,
    p.porcentaje_adultos_mayores,
    p.porcentaje_discapacidad,
    p.promedio_escolaridad,
    p.porcentaje_alfabetizacion,

    h.total_hogares,
    h.porcentaje_computador,
    h.porcentaje_internet_fija,
    h.porcentaje_internet_movil,

    v.total_viviendas,
    v.promedio_personas_vivienda,
    v.porcentaje_hacinamiento,
    v.porcentaje_agua_red,
    v.porcentaje_saneamiento,
    v.porcentaje_electricidad
FROM dim.comuna c
LEFT JOIN fact.censo_personas_comunal p
    ON c.codigo_comuna = p.codigo_comuna
LEFT JOIN fact.censo_hogares_comunal h
    ON c.codigo_comuna = h.codigo_comuna
LEFT JOIN fact.censo_viviendas_comunal v
    ON c.codigo_comuna = v.codigo_comuna;
GO

-- Vista base 2025: combina Censo 2024 con el último año disponible de SINIM.
-- Para evolución histórica, usar vw_ingresos_sinim_detalle directamente por año.
CREATE VIEW fact.vw_indice_desarrollo_base AS
WITH ingresos_pivot AS (
    SELECT
        codigo_comuna,
        SUM(CASE WHEN sector_modelo = 'Municipal' THEN valor_limpio ELSE 0 END) AS ingresos_municipales,
        SUM(CASE WHEN sector_modelo = 'Educacion' THEN valor_limpio ELSE 0 END) AS ingresos_educacion,
        SUM(CASE WHEN sector_modelo = 'Salud' THEN valor_limpio ELSE 0 END) AS ingresos_salud
    FROM fact.vw_ingresos_sinim_detalle
    WHERE anio = 2025
    GROUP BY codigo_comuna
)
SELECT
    c.codigo_comuna,
    c.nombre_comuna,
    c.codigo_region,
    c.nombre_region,
    c.poblacion_total,
    c.promedio_edad,
    c.porcentaje_menores_15,
    c.porcentaje_adultos_mayores,
    c.porcentaje_discapacidad,
    c.promedio_escolaridad,
    c.porcentaje_alfabetizacion,
    c.total_hogares,
    c.porcentaje_computador,
    c.porcentaje_internet_fija,
    c.porcentaje_internet_movil,
    c.total_viviendas,
    c.promedio_personas_vivienda,
    c.porcentaje_hacinamiento,
    c.porcentaje_agua_red,
    c.porcentaje_saneamiento,
    c.porcentaje_electricidad,
    i.ingresos_municipales,
    i.ingresos_educacion,
    i.ingresos_salud,
    i.ingresos_municipales / NULLIF(CAST(c.poblacion_total AS DECIMAL(18,2)), 0) AS ingresos_municipales_pc,
    i.ingresos_educacion / NULLIF(CAST(c.poblacion_total AS DECIMAL(18,2)), 0) AS ingresos_educacion_pc,
    i.ingresos_salud / NULLIF(CAST(c.poblacion_total AS DECIMAL(18,2)), 0) AS ingresos_salud_pc
FROM fact.vw_censo_comunal_integrado c
LEFT JOIN ingresos_pivot i
    ON c.codigo_comuna = i.codigo_comuna;
GO

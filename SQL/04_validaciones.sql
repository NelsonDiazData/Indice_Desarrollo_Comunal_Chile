USE IndiceDesarrolloComunal_CHILE;
GO

SELECT COUNT(*) AS total_comunas
FROM dim.comuna;

SELECT COUNT(*) AS total_indicadores
FROM dim.indicador;

SELECT COUNT(*) AS total_fact_ingresos
FROM fact.ingresos_sinim;

SELECT
    sector_modelo,
    COUNT(*) AS registros
FROM fact.ingresos_sinim
GROUP BY sector_modelo
ORDER BY sector_modelo;

SELECT
    MIN(anio) AS anio_min,
    MAX(anio) AS anio_max
FROM fact.ingresos_sinim;

SELECT
    f.codigo_comuna
FROM fact.ingresos_sinim f
LEFT JOIN dim.comuna c
    ON f.codigo_comuna = c.codigo_comuna
WHERE c.codigo_comuna IS NULL;

SELECT
    f.sector_modelo,
    f.codigo_indicador
FROM fact.ingresos_sinim f
LEFT JOIN dim.indicador i
    ON f.sector_modelo = i.sector_modelo
    AND f.codigo_indicador = i.codigo_indicador
WHERE i.codigo_indicador IS NULL;
GO

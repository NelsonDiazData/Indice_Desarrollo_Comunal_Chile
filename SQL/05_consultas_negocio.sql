USE IndiceDesarrolloComunal_CHILE;
GO

-- Ingresos por año y sector
SELECT
    f.anio,
    f.sector_modelo,
    SUM(f.valor) AS total_ingresos
FROM fact.ingresos_sinim f
GROUP BY f.anio, f.sector_modelo
ORDER BY f.anio, f.sector_modelo;

-- Ingresos por región, año y sector
SELECT
    f.anio,
    c.nombre_region,
    f.sector_modelo,
    SUM(f.valor) AS total_ingresos
FROM fact.ingresos_sinim f
INNER JOIN dim.comuna c
    ON f.codigo_comuna = c.codigo_comuna
GROUP BY f.anio, c.nombre_region, f.sector_modelo
ORDER BY f.anio, c.nombre_region, f.sector_modelo;

-- Top comunas por ingresos acumulados
SELECT TOP 20
    c.nombre_region,
    c.nombre_comuna,
    SUM(f.valor) AS total_ingresos
FROM fact.ingresos_sinim f
INNER JOIN dim.comuna c
    ON f.codigo_comuna = c.codigo_comuna
GROUP BY c.nombre_region, c.nombre_comuna
ORDER BY total_ingresos DESC;

-- Ingresos por indicador
SELECT
    f.sector_modelo,
    i.indicador,
    SUM(f.valor) AS total_ingresos
FROM fact.ingresos_sinim f
INNER JOIN dim.indicador i
    ON f.sector_modelo = i.sector_modelo
    AND f.codigo_indicador = i.codigo_indicador
GROUP BY f.sector_modelo, i.indicador
ORDER BY f.sector_modelo, total_ingresos DESC;
GO

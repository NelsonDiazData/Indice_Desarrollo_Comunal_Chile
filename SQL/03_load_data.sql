USE IndiceDesarrolloComunal_CHILE;
GO

BULK INSERT dim.comuna
FROM 'C:\Users\el_ap\OneDrive\Desktop\Portafolio Power BI\Índice Desarrollo Comunal\Datos\Modelo\dim_comuna.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
GO

BULK INSERT dim.indicador
FROM 'C:\Users\el_ap\OneDrive\Desktop\Portafolio Power BI\Índice Desarrollo Comunal\Datos\Modelo\dim_indicador.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
GO

BULK INSERT fact.ingresos_sinim
FROM 'C:\Users\el_ap\OneDrive\Desktop\Portafolio Power BI\Índice Desarrollo Comunal\Datos\Modelo\fact_ingresos_sinim.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);
GO

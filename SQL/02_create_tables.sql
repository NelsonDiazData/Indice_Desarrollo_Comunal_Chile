USE IndiceDesarrolloComunal_CHILE;
GO

DROP TABLE IF EXISTS fact.ingresos_sinim;
GO

DROP TABLE IF EXISTS dim.indicador;
GO

DROP TABLE IF EXISTS dim.comuna;
GO

CREATE TABLE dim.comuna (
    codigo_comuna INT NOT NULL PRIMARY KEY,
    nombre_comuna VARCHAR(100) NOT NULL,
    codigo_provincia INT NOT NULL,
    codigo_region INT NOT NULL,
    nombre_region VARCHAR(100) NOT NULL
);
GO

CREATE TABLE dim.indicador (
    sector_modelo VARCHAR(50) NOT NULL,
    codigo_indicador VARCHAR(30) NOT NULL,
    indicador VARCHAR(255) NOT NULL,
    CONSTRAINT PK_dim_indicador PRIMARY KEY (sector_modelo, codigo_indicador)
);
GO

CREATE TABLE fact.ingresos_sinim (
    anio INT NOT NULL,
    codigo_comuna INT NOT NULL,
    sector_modelo VARCHAR(50) NOT NULL,
    codigo_indicador VARCHAR(30) NOT NULL,
    valor DECIMAL(18,2) NOT NULL,

    CONSTRAINT FK_ingresos_comuna
        FOREIGN KEY (codigo_comuna)
        REFERENCES dim.comuna(codigo_comuna),

    CONSTRAINT FK_ingresos_indicador
        FOREIGN KEY (sector_modelo, codigo_indicador)
        REFERENCES dim.indicador(sector_modelo, codigo_indicador)
);
GO

# Metodología de Construcción del Índice Integrado de Desarrollo Comunal (IIDC)

**Proyecto:** Índice Integrado de Desarrollo Comunal de Chile (IIDC)

**Autor:** Nelson Daniel Díaz Dean

---

# 1. Objetivo

Este documento registra el proceso metodológico seguido durante la construcción del Índice Integrado de Desarrollo Comunal (IIDC).

Su propósito es documentar las decisiones analíticas, los hallazgos obtenidos durante el análisis exploratorio de datos (EDA), las hipótesis formuladas y las modificaciones realizadas al modelo, permitiendo que el proceso sea completamente reproducible y justificable.

El enfoque adoptado busca que cada decisión metodológica esté respaldada por evidencia obtenida directamente desde los datos y no únicamente por criterios subjetivos.

---

# 2. Metodología General

El desarrollo del IIDC sigue el siguiente flujo de trabajo:

1. Obtención y validación del dataset.
2. Análisis exploratorio de datos (EDA).
3. Evaluación de calidad de la información.
4. Identificación de anomalías y valores atípicos.
5. Formulación de hipótesis.
6. Validación mediante análisis estadístico e histórico.
7. Construcción del índice.
8. Análisis de sensibilidad del modelo.
9. Visualización de resultados en Power BI.

---

# 3. Registro de Hallazgos

Cada hallazgo será documentado siguiendo la siguiente estructura:

* Fecha.
* Descripción.
* Evidencia.
* Hipótesis.
* Decisión metodológica.
* Estado.
* Próximos pasos.

---

# Hallazgo 001 – Valores iguales a cero en Ingresos Municipales de Educación

**Fecha:** 25/06/2026

## Descripción

Durante el análisis exploratorio se detectó que aproximadamente el **29,28 %** de las comunas presentan un valor igual a cero en la variable **Ingresos Municipales de Educación**.

Inicialmente se consideró la posibilidad de que estos valores correspondieran a errores de carga o datos faltantes.

---

## Evidencia

Se consultó la serie histórica de distintas comunas utilizando la vista:

```sql
fact.vw_indice_desarrollo_historico
```

En el caso de la comuna de Arica (Código 15101) se observó el siguiente comportamiento:

* Entre 2015 y 2019 existen ingresos municipales de educación.
* Desde 2020 en adelante el valor registrado es igual a cero.

Posteriormente se realizó un análisis histórico para todas las comunas, observándose que el año de transición hacia valores iguales a cero no es uniforme.

Existen comunas cuyo cambio ocurre en distintos años (2017, 2019, 2020 y 2022, entre otros).

Este comportamiento descarta la hipótesis de un error generalizado del proceso ETL o de la base de datos.

---

## Hipótesis

La evidencia observada es consistente con un cambio institucional asociado al proceso gradual de implementación de los Servicios Locales de Educación Pública (SLEP), mediante el cual la administración de los establecimientos educacionales deja de depender del municipio.

En consecuencia, un valor igual a cero no necesariamente representa ausencia de recursos destinados a educación, sino un cambio en la institución responsable de administrar dichos recursos.

---

## Implicancias para el IIDC

La variable **Ingresos Municipales de Educación** podría dejar de representar la capacidad económica de la comuna y comenzar a reflejar un cambio administrativo.

Por este motivo será evaluada antes de incorporarse definitivamente al índice.

---

## Estado

🟡 En investigación.

---

## Próximos pasos

* Verificar documentalmente la fecha de incorporación al SLEP de las comunas afectadas.
* Analizar el comportamiento por región.
* Evaluar el impacto de excluir esta variable del modelo.
* Comparar distintas versiones del IIDC mediante un análisis de sensibilidad.

---

# 4. Versionado del Modelo

El IIDC podrá evolucionar mediante distintas versiones metodológicas.

Actualmente se consideran:

| Versión | Descripción                                              |
| ------- | -------------------------------------------------------- |
| IIDC v1 | Modelo base con todas las variables.                     |
| IIDC v2 | Modelo excluyendo Ingresos Municipales de Educación.     |
| IIDC v3 | Modelo ajustado considerando el efecto del proceso SLEP. |

Cada versión será comparada mediante análisis de sensibilidad para evaluar la estabilidad del ranking comunal y la robustez del índice.

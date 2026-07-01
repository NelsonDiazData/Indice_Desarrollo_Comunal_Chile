**Proyecto:** Índice de Desarrollo Comunal de Chile (IIDC)

**Documento:** 01 - Calidad de los Datos

**Versión:** 1.0

**Autor:** Nelson Daniel Díaz Dean

**Última actualización:** Julio 2026

**Diseño, validación estadística y visualización de un indicador multidimensional utilizando Python, SQL Server y Power BI.**

---

# 1. Objetivo

Antes de construir cualquier indicador compuesto, es fundamental evaluar la calidad de los datos que servirán como base del análisis.

El objetivo de esta etapa fue verificar la integridad, consistencia y confiabilidad del conjunto de datos consolidado del Índice de Desarrollo Comunal (IIDC), identificando posibles problemas que pudieran afectar la interpretación del índice o introducir sesgos durante el proceso de modelado.

Las validaciones realizadas permitieron garantizar que las transformaciones posteriores (normalización, construcción de subíndices y cálculo del IIDC) se realizaran sobre información consistente y adecuadamente documentada.

---

# 2. Fuente de información

El proyecto integra información proveniente de distintas fuentes oficiales del Estado de Chile.

Entre ellas se encuentran:

* Sistema Nacional de Información Municipal (SINIM)
* Censo de Población y Vivienda 2024
* Información territorial de comunas y regiones

La consolidación de estas fuentes permitió construir un único dataset comunal con variables demográficas, económicas, educacionales, de infraestructura, conectividad y habitabilidad.

---

# 3. Descripción general del dataset

Luego del proceso ETL y de consolidación de las distintas fuentes, el conjunto de datos quedó compuesto por:

| Característica              |    Valor |
| --------------------------- | -------: |
| Comunas                     |      345 |
| Variables originales        |       26 |
| Cobertura                   | Nacional |
| Año de referencia principal |     2025 |

Cada registro representa una comuna de Chile y contiene indicadores que posteriormente serán utilizados para la construcción del IIDC.

---

# 4. Validaciones realizadas

Durante esta etapa se realizaron las siguientes verificaciones de calidad.

## 4.1 Registros duplicados

Se verificó la existencia de registros completamente duplicados y de duplicados por código de comuna.

**Resultado**

* Duplicados exactos: **0**
* Duplicados por código de comuna: **0**

No fue necesario eliminar registros.

---

## 4.2 Valores nulos

Se identificaron las variables con información faltante.

Las variables relacionadas con estructura etaria presentan información faltante en aproximadamente 50 comunas:

* promedio_edad
* porcentaje_menores_15
* porcentaje_adultos_mayores

Estas variables no fueron consideradas para la construcción del índice principal, por lo que su ausencia no afecta el cálculo del IIDC.

---

## 4.3 Valores iguales a cero

Se analizaron variables cuyos valores podían representar ausencia de información o un comportamiento estructural del dato.

Los resultados más relevantes fueron:

| Variable                | % Valores iguales a cero |
| ----------------------- | -----------------------: |
| ingresos_municipales_pc |                   1,45 % |
| ingresos_salud_pc       |                   8,41 % |
| ingresos_educacion_pc   |                  29,28 % |

La variable **ingresos_educacion_pc** presentó una proporción considerablemente superior al resto, motivando una investigación específica sobre su comportamiento histórico.

---

# 5. Investigación de los valores cero en Educación

Durante el análisis exploratorio se detectó que aproximadamente un 29 % de las comunas presentan ingresos iguales a cero en la variable de educación.

Inicialmente se consideró la posibilidad de errores de carga o registros incompletos.

Sin embargo, al revisar la serie histórica de varias comunas se observó un patrón consistente:

* Las comunas presentan valores históricos distintos de cero.
* A partir de determinados años los ingresos pasan a registrarse como cero.
* El cambio ocurre en distintos años según la comuna.

Este comportamiento es consistente con los cambios administrativos derivados de la implementación gradual del sistema de Servicios Locales de Educación Pública (SLEP), mediante el cual la administración de los establecimientos educacionales deja de depender directamente del municipio.

Por esta razón, los valores iguales a cero fueron considerados como **ceros estructurales** y no como errores del proceso ETL.

No obstante, esta situación será considerada durante la construcción del índice para evaluar su impacto sobre la dimensión económica.

---

# 6. Transformaciones realizadas

Con el objetivo de mejorar la comparabilidad entre comunas de distintos tamaños poblacionales, se realizaron transformaciones adicionales.

## Variables per cápita

Se generaron las siguientes variables:

* ingresos_municipales_pc
* ingresos_educacion_pc
* ingresos_salud_pc

Estas variables permiten comparar comunas independientemente de su población total.

---

## Variables invertidas

Para aquellas variables donde un valor menor representa una mejor condición de desarrollo se realizó una inversión previa a la normalización.

Ejemplos:

* porcentaje_hacinamiento
* promedio_personas_vivienda

De esta manera todas las variables mantienen la misma interpretación:

> Valores más altos representan mejores condiciones de desarrollo.

---

## Normalización

Todas las variables utilizadas posteriormente en el IIDC fueron normalizadas utilizando una escala común, permitiendo combinar indicadores medidos en unidades completamente distintas.

---

# 7. Conclusiones

La evaluación de calidad permitió concluir que el dataset consolidado presenta un alto nivel de consistencia para la construcción del Índice de Desarrollo Comunal.

No se detectaron registros duplicados y las variables seleccionadas para el índice presentan una cobertura prácticamente completa.

El principal hallazgo de esta etapa corresponde al comportamiento de la variable **ingresos_educacion**, cuyos valores iguales a cero no responden a errores de calidad de datos, sino probablemente a cambios administrativos asociados al proceso de implementación de los Servicios Locales de Educación Pública (SLEP).

Este hallazgo motivó análisis estadísticos posteriores orientados a determinar si dicha variable debía mantener el mismo tratamiento que el resto de variables económicas durante la construcción del índice.

---

# 8. Lecciones aprendidas

* La ausencia de valores no siempre representa un problema de calidad de datos.
* Es necesario distinguir entre datos faltantes y cambios estructurales en el proceso de generación de la información.
* La investigación del contexto institucional resulta tan importante como la validación técnica del dataset.
* Las transformaciones per cápita permiten realizar comparaciones más justas entre comunas con tamaños poblacionales muy diferentes.
* La calidad de los datos constituye la base sobre la cual se desarrollan todas las etapas posteriores del proyecto.

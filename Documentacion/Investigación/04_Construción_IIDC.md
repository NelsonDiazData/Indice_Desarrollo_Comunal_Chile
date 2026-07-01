# Construcción del Índice de Desarrollo Comunal (IIDC)

**Proyecto:** Índice de Desarrollo Comunal de Chile (IIDC)

**Documento:** 04 - Construcción del IIDC

**Versión:** 1.0

**Autor:** Nelson Daniel Díaz Dean

---

# 1. Objetivo

El objetivo de esta etapa fue diseñar un Índice de Desarrollo Comunal (IIDC) que permitiera sintetizar múltiples dimensiones del desarrollo en un único indicador, facilitando la comparación entre comunas chilenas.

El índice fue construido siguiendo una metodología transparente, reproducible e interpretable, priorizando la comprensión del fenómeno sobre la complejidad matemática.

Las decisiones metodológicas fueron respaldadas mediante análisis estadísticos desarrollados en las etapas anteriores del proyecto.

---

# 2. Principios metodológicos

La construcción del IIDC se basó en cuatro principios fundamentales.

## Comparabilidad

Todas las comunas deben ser evaluadas utilizando una misma metodología, independientemente de su tamaño poblacional.

---

## Interpretabilidad

Cada componente del índice debe poseer una interpretación clara para facilitar su utilización por parte de usuarios técnicos y de negocio.

---

## Reproducibilidad

Todas las transformaciones realizadas pueden ser replicadas utilizando únicamente el código desarrollado dentro del proyecto.

---

## Validación estadística

Las decisiones metodológicas fueron contrastadas mediante análisis de correlaciones, multicolinealidad y Análisis de Componentes Principales (PCA).

---

# 3. Selección de variables

Luego del proceso de limpieza y validación se seleccionaron trece variables distribuidas en cinco dimensiones conceptuales.

## Economía

* ingresos_municipales_pc
* ingresos_educacion_pc
* ingresos_salud_pc

---

## Capital Humano

* promedio_escolaridad
* porcentaje_alfabetizacion

---

## Infraestructura

* porcentaje_agua_red
* porcentaje_saneamiento
* porcentaje_electricidad

---

## Habitabilidad

* porcentaje_hacinamiento
* promedio_personas_vivienda

---

## Conectividad

* porcentaje_computador
* porcentaje_internet_fija
* porcentaje_internet_movil

---

# 4. Transformación de variables

Antes del cálculo del índice se realizaron diversas transformaciones para garantizar la comparabilidad entre indicadores.

## Variables per cápita

Los ingresos municipales, de educación y de salud fueron transformados a valores per cápita para eliminar el efecto del tamaño poblacional.

---

## Variables invertidas

Las variables donde valores menores representan mejores condiciones de desarrollo fueron invertidas antes de la normalización.

Variables invertidas:

* porcentaje_hacinamiento
* promedio_personas_vivienda

Con esta transformación, todas las variables mantienen una interpretación común:

> Valores más altos representan mejores condiciones de desarrollo.

---

## Normalización

Todas las variables fueron normalizadas utilizando una escala común entre 0 y 100.

Esta transformación permite combinar indicadores originalmente expresados en distintas unidades de medida sin alterar su comportamiento relativo.

---

# 5. Construcción de subíndices

Cada dimensión fue calculada mediante el promedio simple de las variables que la componen.

## Economía

Promedio de:

* ingresos municipales per cápita
* ingresos educación per cápita
* ingresos salud per cápita

Durante la investigación se identificó que la variable de ingresos en educación presenta un comportamiento estructural distinto al resto del grupo económico.

No obstante, se decidió mantenerla dentro del índice conceptual con el objetivo de preservar la interpretación original del indicador y evaluar posteriormente su impacto mediante análisis de sensibilidad.

---

## Capital Humano

Promedio de:

* escolaridad
* alfabetización

---

## Infraestructura

Promedio de:

* agua
* saneamiento
* electricidad

---

## Habitabilidad

Promedio de:

* hacinamiento (invertido)
* personas por vivienda (invertido)

---

## Conectividad

Promedio de:

* computador
* internet fija
* internet móvil

---

# 6. Construcción del IIDC

Una vez obtenidos los cinco subíndices, el IIDC se calculó mediante el promedio simple de las cinco dimensiones.

Esta estrategia asigna la misma importancia conceptual a cada dimensión del desarrollo comunal.

Matemáticamente:

IIDC = (Economía + Capital Humano + Infraestructura + Habitabilidad + Conectividad) / 5

La utilización de ponderaciones iguales facilita la interpretación del índice y evita introducir sesgos derivados de decisiones arbitrarias de ponderación.

---

# 7. Validación metodológica

Durante el desarrollo del proyecto se evaluó la robustez del índice mediante distintas técnicas estadísticas.

Entre ellas:

* Estadística descriptiva.
* Correlaciones de Pearson.
* Correlaciones de Spearman.
* Heatmap de correlaciones.
* Factor de Inflación de la Varianza (VIF).
* Análisis de Componentes Principales (PCA).

Los resultados evidenciaron que algunas dimensiones presentan una importante superposición estadística.

Sin embargo, se decidió mantener la estructura conceptual del IIDC debido a que representa una interpretación más intuitiva del fenómeno para usuarios de negocio y tomadores de decisiones.

El PCA fue utilizado como herramienta de validación y contraste, no como mecanismo de sustitución del índice conceptual.

---

# 8. Limitaciones

El IIDC constituye una aproximación cuantitativa al desarrollo comunal utilizando la información disponible para el período analizado.

Entre las principales limitaciones identificadas se encuentran:

* disponibilidad de algunas variables únicamente para un año;
* cambios administrativos asociados a los Servicios Locales de Educación Pública (SLEP);
* alta correlación entre ciertos indicadores de infraestructura y conectividad;
* ausencia de variables relacionadas con seguridad, medio ambiente, empleo y movilidad.

Estas limitaciones representan oportunidades de mejora para futuras versiones del índice.

---

# 9. Propuesta de evolución del proyecto

Como resultado de la investigación realizada, se propone desarrollar una segunda versión experimental del índice.

## IIDC Conceptual (Versión 1)

Construido utilizando las cinco dimensiones conceptuales definidas inicialmente.

Su principal fortaleza es la interpretabilidad.

---

## IIDC Experimental (Versión 2)

Construido utilizando la estructura identificada mediante Análisis de Componentes Principales (PCA).

Esta versión permitirá comparar el comportamiento del índice conceptual frente a una construcción basada exclusivamente en la estructura estadística de los datos.

La comparación entre ambas metodologías permitirá evaluar la sensibilidad del índice frente a distintos enfoques de construcción.

---

# 10. Conclusiones

La construcción del IIDC combinó criterios conceptuales con evidencia estadística obtenida durante el proceso de investigación.

El análisis exploratorio permitió identificar particularidades importantes del conjunto de datos, mientras que las técnicas multivariadas respaldaron las decisiones metodológicas adoptadas.

El resultado es un índice interpretable, reproducible y metodológicamente documentado, capaz de sintetizar múltiples dimensiones del desarrollo comunal en un único indicador.

Más que un valor numérico, el IIDC representa un marco analítico para comprender las diferencias territoriales entre comunas chilenas y apoyar procesos de análisis, comparación y toma de decisiones.

---

# 11. Lecciones aprendidas

* Un índice compuesto debe ser conceptualmente interpretable antes de ser estadísticamente sofisticado.
* La validación estadística fortalece el diseño metodológico, pero no reemplaza el criterio conceptual.
* La combinación de teoría y evidencia empírica permitió construir un indicador más robusto y defendible.
* Documentar las decisiones metodológicas es tan importante como implementar el algoritmo que calcula el índice.
* La construcción de indicadores multidimensionales requiere un equilibrio entre simplicidad, interpretabilidad y rigor estadístico.

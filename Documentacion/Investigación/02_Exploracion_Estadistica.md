# Exploración Estadística

**Proyecto:** Índice de Desarrollo Comunal de Chile (IIDC)

**Documento:** 02 - Exploración Estadística

**Versión:** 1.0

**Autor:** Nelson Daniel Díaz Dean

---

# 1. Objetivo

Una vez validada la calidad del conjunto de datos, se realizó una exploración estadística con el propósito de comprender el comportamiento de las variables que conforman el Índice de Desarrollo Comunal (IIDC).

Esta etapa tuvo como objetivos principales:

* Comprender la distribución de cada variable.
* Detectar valores extremos (outliers).
* Identificar asimetrías importantes.
* Analizar la relación entre población e indicadores económicos.
* Evaluar el comportamiento de las variables antes de construir el índice.

A diferencia de una simple exploración descriptiva, esta etapa buscó generar hipótesis que posteriormente serían contrastadas mediante análisis multivariado.

---

# 2. Estadística descriptiva

Para cada una de las variables numéricas se calcularon los principales estadísticos descriptivos:

* Número de observaciones.
* Media.
* Mediana.
* Desviación estándar.
* Valores mínimos y máximos.
* Percentiles.
* Asimetría (Skewness).
* Curtosis (Kurtosis).

El objetivo fue identificar distribuciones anormales, variables altamente dispersas y posibles valores extremos.

---

# 3. Distribución de las variables económicas

Las primeras variables analizadas fueron los ingresos municipales, ingresos en salud e ingresos en educación.

Durante esta etapa se observó un comportamiento común en las tres variables:

* fuerte concentración de comunas con ingresos relativamente bajos;
* presencia de pocas comunas con ingresos considerablemente superiores;
* distribuciones altamente asimétricas hacia la derecha.

Esta estructura sugiere la existencia de una distribución típica de variables económicas territoriales, donde un número reducido de comunas concentra una proporción importante de los recursos disponibles.

---

# 4. Transformación logarítmica

Se evaluó la aplicación de una transformación logarítmica (`log(x+1)`) sobre las variables económicas con el objetivo de reducir la asimetría observada.

Si bien la transformación mejoró parcialmente la visualización de las distribuciones, los indicadores de asimetría y curtosis continuaron siendo elevados.

Como resultado, se decidió mantener las variables originales para los análisis posteriores, utilizando métodos estadísticos adecuados para distribuciones no normales cuando fuese necesario.

---

# 5. Variables per cápita

Con el propósito de eliminar el efecto del tamaño poblacional, los ingresos municipales, de salud y de educación fueron transformados a valores per cápita.

Esta decisión permitió comparar comunas de distinta población bajo una misma escala de análisis.

El uso de indicadores per cápita evita que comunas altamente pobladas aparezcan sistemáticamente favorecidas únicamente por su tamaño.

---

# 6. Relación entre población e ingresos

Posteriormente se analizaron diagramas de dispersión entre la población comunal y los ingresos per cápita.

Los resultados mostraron una relación claramente no lineal.

Las comunas de menor población presentan una dispersión considerablemente mayor en sus ingresos per cápita, mientras que las comunas más pobladas muestran valores relativamente más estables.

Este comportamiento sugirió que la población ejerce un efecto importante sobre la variabilidad de los indicadores económicos, particularmente en comunas pequeñas.

---

# 7. Pearson versus Spearman

Debido al comportamiento observado en los diagramas de dispersión, se compararon dos medidas de correlación:

* Correlación de Pearson.
* Correlación de Spearman.

La correlación de Pearson presentó asociaciones débiles entre población e ingresos per cápita.

Sin embargo, la correlación de Spearman reveló asociaciones considerablemente más fuertes, especialmente para los ingresos municipales per cápita.

Este resultado indica que la relación entre estas variables no es estrictamente lineal, sino predominantemente monotónica.

En consecuencia, la correlación de Spearman fue considerada una medida más representativa para describir este comportamiento.

---

# 8. Hallazgos relevantes

Durante la exploración estadística surgieron varios hallazgos que modificaron el enfoque inicial del proyecto.

## Hallazgo 1

Las variables económicas presentan distribuciones altamente asimétricas y contienen valores extremos que representan comunas con capacidades financieras significativamente superiores al promedio nacional.

---

## Hallazgo 2

La población explica parte del comportamiento observado en los ingresos per cápita, aunque dicha relación no sigue un patrón lineal.

---

## Hallazgo 3

Las variables económicas no presentan el mismo comportamiento entre sí.

Particularmente, los ingresos en educación muestran un patrón distinto respecto a los ingresos municipales y de salud, reforzando la hipótesis planteada durante la etapa de calidad de datos sobre el posible efecto de la implementación de los Servicios Locales de Educación Pública (SLEP).

---

## Hallazgo 4

La comparación entre Pearson y Spearman permitió concluir que las relaciones entre varias variables del proyecto son monotónicas y no necesariamente lineales.

Este resultado condicionó la selección de las técnicas estadísticas utilizadas en las etapas posteriores.

---

# 9. Conclusiones

La exploración estadística permitió comprender el comportamiento general de las variables antes de iniciar la construcción del índice.

Las distribuciones observadas evidencian que el desarrollo comunal es un fenómeno altamente heterogéneo y que las diferencias entre comunas no pueden explicarse únicamente mediante relaciones lineales simples.

Los resultados obtenidos justificaron la realización de análisis multivariados para comprender la estructura conjunta de las variables y evaluar posibles redundancias entre los indicadores utilizados.

---

# 10. Lecciones aprendidas

* Una distribución altamente asimétrica no implica necesariamente una mala calidad del dato.
* La visualización gráfica es fundamental para comprender relaciones que no son evidentes mediante estadísticas descriptivas.
* Las transformaciones deben responder a una necesidad analítica y no aplicarse de forma automática.
* La comparación entre Pearson y Spearman permitió identificar relaciones monotónicas que no habrían sido detectadas utilizando únicamente correlaciones lineales.
* La exploración estadística permitió formular hipótesis que posteriormente fueron evaluadas mediante análisis de correlaciones, multicolinealidad y Análisis de Componentes Principales (PCA).

# Hallazgos de la Investigación

**Proyecto:** Índice de Desarrollo Comunal de Chile (IIDC)

**Documento:** 05 - Hallazgos

**Versión:** 1.0

**Autor:** Nelson Daniel Díaz Dean

---

# Introducción

El objetivo de este documento es resumir los principales hallazgos obtenidos durante el proceso de investigación y construcción del Índice de Desarrollo Comunal (IIDC).

A diferencia de los documentos metodológicos, este informe se centra en los descubrimientos obtenidos a partir del análisis de los datos y en las implicancias que estos tienen para la interpretación del desarrollo comunal en Chile.

Los hallazgos aquí presentados fueron obtenidos mediante análisis exploratorios, estadísticos y multivariados realizados durante el desarrollo del proyecto.

---

# Hallazgo 1

## El desarrollo comunal es un fenómeno multidimensional

Desde el inicio del proyecto se asumió que el desarrollo comunal no podía explicarse mediante una única variable.

Los resultados confirmaron esta hipótesis.

Variables relacionadas con educación, infraestructura, conectividad, salud, ingresos municipales y condiciones habitacionales aportan información complementaria sobre el nivel de desarrollo de cada comuna.

Este resultado respalda la construcción de un índice compuesto en lugar de utilizar indicadores aislados.

---

# Hallazgo 2

## La población influye en el comportamiento de los indicadores económicos

Los análisis exploratorios mostraron que las comunas con menor población presentan una mayor variabilidad en los ingresos municipales, de salud y de educación expresados en términos per cápita.

Las comunas más grandes tienden a presentar valores más estables, mientras que las comunas pequeñas muestran una dispersión considerablemente mayor.

Este comportamiento justificó la utilización de variables per cápita para mejorar la comparabilidad entre territorios.

---

# Hallazgo 3

## Las relaciones entre variables no son estrictamente lineales

La comparación entre las correlaciones de Pearson y Spearman evidenció diferencias importantes.

Mientras Pearson mostró asociaciones relativamente débiles, Spearman permitió identificar relaciones monotónicas significativamente más fuertes.

Este resultado indica que varios fenómenos asociados al desarrollo comunal evolucionan conjuntamente sin seguir necesariamente una relación lineal.

La selección de técnicas estadísticas adecuadas resultó fundamental para comprender correctamente el comportamiento de los datos.

---

# Hallazgo 4

## Infraestructura, conectividad y capital humano evolucionan conjuntamente

El análisis de correlaciones reveló una fuerte asociación entre variables relacionadas con:

* escolaridad;
* alfabetización;
* acceso a computadores;
* acceso a internet;
* agua potable;
* saneamiento;
* electricidad.

Estas relaciones sugieren que el desarrollo comunal tiende a manifestarse de manera integrada, donde avances en una dimensión suelen acompañarse de mejoras en otras.

---

# Hallazgo 5

## Los ingresos municipales y los ingresos en salud presentan un comportamiento muy similar

Las variables de ingresos municipales e ingresos en salud mostraron una alta correlación entre sí.

Este resultado sugiere que ambas variables representan una dimensión común asociada a la capacidad financiera o administrativa de los gobiernos locales.

Su comportamiento fue consistente tanto en los análisis de correlación como en el Análisis de Componentes Principales (PCA).

---

# Hallazgo 6

## Los ingresos en educación presentan un comportamiento estructural diferente

Uno de los descubrimientos más relevantes del proyecto corresponde a la variable de ingresos en educación.

Durante la etapa de calidad de datos se detectó que aproximadamente un 29 % de las comunas registran ingresos iguales a cero.

La revisión de casos individuales mostró que este comportamiento coincide con el proceso gradual de implementación de los Servicios Locales de Educación Pública (SLEP), mediante el cual la administración de la educación deja de depender directamente de los municipios.

Los análisis posteriores confirmaron que esta variable presenta un comportamiento estadístico considerablemente distinto respecto al resto de variables económicas.

---

# Hallazgo 7

## Existen importantes niveles de redundancia entre variables

El análisis mediante el Factor de Inflación de la Varianza (VIF) evidenció niveles elevados de multicolinealidad.

Lejos de representar un problema de calidad de datos, este resultado indica que varias variables describen aspectos comunes del desarrollo comunal.

Este hallazgo justificó la utilización de técnicas de reducción de dimensionalidad para comprender mejor la estructura del conjunto de datos.

---

# Hallazgo 8

## La estructura estadística no coincide completamente con la estructura conceptual

El Análisis de Componentes Principales permitió identificar que gran parte de la variabilidad del dataset puede resumirse mediante un número reducido de componentes.

Los cuatro primeros componentes explican aproximadamente el 86 % de la información disponible.

Sin embargo, la agrupación obtenida estadísticamente no coincide exactamente con las cinco dimensiones conceptuales utilizadas para construir el IIDC.

Este resultado no invalida el índice conceptual; por el contrario, demuestra la importancia de contrastar permanentemente la teoría con la evidencia empírica.

---

# Hallazgo 9

## La investigación modificó el enfoque original del proyecto

Inicialmente el objetivo consistía en desarrollar un dashboard que permitiera visualizar un índice de desarrollo comunal.

Sin embargo, el análisis de los datos transformó progresivamente el alcance del proyecto.

El foco dejó de estar únicamente en la visualización para centrarse en la construcción y validación metodológica del indicador.

Como consecuencia, el dashboard pasó a convertirse en la herramienta de comunicación de una investigación previamente validada.

---

# Hallazgo 10

## El valor del proyecto radica tanto en la metodología como en el resultado

Uno de los principales aprendizajes obtenidos durante el desarrollo del IIDC es que la construcción de un indicador requiere mucho más que combinar variables y generar visualizaciones.

El verdadero aporte del proyecto reside en el proceso utilizado para formular hipótesis, validar supuestos, cuestionar resultados y justificar metodológicamente cada decisión adoptada.

La documentación desarrollada durante el proyecto busca precisamente preservar ese proceso de razonamiento para facilitar su comprensión, revisión y reproducción.

---

# Conclusiones generales

El desarrollo comunal constituye un fenómeno complejo que no puede explicarse mediante un único indicador.

La combinación de técnicas de calidad de datos, exploración estadística, análisis multivariado y construcción de indicadores permitió desarrollar un índice metodológicamente sólido y respaldado por evidencia empírica.

Más allá del resultado numérico obtenido para cada comuna, el principal producto de este proyecto es una metodología reproducible para estudiar el desarrollo territorial utilizando datos públicos.

---

# Trabajo futuro

Este proyecto representa una primera versión del Índice de Desarrollo Comunal.

Como líneas de evolución futuras se consideran:

* incorporación de nuevas dimensiones relacionadas con seguridad, empleo, movilidad y medio ambiente;
* análisis temporal utilizando series históricas;
* comparación entre el índice conceptual y un índice construido mediante PCA;
* análisis de sensibilidad de ponderaciones;
* evaluación de nuevas fuentes oficiales de información.

---

# Reflexión final

Este proyecto comenzó con el objetivo de desarrollar un dashboard para visualizar información comunal.

Durante el proceso de investigación, el énfasis pasó desde la construcción de visualizaciones hacia la comprensión profunda de los datos y la validación metodológica del índice.

La experiencia confirmó que el análisis de datos no consiste únicamente en aplicar herramientas estadísticas o construir modelos, sino en formular preguntas, contrastar hipótesis y documentar rigurosamente cada decisión tomada.

El Índice de Desarrollo Comunal desarrollado en este proyecto representa tanto un producto analítico como una metodología de trabajo orientada a la toma de decisiones basada en evidencia.

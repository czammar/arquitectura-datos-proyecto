# Consideraciones sobre el proyecto Rita

## 1. Conceptualización general del problema

**Liliana:**

* **Producto de datos:** Si pueden evitar tener regresión será méjor. No hay problema si tienen muchas categorías a clasificar, lo que necesitarán hacer es un modelo por cada categoría para convertirlo en un binario y poder entender a fondo el *performance* de cada clase, si hacen un solo modelo multinomial no queda claro cuándo lo hace bien, ni se distingue en que lo hace muy mal.

**Responsable:** todos

**Comentario:** Evaluar la cantidad de clases a considerar y el performance de los modelos sobre ellos, basado en alguna métrica. Ver puntos siguientes.

## 2. Conceptualización de categorías

**Liliana:**

+ El número de categorías tendrá que definirse pensando en el beneficio a su usuario, en su caso, tiene sentido que su vuelo se atrasará 15 minutos? no creo. Sin embargo decirle que se atrasará 1 hora y media puede permitirle tomar una junta o salir después de hora pico en el transporte, etc. beneficios tangibles en su toma de decisión.

+ Considero que la cota inferior de demora debe ser de 1.5 horas, y de ahí definan cuántas categorías, por ejemplo más de 3.5 horas supongo que tienen un tratamiento diferente?? en cuyo caso puede haber retraso de 1.5 a 2.5 horas, 2.5 horas a 3.5 horas y mayores a 3.5 horas. A estas categorías falta agregarle la de cancelado. Eso implica 4 categorías totales.

**Responsable:** Danahi y León

**Comentario:** 

* Explorar los datos para caracterizar los tiempos de retraso e intentar motivar los intervalos.
* Intentar verificar otras fuentes (encuestas,  otras fuentes que describan el servicio),
* En último caso, aceptar las categorías propuestas por Liliana.

## 3. Evaluación de costos de categorías y métricas para modelos

**Liliana:**

+ Habrá que definir para cada categoría qué tipo de error es el más costoso, por ejemplo, es muy evidente que equivocarnos en el modelo de cancelación en un FN implica que el usuario perdió su vuelo :( y puede haber una posible demanda a este servicio y a la aerolínea..

**Responsable:** Danahi y León

**Comentario:** 

* Explorar los datos para caracterizar los tiempos de retraso e intentar motivar los intervalos.
* Intentar verificar otras fuentes (encuestas,  otras fuentes que describan el servicio),
* En último caso, aceptar las categorías propuestas por Liliana.

## 4. Evaluación de métricas para modelos

**Liliana:**

+ Definan qué métrica de desempeño será la que definirá si cada modelo es "bueno" o "malo". (Precision, Recall, F1-score o Fbeta-score).

**Responsable:** Paola + Luis + César

**Comentario:** 

* Creo que hemos acordado explicar 

## 5. Frecuencia de emisión de recomendación

**Liliana:**

+ Definan la frecuencia de emisión de recomendación, por ejemplo puede ser on demand (dado que lo quieren asociar a una app móvil) o cada hora? en este segundo escenario son más preventivos y no están esperando que el usuario sea el que pregunte... eso cambia también su producto???????

**Responsable:** todos

**Comentario:** 

* Creo que hemos acordado explicar que se hará semanal; dado que buscaremos nuevos datos mensuales en el pipeline. No es posible hacer predicciones diarias, dado que los datos llegan con delay (aunque la documetación diga que son mensuales.)

### 6. EC2 y archivos temporales

**Liliana:**

+ **ETL:** No es necesario guardar archivos en el EC2 y luego pasarlos al lugar donde se almacenarán los datos, aún y cuando los borren una vez ocupados. El EC2 solo debe ser ocupado como procesamiento de Luigi, no como almacenador (ni siquiera temporal)

**Responsable:** todos

**Comentario:** ya no aplica, dado que el orquestador ahora escribe directamente de la API de Rita al S3, guardando un .zip con todos los datos por cada mes..

### 7. Reescribir pregunta a resolver como enunciado con objetivos

**Liliana:**

+ Escriban la pregunta que quieren resolver a través de este producto de datos como un enunciado de objetivo(s). A través de ese enunciado deberán definir los KPIs, el usuario final, el producto, la frecuencia de emisión.

**Responsable:** Paola + Luis + César

**Comentario:** Reescribir el problema en términos de lo que Liliana sugiere "enunciado con objetivos", ligado a KPI's + quién sería el usuario final + qué sería el producto + frecuencia de emisión.

### 8. Corte de información a tentativamente 5 años

**Liliana:**

+ Definan si van a ocupar todos los años de información o solo una parte? en caso de la última, a partir de qué año y cuál es la justificación asociada.

**Responsable:** todos

**Comentario:** Estudiar los datos de últimos 5 años, para ver como motivar que vamos a cortarlos desde este punto.
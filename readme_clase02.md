Actividad Clase 2: 


1) ¿Qué problema resuelve la técnica de hoy?

La complejidad práctica y el conteo de operaciones resuelven la necesidad de anticipar cómo se comportará un algoritmo al escalar el tamaño de la entrada. Permiten evaluar formalmente el costo computacional teórico y empírico más allá del tiempo cronológico del hardware, optimizando la toma de decisiones técnicas.


2) Archivo de Código y Pruebas
Se implementó el archivo con las funciones analizadas en la sesión y sus respectivas pruebas de validación:
- sumar y max_: Recorren la colección de datos de manera lineal. O(n)
- contar_pares_iguales: Utiliza ciclos anidados para comparar pares de elementos. O(n2)
- cuantos_halves: Modela un crecimiento logarítmico dividiendo el valor de entrada sucesivamente por 2. O(log n)
- medir: Utiliza la librería time (perf_counter) para complementar el análisis mediante la medición de tiempos reales de ejecución.

Casos de prueba incluidos:
1. Prueba 1: Medición de tiempo y ejecución para operaciones de orden lineal O(n) como suma y búsqueda de máximo.
2. Prueba 2: Evaluación de costos en ciclos anidados mediante el conteo de pares duplicados en una lista.
3. Prueba 3: Comprobación del orden logarítmico O(log n) utilizando potencias de 2 (como el número 64) para verificar las divisiones sucesivas.


3) Dificultad técnica y Decisión de diseño
Al estructurar la función de medición de tiempos (perf_counter) con funciones que reciben distintos tipos de parámetros (algunas listas y otras números enteros), un desafío menor fue adaptar los bloques de prueba para que cada algoritmo pudiera ser medido de forma correcta sin desbordar la consola.
Se optó por encapsular la lógica de medición en una función auxiliar (medir), lo que permite reutilizar el código de control de tiempo con cualquier algoritmo y separar claramente el análisis teórico de las variaciones del entorno de hardware.

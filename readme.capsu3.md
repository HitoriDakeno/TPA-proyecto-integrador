Pregunta y respuesta de la capsula 1 de recursión:

1. Determinar el orden de cinco fragmentos de código.

R: 

Si hay un ciclo simple que recorre hasta n, es O(n) lineal


2. Explicar por qué 3n+20 y 100n pertenecen al mismo orden.

R: El 3 de 3n y el 100 de 100n se desprecian porque, cuando n crece muchísimo, el factor numerico deja de
importar frente a la tendencia de crecimiento. El +20 es una constante fija que no depende de n.
Por lo tanto, al eliminar constantes y términos menores, ambas expresiones se reducen simplemente a O(n)


3. Diseñar un experimento que no confunda costo de preparación con costo del algoritmo.

R: Como se responde: Para medir el tiempo real de un algoritmo sin que afecte el rendimiento inicial, el diseño del experimento debe separar la fase de configuración de la fase de medición:

Que hacer: Cargar archivos, generar listas grandes o preparar las variables antes de iniciar el cronómetro.

Medición limpia: Usar funciones de alta precisión (como time.perf_counter()) encerrando únicamente la llamada a la función del algoritmo que se quiere evaluar, evitando que el tiempo de impresión en pantalla o la creación de datos altere el resultado final.



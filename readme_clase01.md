Actividad clase 1:

1. ¿Qué problema resuelve la técnica de hoy?
la técnica de hoy vista en clases son dos métodos, una búsqueda lineal y binaria de un objetivo, la primera es mas simple pero menos eficiente que la binaria para búsquedas inmensas, aunque la binaria requiere que la lista de elementos este ordenada.


2. En este repositorio se encientra el archivo "clase01_pruebas_rut.py", el cual implementa:
búsqueda lineal: recorre elementos uno por uno, ideal para listas desordenadas.
búsqueda binaria: divide el espacio de búsqueda a la mitad iterativamente, requiere que la lista este ordenada.
Tests: se incluyen 3 tests.


3. Dificultad técnica y decisión de diseño
Al implementar la búsqueda binaria y el ordenamiento manual, un obstáculo común fue controlar correctamente los limites de los índices (izq,der,medio), lo que en un inicio podría generar bucles infinitos o errores fuera de rango si la lista cambiaba de tamaño.
Se decidio estructurar el código en funciones independientes y reutilizables, separando la lógica de búsqueda de la estructura de datos, y validando explícitamente las condiciones de salida(-1 cuando el elemento no es encontrado) para asegurar la estabilidad del programa.
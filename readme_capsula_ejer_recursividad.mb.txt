PARTE 1:

1.1 Concepto base: Explique con sus propias palabras la diferencia entre el caso base y el paso
recursivo. ¿Qué ocurre en la pila de llamadas (call stack) si una función recursiva carece de
un caso base alcanzable?

R: El caso base es la condición de termino que resuelve el problema de forma directa y trivial sin realizar mas llamadas recursivas. 
El paso recursivo es la regla mediante la cual la función se llama a si misma reduciendo el problema hacia el caso base.


1.2 Traza de ejecución: Dado el algoritmo de Euclides para el máximo común divisor (mcd(a,b) que retorna mcd(b, a % b) 
si b != 0), realice la traza manual detallando cada llamada recursiva en la pila para la ejecución de mcd(48, 18) hasta llegar al resultado final.

R:
mcd(48, 18) -> b = 18 != 0, retorna mcd(18, 48 % 18) = mcd(18, 12)
mcd(18, 12) -> b = 12 != 0, retorna mcd(12, 18 % 12) = mcd(12, 6)
mcd(12, 6) -> b = 6 != 0, retorna mcd(6, 12 % 8) = mcd(6, 0)
mcd(6, 0) -> b = 0, se alcanza el caso base y retorna abs(6) = 6


1.3 Desarrollo de código: Escriba una función recursiva en Python llamada invertir_cadena(s,
i, j) que invierta una cadena de texto (o lista de caracteres) intercambiando los elementos
en los índices i y j. No utilice ciclos for ni while.

R: código subido al repositorio con test 


1.4 Análisis de eficiencia: Explique detalladamente por qué la implementación recursiva ingenua de la sucesión de Fibonacci (Fn = Fn−1 + Fn−2) es ineficiente.
Dibuje el árbol de llamadas para fib(5) para respaldar su argumento.

R: La forma recursiva ingenua Fn = Fn-1 + Fn-2 es ineficiente porque recalcula multiples veces los mismos valores de forma independiente.
La computadora no almacena ni recuerda los resultados que ya calculo en una rama anterior, por lo que vuelve a repetir todo el proceso 
desde cero cada vez que lo necesita. Esto provoca que el numero de llamadas crezca de manera exponencial a medida que n aumenta.

                  fib(5)
                /        \
          fib(4)          fib(3)  <-- Aquí aparece fib(3) por primera vez
         /      \        /      \
   fib(3)        fib(2) fib(2)   fib(1)  <-- fib(3) y fib(2) se repiten
   /    \        /    \  /    \
fib(2)  fib(1) fib(1) fib(0) ... (sigue ramificándose)


1.5 Costo oculto: Explique la diferencia de complejidad temporal y espacial entre recorrer una
lista recursivamente pasando un índice (ej. func(lista, i+1)) versus recorrerla pasando
una sublista mediante slicing (ej. func(lista[1:])).

R: pasar un índice tiene un costo temporal y espacial de O(1) por llamada, ya que solo se pasa un puntero numerico entero 
como argumento sin duplicar datos. Pasar una sublista por slicing obliga a Python a copiar físicamente los elementos restantes 
en un bloque de memoria nuevo en cada paso, elevando el costo temporal y espacial a un orden cuadratico O(n2).


PARTE 2:

2.1 Concepto estructural: ¿Por qué el paradigma recursivo es naturalmente adecuado para
procesar estructuras como documentos JSON o sistemas de archivos (carpetas y subcarpetas)?

R: El paradigma recursivo es adecuado porque estas estructuras son jerárquicas y contienen elementos dentro de otros. La recursividad
permite procesar cada elemento y volver a aplicar el mismo procedimiento a sus subelementos, sin importar cuantos niveles de profundidad existan.


2.2 Desarrollo de código: Escriba una función recursiva profundidad_maxima(x) que reciba
una lista que puede contener otras listas anidadas en múltiples niveles (ej. [1, [2, [3, 4]],
5]) y retorne la profundidad máxima de la estructura. Un elemento simple tiene profundidad
0.

R: código subido con el test

2.3 Desarrollo de código: Implemente una función recursiva extraer_enteros(estructura)
que reciba un diccionario anidado (que puede contener listas y otros diccionarios) y retorne
una única lista plana con todos los valores de tipo entero (int) que encuentre.

R: código subido con el test

2.4 Complejidad en estructuras: Si una estructura anidada tiene un total de N elementos
(contando tanto los contenedores como los valores simples o primitivos), justifique por qué
el costo de recorrerla completamente con una función recursiva bien diseñada es O(N).

R: El costo es O(N) porque la función recorre cada elemento de la estructura una sola vez. Cada elemento 
realiza una cantidad constante de trabajo y, aunque haya llamadas recursivas, en total se procesan los n elementos, por lo que la complejidad es O(n).


PARTE 3:

3.1 Interpretación de recurrencias: Explique qué comportamiento algorítmico modela la
relación de recurrencia T(n) = T(n − 1) + O(1). Dé un ejemplo de una función recursiva
estudiada en clases que posea este costo temporal.

R: La relacion T(n) = T(n-1) + O(1) modela un algoritmo que reduce el tamaño del problema de uno en uno cada paso,
realiando una cantidad constante de trabajo por iteración, ejemplo: la suma de una lista mediante índice, el factorial, o la potencia linal.


3.2 Método de expansión: Resuelva paso a paso la siguiente relación de recurrencia utilizando
el método de expansión o iteración:
                       T(n) = T(n/2) + c
(Asuma T(1) = c). Indique a qué orden de complejidad Big-O pertenece.


R: se expande n/2 en n -> T(n/2) = T(n/4) + c

pues quedaría:
   
   T(n) = T(n/4) + c + c
   T(n) = T(n/4) + 2c

se vuelve a expandir:
   T(n/4) = T(n/8) + c
 
se reemplaza:
   T(n) = T(n/8) + c + 2c
   T(n) = T(n/8) + 3c

.
.
.

se podría seguir asi sucesivamente, asi que quedaría de esta forma:

   T(n) = T(n/2^k) + kc

la recursión termina cuando se llega al caso base:
    T(1) = c

se quiere:
    n / 2^k = 1

despejando:
   n = 2^k

aplicando log base 2:
   k = log2(n)


queda: T(n) = c + clog2(n)

ósea es de orden: O(log n)


3.3 Modelado matemático: Un algoritmo divide un arreglo de tamaño n en tres partes iguales,
realiza una llamada recursiva solo en una de esas partes y luego hace un trabajo adicional
que toma tiempo constante O(1). Escriba la relación de recurrencia T(n) para este algoritmo
y determine su complejidad.

R: T(n) = T(n/3) + O(1)

= T(n) = T(n/3) + c

= T(n) = T(n/9) + 2c

= T(n) = T(n/27) + 3c

.
.
.
  T(n) = T(n/3^k) + kc

el caso base es cuando: 
     n/3^k = 1


por tanto

   n = 3^k
   k = log3(n)


entonces
   T(n) = T(1) + clog3(n)


complejidad temporal: O(log n)


3.4 Árbol de recursión: Dibuje los primeros tres niveles del árbol de recursión para la relación
T(n) = 2T(n/2) + O(n). Determine cuánto trabajo se realiza en cada nivel y justifique por
qué el costo total resulta en O(n log n).

R:

Nivel 0:                 T(n)
                       /    \
                      /      \
Nivel 1:          T(n/2)    T(n/2)
                  /   \      /   \
                 /     \    /     \
Nivel 2:     T(n/4) T(n/4) T(n/4) T(n/4)


en cada nivel se realiza un trabajo de O(n)

la profundidad del árbol es log2(n)

el costo total es: O(n) * O(log n) = O(n log n)



3.5 Comparación de potencias: En clases se vio que calcular a
n mediante potencia lineal
tiene costo T(n) = T(n − 1) + O(1), mientras que la potencia rápida tiene costo T(n) =
T(n/2) + O(1). Demuestre, evaluando ambas recurrencias para n = 1024, cuántas llamadas
recursivas realiza aproximadamente cada algoritmo.

R: 

Potencia lineal (T(n) = n): Realiza exactamente 1024 llamadas recursivas.
Potencia rápida (T(n) = log2n): Realiza log2(1024) = 10 llamadas recursivas.



PARTE 4:

4.1 Patrón algorítmico: Describa los tres pasos fundamentales del paradigma "Dividir para
Conquistar"(Dividir, Resolver, Combinar). Aplique esta descripción para explicar conceptualmente cómo funciona el algoritmo Merge Sort.

R:

1. Dividir: Se divide el problema original en problemas mas pequeños.
2. Resolver: Se resuelven los problemas pequeños, normalmente mediante recursividad.
3. Combinar: Se juntan las soluciones de los problemas pequeños para obtener la solución del problema original

por ejemplo en MergeSort

Dividir: El arreglo se divide en dos mitades
Resolver: Cada mitad se ordena recursivamente usando Merge Sort
Combinar: Se mezclan las dos mitades ya ordenadas para formar un único arreglo ordenado.


4.2 Traza de combinación (Merge): Dadas las listas ordenadas izq = [2, 5, 9] y der =
[1, 6, 8], realice la traza manual de la función merge(izq, der), mostrando cómo avanzan
los índices y cómo se construye la lista resultante paso a paso.

R:

índices iniciales: i =0, j =0


izq[i] = 2 , der[j] = 1

se agrega 1 -> [1]

izq[i] = 2 , der[j] = 6

se agrega 2 -> [1,2]

izq[i] = 5 , der[j] = 6

se agrega 5 -> [1,2,5]

izq[i] = 9 , der[j] = 6

se agrega 6 -> [1,2,5,6]

izq[i] = 9 , der[j] = 8

se agrega 8 -> [1,2,5,6,8]

der ya no tiene elementos, queda solo el 9 de izq, se agrega:

[1,2,5,6,8,9]




4.3 Estabilidad algorítmica: Defina qué significa que un algoritmo de ordenamiento sea "estable". Explique por qué Merge Sort
es estable (si se implementa correctamente la condición <=) y proporcione un ejemplo de la vida real donde la estabilidad sea necesaria.

R: Un algoritmo de ordenamiento es estable cuando, si dos elementos tienen la misma clave de ordenamiento, mantiene entre 
ellos el mismo orden relativo que tenían originalmente.

Merge Sort es estable si en la etapa de combinación se utiliza la condición <=. Así, cuando dos elementos tienen el mismo 
valor, se toma primero el elemento de la lista izquierda, manteniendo su orden original.

Ejemplo de la vida real: ordenar una lista de estudiantes primero por curso y después por apellido. Si varios estudiantes
pertenecen al mismo curso, la estabilidad permite conservar el orden por apellido que ya tenían, evitando alterar innecesariamente el orden entre ellos.




4.4 Análisis de QuickSort: El rendimiento de QuickSort depende críticamente de la elección
del pivote. Contraste el árbol de llamadas recursivas de QuickSort en el mejor caso frente
al peor caso. ¿Cuál es la relación de recurrencia para ambos escenarios?


R:

Mejor caso: El pivote divide el arreglo exactamente a la mitad simétrica, generando la recurrencia T(n) = 2T(n/2) + O(n), con un costo de O(n log n)

Peor caso: El pivote es el elemento extremo (menor o mayor), generando un desbalance total con la recurrencia T(n) = T(n-1) + O(n), cuyo costo asciende a O(n2)



4.5 Desarrollo conceptual (Búsqueda Binaria): Modifique conceptualmente el algoritmo
de búsqueda binaria para que, en lugar de retornar el índice de un elemento si lo encuentra,
retorne la cantidad total de veces que un número aparece en un arreglo ordenado (asuma
que hay elementos repetidos). ¿Se mantiene la complejidad en O(log n)? Explique.

R: Se puede adaptar encontrando por separado la primera posición y la ultima posición del elemento mediante búsquedas binarias modificadas. 
La cantidad total de apariciones se obtiene restando ambos índices (mas uno). La complejidad se mantiene en O(log n) (o O(log n + k)
si se recorren linealmente las repeticiones k)





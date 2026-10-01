#David Villalobos - 21.646.173-8

#clase 2 - pruebas


from time import perf_counter


def sumar(datos): #orden: O(N)
    total = 0     #crece linealmente: T(n) = an + b
    for x in datos:
        total += x
    return total


def contar_pares_iguales(datos): 
    c = 0                        # O(n2)
    for i in range(len(datos)):  #dos ciclos anidados
        for j in range(i+1,len(datos)):
            if datos[i] == datos[j]:
                c += 1
    return c

def cuantos_halves(n): #k ~~ log2 n => O(log n)
    c = 0
    while(n>1):
        n = n // 2
        c += 1
    return c

def max_(datos): # busca el maximo de un lista elemento por elemento O(n)
    max_ = datos[0]
    for i in range(len(datos)):
        if datos[i] > max_:
            max_ = datos[i]
    return max_



def medir(funcion, datos): #funcion para medir el tiempo que demora en ejecutar la tarea una funcion, puede variar.
    inicio = perf_counter()
    result = funcion(datos)
    fin = perf_counter()
    return result, fin-inicio


print("=== INICIANDO PRUEBAS CLASE 2 ===\n")

# Prueba 1: Probar la suma y el máximo con medición de tiempo O(n)
lista_numeros = [4, 12, 7, 25, 9, 3]
res_suma, tiempo_suma = medir(sumar, lista_numeros)
res_max, tiempo_max = medir(max_, lista_numeros)

print("Prueba 1 Lineal O(n):")
print(f" -> Suma de {lista_numeros} = {res_suma} (Demoró {tiempo_suma:.8f}s)")
print(f" -> Máximo de {lista_numeros} = {res_max} (Demoró {tiempo_max:.8f}s)\n")

# Prueba 2: Probar conteo de pares iguales con elementos repetidos O(n^2)
lista_con_repetidos = [1, 2, 2, 3, 1]
res_pares, tiempo_pares = medir(contar_pares_iguales, lista_con_repetidos)
print("Prueba 2 Cuadrática O(n^2):")
print(f" -> Pares iguales encontrados en {lista_con_repetidos} = {res_pares} (Demoró {tiempo_pares:.8f}s)\n")

# Prueba 3: Probar el crecimiento logarítmico con 'cuantos_halves' O(log n)
# Nota: Como 'cuantos_halves' recibe un número entero y no una lista, lo medimos directo.
n_prueba = 64
inicio_h = perf_counter()
res_halves = cuantos_halves(n_prueba)
fin_h = perf_counter()
tiempo_halves = fin_h - inicio_h

print("Prueba 3 Logarítmica O(log n):")
print(f" -> Divisiones por 2 para llegar a 1 desde {n_prueba} = {res_halves} (Demoró {tiempo_halves}s)")








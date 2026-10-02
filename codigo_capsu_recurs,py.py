#codigo de problema 1.3

def invertir_cadena(s,i,j):
    if(i>=j):
        return 
    s[i], s[j] = s[j],s[i]
    invertir_cadena(s, i+1, j-1)
    
#test:
letras = ["h", "o", "l", "a"]

invertir_cadena(letras, 0, len(letras) - 1)

print(letras)  # Muestra: ['a', 'l', 'o', 'h']

print("="*30)
#codigo de problema 2.2

def profundidad_maxima(x):
    maximo = 0

    for elemento in x:
        if isinstance(elemento, list):
            profundidad = profundidad_maxima(elemento) + 1

            if profundidad > maximo:
                maximo = profundidad

    return maximo


lista = [1, [2, [3, 4]], 5]

print(profundidad_maxima(lista)) #porque [3, 4] esta en profundidad 2

print("="*30)
#codigo de problema 2.3

def extraer_enteros(estructura):
    enteros = []

    if isinstance(estructura, dict):
        for valor in estructura.values():
            enteros += extraer_enteros(valor)

    elif isinstance(estructura, list):
        for elemento in estructura:
            enteros += extraer_enteros(elemento)

    elif isinstance(estructura, int):
        enteros.append(estructura)

    return enteros

datos = {
    "edad": 22,
    "notas": [5, 6, {"numero": 10}],
    "nombre": "Juan"
}

print(extraer_enteros(datos))

print("="*30)
#codigo problema 4.6

def maximo_dc(arreglo, lo, hi):

    if lo == hi:
        return arreglo[lo]

    medio = (lo + hi) // 2

    max_izq = maximo_dc(arreglo, lo, medio)
    max_der = maximo_dc(arreglo, medio + 1, hi)

    if max_izq > max_der:
        return max_izq
    else:
        return max_der

#La función sigue dividiendo hasta llegar a un solo elemento. 
#Cuando lo == hi, significa que queda un solo elemento, 
#por lo que ese elemento es el máximo de esa pequeña parte.


arreglo = [4, 8, 2, 10, 5, 7]

resultado = maximo_dc(arreglo, 0, len(arreglo) - 1)

print(resultado)

#relacion de recurrencia: T(n) = 2T(n/2) + O(1), la cual pertenece a una
#complejidad temporal de O(n)


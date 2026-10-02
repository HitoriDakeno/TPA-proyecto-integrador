from __future__ import annotations


def contar_digitos(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        n = -n
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


def invertir(texto: str) -> str:
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir(texto[:-1])


def fragmento_a(n: int) -> int:
    contador = 0
    i = 1
    while i < n:
        contador += 1
        i *= 2
    return contador


def fragmento_b(n: int) -> int:
    contador = 0
    for i in range(n):
        for _ in range(i, n):
            contador += 1
    return contador


#USTIFICACIÓN DEL ORDEN ASINTÓTICO:
#
# 1. fragmento_a(n):
#    - La variable 'i' comienza en 1 y se multiplica por 2 en cada iteración (1, 2, 4, 8...).
#    - El ciclo corre k veces hasta que 2^k >= n, lo que significa que k = log2(n).
#    - Orden asintótico: O(log n) (Crecimiento logarítmico).
#
# 2. fragmento_b(n):
#    - El ciclo externo se ejecuta n veces. El ciclo interno se ejecuta (n - i) veces por cada vuelta.
#    - Esto genera una sumatoria aritmética: n + (n-1) + (n-2) + ... + 1.
#    - La fórmula matemática de esta suma es n*(n + 1) / 2 = (n^2 + n) / 2.
#    - Al aplicar las reglas asintóticas (descartar constantes y el término menor), queda el término dominante n^2.
#    - Orden asintótico: O(n^2) (Crecimiento cuadrático).
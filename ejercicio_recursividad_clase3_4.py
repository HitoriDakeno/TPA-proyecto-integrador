from __future__ import annotations

def potencia(a,n):
    if n == 0:
        return 1
    return a * potencia(a, n-1)
    

#1. cual es el caso base?

#R: ocurre cuando el exponente es cero (n==0), retornando directamente 1

#2. cual es el paso recursivo?

#R: multiplicar la base "a" por la funcion llamada con el exponente disminuido en uno

#3. traza de potencia(2,4):
    
# potencia(2, 4) -> 2 * potencia(2, 3)
# potencia(2, 3) -> 2 * potencia(2, 2)
# potencia(2, 2) -> 2 * potencia(2, 1)
# potencia(2, 1) -> 2 * potencia(2, 0)
# potencia(2, 0) -> 1 (caso base)

#retornos:
#potencia(2, 1) = 2 * 1 = 2
#potencia(2, 2) = 2 * 2 = 4
#potencia(2, 3) = 2 * 4 = 8
#potencia(2, 4) = 2 * 8 = 16 (resultado final)

#print(potencia(2, 4)) #imprime 16

#4. Cuántas llamadas realiza aproximadamente para un exponente n?

#Realiza n + 1 llamadas (complejidad temporal O(n)), ya que
#el exponente disminuye de uno en uno en cada paso.

#5. Compare con potencia rápida

#La potencia lineal hace O(n) llamadas restando de 1 en 1. La potencia rápida 
#divide el exponente a la mitad en cada paso (n / 2), reduciendo drásticamente 
#el costo computacional a un orden logarítmico O(log n).


def potencia_rapida(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        # Si n es par: (a^(n/2))^2
        mitad = potencia_rapida(a, n // 2)
        return mitad * mitad
    else:
        # Si n es impar: a * (a^((n-1)/2))^2
        mitad = potencia_rapida(a, (n - 1) // 2)
        return a * mitad * mitad



print("=== PRUEBAS DE POTENCIAS RECURSIVAS ===")
    
# Probando potencia lineal
res_lineal = potencia(2, 4)
print(f"Potencia lineal (2^4) = {res_lineal}")
    
# Probando potencia rápida
res_rapida = potencia_rapida(2, 10)
print(f"Potencia rápida (2^10) = {res_rapida}")


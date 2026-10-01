#ejercicios estudiantes de la unidad 1 de introduccion

from __future__ import annotations

#Retorna la primera posición del objetivo o -1 si no se encuentra.
def primera_posicion(datos: list[int], objetivo: int) -> int:
    for i, valor in enumerate(datos):
        if valor == objetivo:
            return i
    return -1



# Propone una solución utilizando un conjunto (set).
# Costo temporal: O(n), ya que recorrer la lista para transformarla a set toma tiempo lineal.
# Costo espacial: O(n), por el almacenamiento temporal de los elementos en el set.


def contiene_duplicados(datos: list[int]) -> bool:
    return len(datos) != len(set(datos))



#Agrupa palabras por su longitud sin duplicar palabras dentro de cada grupo.
def agrupar_por_longitud(palabras: list[str]) -> dict[int, list[str]]:
    grupos: dict[int, list[str]] = {}
    
    for palabra in palabras:
        largo = len(palabra)
        if largo not in grupos:
            grupos[largo] = []
        
        # Evita duplicados dentro de la lista del grupo respectivo
        if palabra not in grupos[largo]:
            grupos[largo].append(palabra)
            
    return grupos


# Calcula el promedio de los valores.
# Decisión ante lista vacía: Retorna 0.0 para documentar y prevenir un error 
# de división por cero (ZeroDivisionError).
def promedio(valores: list[float]) -> float:
    if not valores:
        return 0.0
        
    return sum(valores) / len(valores)
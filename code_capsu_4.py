#codigos de la capsula 2 de recursion:
    
def contar_digitos(n):
    if n < 0:
        n = -n
    
    
    if n < 10:
        return 1
    
    return 1 + contar_digitos(n // 10)


print(contar_digitos(10)) ## 2 digitos (imprime 2)
print(contar_digitos(100)) ## 3 digitos (imprime 3)



def invertir_cadena_texto(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + invertir_cadena_texto(s[:-1])

print(invertir_cadena_texto("hola mundo"))



#El uso de lista[1:] agrega costo adicional ya que python no se limita
#a apuntar al siguiente elemento, sino que crea una copia fisica de todos
#los elementos restantes de un espacio de memoria nuevo.

#IMPACTO: si una lista tiene un tamaño n, hacer esto en cada llamada 
#recursiva obliga a duplicar datos una y otra vez, elevando el costo 
#temporal de un eficiente O(n) a un costoso O(n2), ademas de
#consumir mucha mas memoria de la necesaria en la pila de llamadas.
#Por eso siempre es preferible avanzar usando un indice (como i+1).


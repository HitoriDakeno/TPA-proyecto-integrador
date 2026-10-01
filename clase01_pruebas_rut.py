#David Villalobos 21.646.173-8

#clase 1 - pruebas

def buscar_lineal(datos, obj):
    for i, valor in enumerate(datos):
        if valor == obj:
            return i
    return -1


def buscar_binaria(datos, obj):
    izq, der = 0, len(datos) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if datos[medio] == obj:
            return medio
        if datos[medio] < obj:
            izq = medio + 1
        else:
            der = medio - 1
    return -1


# Datos de prueba
estudiantes = ["david", "chatGPT", "Grok"]
ruts = ["1234", "4321", "4312"]


print("=== EJECUCIÓN DE TESTS ===\n")

# --- TEST 1: RUT que SÍ existe (Búsqueda Lineal) ---
print("Test 1: Buscando un RUT existente")
rut_buscado_1 = "1234"
pos_1 = buscar_lineal(ruts, rut_buscado_1)

if pos_1 != -1:
    print(f"Resultado: Estudiante encontrado -> {estudiantes[pos_1]}")
else:
    print("No encontrado")

print("")

# --- TEST 2: RUT que NO existe (Caso no encontrado) ---
print("Test 2: Buscando un RUT que no está en la lista")
rut_buscado_2 = "9999"
pos_2 = buscar_lineal(ruts, rut_buscado_2)

if pos_2 != -1:
    print(f"Resultado: Estudiante encontrado -> {estudiantes[pos_2]}")
else:
    print("Resultado: RUT no encontrado (Funciona el -1 correctamente!)")

print("")

# --- TEST 3: Búsqueda Binaria con lista ordenada ---
print("Test 3: Usando búsqueda binaria con lista ordenada de RUTs")
ruts_ordenados = ["1234", "4312", "4321"]  # Lista ya ordenada
rut_buscado_3 = "4312"
pos_binaria = buscar_binaria(ruts_ordenados, rut_buscado_3)

print(f"Buscando '{rut_buscado_3}' con búsqueda binaria -> Encontrado en el índice: {pos_binaria}")



# Diccionario de equivalencias: diferentes formas de escribir
# un medicamento se convierten a un solo nombre estándar.
EQUIVALENCIAS = {
    "ACETAMINOFEN": "ACETAMINOFÉN",
    "PARACETAMOL": "ACETAMINOFÉN",
    "PANADOL": "ACETAMINOFÉN",
    "MOTRIN": "IBUPROFENO",
    "SALIR": "N",
}

def limpiar_nombre(nombre):
    nombre = nombre.upper().strip()
    nombre = EQUIVALENCIAS.get(nombre, nombre)
    # return entrega el resultado al lugar donde se llamó la función.
    return nombre

# La lista comienza vacía.
# Aquí guardaremos cada medicamento después de limpiarlo.
medicamentos = []

# El ciclo permite ingresar varios medicamentos.
# True mantiene el ciclo activo hasta que ejecutemos break.
while True:
    # input() recibe lo que escribe la persona como una cadena de texto.
    medicamento = input(
        "Ingrese el nombre del medicamento o 'n' para salir: "
    )

    # Llamamos a la función y guardamos el resultado en la misma variable.
    # En este punto se limpian los espacios, se convierten las mayúsculas
    # y se aplica la equivalencia cuando existe.
    medicamento = limpiar_nombre(medicamento)

    # Una entrada como "n", "N" o "salir" termina convertida en "N".
    # break termina el ciclo antes de agregar esa entrada a la lista.
    if medicamento == "N":
        break

    # Si la persona presiona Enter sin escribir un nombre, la cadena queda
    # vacía. continue vuelve al inicio del ciclo para pedir otra entrada.
    if medicamento == "":
        print("Escriba un nombre de medicamento.")
        continue

    # append() agrega el medicamento limpio al final de la lista.
    # Las entradas repetidas también se guardan para poder contarlas después.
    medicamentos.append(medicamento)

    # Mostramos el nombre que realmente quedó guardado.
    print("Medicamento registrado:", medicamento)

# Esta parte se ejecuta después de salir del ciclo.
print("\nMedicamentos registrados:")
print(medicamentos)

# También podemos llamar a la función directamente dentro de print().
# Como esta frase no está en el diccionario, solo se limpia y pasa a mayúsculas.
print(limpiar_nombre("     fin del programa  "))

# Mantiene abierta la terminal hasta que la persona presione Enter.
input("Presione Enter para salir...")

"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
sobre_promedio = 0
indice = 0
while indice < len(precios):
    if precios[indice] > promedio:
        sobre_promedio += 1
    indice += 1

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    clasificacion = "variación alta"
elif rango >= 150:
    clasificacion = "variación moderada"
else:
    clasificacion = "variación baja"

# TODO: Muestre producto y todos los resultados.
print(f"Producto: {producto}")
print(f"Promedio: ₡{promedio:.0f}")
print(f"Mínimo: ₡{minimo}")
print(f"Máximo: ₡{maximo}")
print(f"Rango: ₡{rango}")
print(f"Precios sobre el promedio: {sobre_promedio}")
print(f"Clasificación: {clasificacion}")
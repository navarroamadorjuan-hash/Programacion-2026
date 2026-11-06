"""Caso 1: cambio del consumo diario de agua. Complete el programa."""


consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
total = sum(consumos_litros)
promedio = total / len(consumos_litros)

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
# de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]

ahorro = primer_dia - ultimo_dia
porcentaje_reduccion = (ahorro / primer_dia) * 100

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
# de lo contrario, sin reducción.
if porcentaje_reduccion >= 15:
    clasificacion = "reducción alta"
elif porcentaje_reduccion > 0:
    clasificacion = "reducción moderada"
else:
    clasificacion = "sin reducción"

# TODO: Muestre los cinco resultados.
print(f"Total: {total} L")
print(f"Promedio diario: {promedio} L")
print(f"Ahorro: {ahorro} L")
print(f"Reducción: {porcentaje_reduccion:.0f} %")
print(f"Clasificación: {clasificacion}")
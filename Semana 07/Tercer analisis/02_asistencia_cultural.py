"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
total = 0
bloques_altos = 0
limite_70 = capacidad * 0.70

for asistencia in asistencias:
    total += asistencia
    if asistencia > limite_70:
        bloques_altos += 1

# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100

# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje >= 80:
    estado = "ocupación alta"
elif porcentaje >= 50:
    estado = "ocupación media"
else:
    estado = "ocupación baja"

# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
print(f"Total: {total}")
print(f"Promedio: {promedio:.0f}")
print(f"Porcentaje: {porcentaje:.0f} %")
print(f"Bloques: {bloques_altos}")
print(f"Estado: {estado}")
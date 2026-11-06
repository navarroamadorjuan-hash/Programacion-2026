"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

total_minutos = 0
conteo_categoria = {"Acceso": 0, "Equipo": 0, "Red": 0}
pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)

for incidencia in incidencias:
    total_minutos += incidencia["minutos_atencion"]
    conteo_categoria[incidencia["categoria"]] += 1

    if not incidencia["resuelto"]:
        pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))

    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])

promedio = total_minutos / len(incidencias) if incidencias else 0

print(f"Total casos: {len(incidencias)}")
print(f"Total minutos: {total_minutos}")
print(f"Promedio: {promedio:.0f}")
print(f"Conteo por categoría: {conteo_categoria}")
print(f"Pendientes: {pendientes}")
print(f"Provincias con pendientes: {provincias_pendientes}")
print(f"Casos urgentes: {casos_urgentes}")
print(f"Caso más largo: {caso_mas_largo}")
print(f"Hay pendientes en San Jose: {'San Jose' in provincias_pendientes}")
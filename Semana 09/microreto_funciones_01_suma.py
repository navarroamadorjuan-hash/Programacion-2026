"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        # TODO: acumule cada minuto en total.
        total += minuto 

    return total
total_minutos = sumar_esperas(ESPERAS)
total_horas = round(total_minutos / 60, 2)

print("Total de minutos:", total_minutos)
print("Total en horas:", total_horas)

#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.
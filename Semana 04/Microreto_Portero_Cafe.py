"""Microreto: el portero del café."""

nombre = input("Como te llamas?: ") .upper().strip()
energia = int(input("Cuánta energia tienes de 0 a 100: "))
trae_café = input("Traes café (si/no)?: ") .lower() .strip() =="si" 
mensaje = ""
#Si menos 50% y no tengo cafe: -> Descansar
if energia < 50 and not (trae_café):
    mensaje = "Descansar"

#Si 50% o mas o tengo cafe : -< Puedo ingresar a la clase
elif energia >=50 or (trae_café):
    mensaje = "Puedo ingresar a la clase"

#Cualquie otro ecenario : Portero confundido : revisar respuestas
else:
    mensaje = "Portero confundido : revisar respuestas"

print(f"{nombre}: {mensaje}")
    


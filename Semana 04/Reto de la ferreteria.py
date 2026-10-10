#Solución: Misión kit Seguro

nombre = input("Nombre: ").upper().strip()
kit = input('Tipo de kit: ').lower().strip()
autorizacion = input ("Tiene autorización (si/no)? ").lower().strip() == 'si'
try:
    cantidad = int(input("Cantidad de Kits?: "))
    if cantidad < 1:
        print("Error: la catididad minima es 1")
except ValueError:
    print("Cantidad de kits invalida, digite del 1 al 100")
    cantidad = -1
try:
    dias = int(input("Cantidad de días?: "))
except ValueError:
    print("Cantidad de días invalida, digite del 1 al 100")
    dias = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado: revise los datos ingresados!"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"Solititud aprobada para {nombre}: {cantidad} kit(s) de {kit}"
else:
    resultado = "Solicitud envidad a revisión"
    
print("-" * 50,'\n')
print(resultado)
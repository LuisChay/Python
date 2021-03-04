peso = float(input("Ingrese su peso en kg"))
altura = float(input("Ingrese su altura en m"))

imc=(peso/altura**2)

print("Tu indice de masa corporal es", round(imc,2))

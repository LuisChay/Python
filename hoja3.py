print("-----------------------------------")
print("Ejercicio #1")
contraseña1 = (input("Ingrese una contraseña "))

contraseña2 = (input("Ingrese una contraseña "))

if contraseña1.lower() == contraseña2.lower():
    print("Ambas contraseñas coinciden")
else:
    print("Ambas contraseñas no coinciden")

print("-----------------------------------")
print("Ejercicio #2")

nombre = input("Ingrese su nombre ")
genero = input("Ingrese su genero (M o H) ")

if genero == "M":
    if nombre.lower() < "m":
          grupo = "A"
    else:
          grupo = "B"
else:
    if nombre.lower() > "n":
          grupo = "A"
    else:
          grupo = "B"
print("tu grupo es", grupo)

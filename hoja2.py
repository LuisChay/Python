print("-----------------------------------")
print("Ejercicio #1")
numero = int(input("Ingrese el numero de filas que desea para su triangulo: "))

for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")
    
print("-----------------------------------")
print("Ejercicio #2")
inverso = int(input("Ingrese un numero: "))

while inverso >=0:
    print (inverso, end=",")
    inverso -= 1
print()

print("-----------------------------------")
print("Ejercicio #3")
entero = int(input("Ingrese un numero: "))           
def evaluar_primos(entero):
    contador=0
    resultado=True
    for i in range (1,entero+1):
        if (entero%i==0):
            contador+=1
        if(contador>2):
             resultado=False
             break
    return resultado
if (evaluar_primos(entero)==True):
    print ("el numero", entero, "es un numero primo")
else:
    print ("el numero", entero, "no es un numero primo")
print("-----------------------------------")

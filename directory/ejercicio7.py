import random

n = random.randint(0, 10)
respuesta = int(input("Trate de adivinar el número"))
intentos = 1
while respuesta != n:
    intentos = intentos + 1
    if respuesta > n:
        print("El número introducido es mayor del correcto, vuelva a probar")
        respuesta = int(input())
    else:
        print("El número introducido es menor del correcto, vuelva a probar")
        respuesta = int(input())
print("Lo has adivinando, el número de intentos que te ha llevado ha sido " + str(intentos))

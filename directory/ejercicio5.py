n = int(input("Introduzca un numero "))
e = 1
if n%3==0 or n%5==0:
    while e <= n:
        print(str(e) + " + " + str(n) + " es igual a " + str(e + n))
        e = e + 1
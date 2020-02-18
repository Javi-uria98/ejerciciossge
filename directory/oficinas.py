i=0
f=0
cont=0
contOficina=0
arrayfichero=""

dirFichero1 = 'C:\\Users\DAM\Desktop\ofi1.txt'
print("Primer fichero")
with open(dirFichero1, 'r') as reader:
    for line in reader:
        arrayfichero=arrayfichero+line
        cont=cont+1
        if cont==2:
            break

    alto = int(arrayfichero[:1])
    ancho = int(arrayfichero[1:])

    arrayfichero=""

    matrizOfi1 = [[0 for x in range(ancho)] for y in range(alto)]

    for line2 in reader:
        arrayfichero=arrayfichero+line2

    print(arrayfichero)
    print()

    for caracter in arrayfichero:
        print(caracter)
        if caracter!='\n':
            matrizOfi1[i][f]=caracter
            f=f+1
            if f>4:
                f=0
                i=i+1
    print(matrizOfi1)
    print()

    for posicion in matrizOfi1:
        for posicion2 in posicion:
            if posicion2=='1':
                contOficina=contOficina+1
            if posicion2=='0':
                contOficina=contOficina-1

    print("El numero de oficinas en el primer fichero es "+str(contOficina))


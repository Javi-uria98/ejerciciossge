diccionario = {}
with open("C:/Users/DAM/Desktop/diccionario.txt", "r+") as f:
    for line in f:
        command, description = line.strip().split(' ', 1)
        diccionario[command] = description.strip()
    print(diccionario)
    respuesta = int(input("Quiere introducir alguna palabra nueva al diccionario? (introduzca 1 si quiere o 0 si no quiere) "))
    while respuesta!=1 or respuesta!=0:
        if respuesta==1:
            #palabra = f.write(input("Introduzca la nueva palabra "))
            #definicion = f.write(input("Introduzca su definicion "))
            diccionario[input("Introduzca la palabra ")]=input("Introduzca la definicion de la palabra ")
            respuesta=int(input("Vuelva a introducir 1 o 0 en función de si quiere introducir más palabras o salir "))
        else:
            if respuesta==0:
                print("No ha querido introducir más palabras. Las palabras que tiene el diccionario son "+str(diccionario))
                respuesta2 = int(input("Quiere ahora buscar alguna palabra o desea salir? (1 para buscar por palabra o 0 para salir) "))
                if respuesta==1:
                    print(respuesta)
                    #me queda esta opción de buscar una palabra introduciendola por teclado y que me salga su definicion
                else:
                    if respuesta==0:
                        print("Fin del programa ")
                        break
                    else:
                        respuesta=int(input("No se ha indicado una respuesta correcta, vuelva a probar "))
            else:
                respuesta=int(input("No se ha indicado una respuesta correcta, vuelva a probar "))
    print(diccionario)



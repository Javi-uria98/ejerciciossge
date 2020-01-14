n = int(input("Indica el número de elementos que tendrá la lista"))
lista = ["Hola"] * n
for i in range(1, len(lista)):
    print("Indique el elemento en cuestión")
    lista[i] = input()
print(lista)

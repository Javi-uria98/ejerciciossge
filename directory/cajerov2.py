class cajero:
    def __init__(self, total, billetes):
        self.total = total
        self.billetes = billetes

    def inicializarcajero(self):
        self.billetes = [[10, 10], [20, 20], [50, 10]]
        self.total = sum(clave * valor for clave, valor in self.billetes)


class cliente:
    def __init__(self, dni, saldo):
        self.dni = dni
        self.saldo = saldo

    def registrarse(self):
        self.dni = input("Introduzca su dni")
        return self.dni


c = cajero(0, 0)
cli = cliente("", 0)

c.inicializarcajero()
dni = cli.registrarse()

if dni == "11111111X":
    print("Bienvenido cliente 1")
    cli = cliente("11111111X", 750)
    bucle = True
    while bucle:
        if int(input("¿Que operación desea realizar? (pulse 1 para sacar dinero o pulse 0 para salir)")) == 1:
            cantidad = int(input("¿Cuanto dinero quiere sacar? (introduzca la cantidad por teclado)"))
            if cantidad > cli.saldo:
                print("No tiene tanto saldo en el cajero")
            else:
                if cantidad % 10 != 0:
                    print("Recuerde, solo puede sacar dinero en múltiplos de 10")
                else:
                    for i in c.billetes:
                        if (cantidad % i[0] == 0) and ((i[0] * 10 - cantidad) >= 0):
                            i[1] = i[1] - (cantidad / i[0])
                            print("Quedan " + str(i[1]) + " billetes de " + str(i[0]) + " euros")
                            cli.saldo = cli.saldo - cantidad
                            c.total = c.total - cantidad
                            print("Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))


        else:
            print("Vuelva pronto")
            bucle = False

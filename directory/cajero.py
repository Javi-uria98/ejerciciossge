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
                    if ((cantidad <= (c.billetes[2][0] * c.billetes[2][1])) and (cantidad % c.billetes[2][0] == 0)) and (
                            c.billetes[2][0] * c.billetes[2][1] != 0):
                        numBillete = cantidad / c.billetes[2][0]
                        c.billetes[2][1] = c.billetes[2][1] - numBillete
                        cli.saldo = cli.saldo - cantidad
                        c.total = c.total - cantidad
                        print("Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))
                        print("Quedan " + str(c.billetes[2][1]) + " billetes de cincuenta euros")
                    else:
                        if ((cantidad <= (c.billetes[1][0] * c.billetes[1][1])) and (cantidad % c.billetes[1][0] == 0)) and (
                                c.billetes[1][0] * c.billetes[1][1] != 0):
                            numBillete = cantidad / c.billetes[1][0]
                            c.billetes[1][1] = c.billetes[1][1] - numBillete
                            cli.saldo = cli.saldo - cantidad
                            c.total = c.total - cantidad
                            print("Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))
                            print("Quedan " + str(c.billetes[1][1]) + " billetes de veinte euros")
                        else:
                            if ((cantidad <= (c.billetes[0][0] * c.billetes[0][1])) and (cantidad % c.billetes[0][0] == 0)) and (
                                    c.billetes[0][0] * c.billetes[0][1] != 0):
                                numBillete = cantidad / c.billetes[0][0]
                                c.billetes[0][1] = c.billetes[0][1] - numBillete
                                cli.saldo = cli.saldo - cantidad
                                c.total = c.total - cantidad
                                print(
                                    "Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))
                                print("Quedan " + str(c.billetes[0][1]) + " billetes de diez euros")
        else:
            print("Vuelva pronto")
            bucle = False

else:
    if dni == "22222222Y":
        print("Bienvenido cliente 2")
        cli = cliente("22222222Y", 5500)
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
                        if ((cantidad <= (c.billetes[2][0] * c.billetes[2][1])) and (cantidad % c.billetes[2][0] == 0)) and (
                                c.billetes[2][0] * c.billetes[2][1] != 0):
                            numBillete = cantidad / c.billetes[2][0]
                            c.billetes[2][1] = c.billetes[2][1] - numBillete
                            cli.saldo = cli.saldo - cantidad
                            c.total = c.total - cantidad
                            print("Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))
                            print("Quedan " + str(c.billetes[2][1]) + " billetes de cincuenta euros")
                        else:
                            if ((cantidad <= (c.billetes[1][0] * c.billetes[1][1])) and (cantidad % c.billetes[1][0] == 0)) and (
                                    c.billetes[1][0] * c.billetes[1][1] != 0):
                                numBillete = cantidad / c.billetes[1][0]
                                c.billetes[1][1] = c.billetes[1][1] - numBillete
                                cli.saldo = cli.saldo - cantidad
                                c.total = c.total - cantidad
                                print(
                                    "Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(c.total))
                                print("Quedan " + str(c.billetes[1][1]) + " billetes de veinte euros")
                            else:
                                if ((cantidad <= (c.billetes[0][0] * c.billetes[0][1])) and (cantidad % c.billetes[0][0] == 0)) and (
                                        c.billetes[0][0] * c.billetes[0][1] != 0):
                                    numBillete = cantidad / c.billetes[0][0]
                                    c.billetes[0][1] = c.billetes[0][1] - numBillete
                                    cli.saldo = cli.saldo - cantidad
                                    c.total = c.total - cantidad
                                    print("Su saldo restante es " + str(cli.saldo) + " y en el cajero quedan " + str(
                                        c.total))
                                    print("Quedan " + str(c.billetes[0][1]) + " billetes de diez euros")
            else:
                print("Vuelva pronto")
                bucle = False
    else:
        print("El dni introducido no coincide con ningún usuario")

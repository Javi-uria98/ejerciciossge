class cajero:
    def __init__(self, total, billetes):
        self.total = total
        self.billetes = billetes

    def inicializarcajero(self):
        self.total=1000
        self.billetes = {50: 10, 20: 20, 10: 10}


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
            if (cantidad % 10 == 0):
                c.total = c.total - cantidad
                cli.saldo = cli.saldo - cantidad
                if (cantidad % 10 == 0 and cantidad < 50) and c.billetes[10] > 0:
                    billetes10 = cantidad / 10
                    c.billetes[10] = c.billetes[10] - billetes10
                else:
                    if cantidad % 20 == 0:
                        billetes20 = cantidad / 20
                        c.billetes[20] = c.billetes[20] - billetes20

                print("El dinero restante del cajero es " + str(c.total) + ", el saldo que tiene el cliente es " + str(
                    cli.saldo) + " , quedan "
                                 "" + str(c.billetes[10]) + " billetes de diez euros, " + str(
                    c.billetes[20]) + " de veinte euros, " + str(c.billetes[50]) + " de cincuenta euros")
            else:
                print("Recuerde, solo puede sacar dinero en múltiplos de 10")
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
                c.total = c.total - cantidad;
                cli.saldo = cli.saldo - cantidad;
                print(
                    "El dinero restante del cajero es " + str(c.total) + ", y el saldo que tiene el cliente es " + str(
                        cli.saldo))
            else:
                print("Vuelva pronto")
                bucle = False
    else:
        print("El dni introducido no coincide con ningún usuario")

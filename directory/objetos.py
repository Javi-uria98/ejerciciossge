class persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayoredad(self):
        if self.edad > 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
            self.__saluda()

    #   método privado
    def __saluda(self):
        print("eyy muy buenas a todos aqui willyrex")

p = persona("javier",19)
p.mayoredad()

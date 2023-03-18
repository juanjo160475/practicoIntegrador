from mimetypes import init
'''Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos'''

class Persona():
    def __init__(self , nombre , apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido



class Cuenta():
   
    def __init__(self,titular):
        self.__titular = titular
        self.__cantidad=0.0

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular (self,persona):
        self.__titular= persona
   
    @property
    def cantidad(self):
        return self.__cantidad   
    
    def retirar(self,monto):
        if (monto>0):
            self.__cantidad = self.__cantidad - monto
            print(self.mostrar())
        else:
            print("Ingrese un monto superior a 0")

    def ingresar(self,monto):
        if (monto>0):
            self.__cantidad = self.__cantidad + monto
            print(self.mostrar())
        else:
            print("Ingrese un monto superior a 0")

    def mostrar(self):
        return f"Titular  {self.titular.nombre} {self.titular.apellido} saldo {self.__cantidad} $"


titular1 = Persona("Juan", "Perez")
cuenta1 = Cuenta(titular1)  

cuenta1.retirar(100.30)
cuenta1.ingresar(500)
cuenta1.retirar(-1)




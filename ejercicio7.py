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
    def __init__(self , nombre , apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad=edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    @property
    def edad(self):
        return self.__edad


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
    
    @cantidad.setter
    def cantidad(self,cant):
        self.__cantidad=cant

    
    def retirar(self,monto):
        if (monto>0):
            self.__cantidad = self.__cantidad - monto
            print(f"\n Se retiraron: {monto}\n" ,self.mostrar())
        else:
            print("\n Ingrese un monto superior a 0\n")

    def ingresar(self,monto):
        if (monto>0):
            self.__cantidad = self.__cantidad + monto
            print(f"\n Se ingresaron: {monto}\n" ,self.mostrar())
        else:
            print("\n Ingrese un monto superior a 0\n")

    def mostrar(self):
        return f"Titular:  {self.titular.nombre} {self.titular.apellido} \n Saldo: {self.__cantidad} $"

'''8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta'''
class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion):
        super().__init__(titular)
        self.__bonificacion=bonificacion
    
    @property
    def bonificacion (self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion (self,bono):
        self.__bonificacion=bono

    def es_titular_valido(self):
        if (self.__titular.edad > 18 and self.__titular.edad < 25 ):
            return True
        else:
            return False

    def retirar(self, monto):
        if(self.es_titular_valido==True):
            return super().retirar(monto)
        else:
            return print ("\nTitular no valido no puede extraer dinero")
        
    def ingresar(self, monto):
         super().ingresar(monto) 
         self.cantidad = self.cantidad + (monto * (self.__bonificacion/100))
         return print("",self.cantidad)   

    def mostrar(self):
         return f"Cuenta Joven:  {self.titular.nombre} {self.titular.apellido} \n Saldo: {self.cantidad} $ \n Bonificacion: {self.bonificacion}%"
    
    


titular1 = Persona("Juan", "Perez",25)
cuenta1 = Cuenta(titular1)  

cuenta1.retirar(100.30)
cuenta1.ingresar(500)
cuenta1.retirar(-1)


titular2 = Persona("jose", "Marrone",45)
cuenta2 = CuentaJoven(titular2, 20)  
cuenta2.ingresar(500)
cuenta2.retirar(100.30)
cuenta2.ingresar(500)





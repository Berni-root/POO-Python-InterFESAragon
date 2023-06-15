class Alumno:
    facultad = "FES Aragón" # Atributo de clase, el valor es el mismo para todos
    def __init__(self, nom, ed, carr):
        self.__nombre = nom #doble '_' para ser mas estrictos 
        self.__edad = ed
        self.__carrera = carr
        #print("constructor")
        #print(type(self))

#Métodos de Acceso
    def set_nombre(self, nom): # notacion snake
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, ed): # notacion snake
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("Esa edad no existe")
            self.__edad = 0

        self.__edad = ed

    def get_nombre(self):
        return self.__edad
    
    def set_carrera(self, carr): # notacion snake
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera
# El metodo toString retorna el estado actual del objeto, es decir que valores guarda en este momento el objeto.
    def __str__(self):
        cadena = " -------------- \n Nombre: " + self.__nombre
        cadena = cadena + "\n edad:" + str(self.__edad)
        cadena = cadena + "\n Carrera:" + self.__carrera
        cadena = cadena + "\n --------------"
        return cadena
    
    def estudiar(self, horas=1):
        print(f"EL alumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"
    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    #Método de acceso get 
    @property
    def raza(self):
        return self.__raza
    
    #Método acceso set
    @raza.setter
    def raza(self, la_raza):
        self.__raza = la_raza

    #Método de acceso get 
    @property
    def edad(self):
        return self.__edad
    
    #Método acceso set
    @edad.setter
    def edad(self, la_edad):
        if la_edad > 0 and la_edad < 20:
            self.__raza = la_edad
        else:
            print("Esa no es una edad valida para un perro")
            self.__edad = 0
    
    #Método de acceso get 
    @property
    def estatura(self):
        return self.__estatura
    
    #Método acceso set
    @estatura.setter
    def estatura(self, la_estatura):
        if la_estatura > 0.1 and la_estatura < 1.1:
            self.__estatura = la_estatura
        else:
            print("No way")
            self.__estatura = 0.1
    
    #Método to String
    def __str__(self):
        return f"""
        --------------------------
        Raza: {self.__raza}
        Edad: {self.__edad}
        Estatura: {self.__estatura}
        --------------------------
        """

    @staticmethod
    def es_cachorro(edad):
        return edad < 3
    
    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"Dando vuelta { n + 1}")
        print("Zzzzzzz!")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls("",0,est)
        
#Diagrama UML
'''
- private
+ public
# protected
~ friend paq

example:
-nombre: String
-edad: Int
-carrera: String
+estudiar(horas:int)

NOTACIONES:

@property - Ayuda a implementar encapsulamiento.
@classmethod - Permite la delcaracion de metodos de clase.
@staticmethod - Permite la dlecaracion de metodos miembro de una clase.

'''


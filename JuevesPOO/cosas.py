class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre
    
    #Método acceso set
    @nombre.setter
    def edad(self, nom):
        self.__raza = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo
    
    #Método acceso set
    @pseudonimo.setter
    def edad(self, pseudo):
        self.__raza = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} pseudónimo: {self.__pseudonimo}"
    

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente libro")


class Libro:
    def __init__(self, tit, aut, an, ed ):
        self.__titulo = tit
        self.__autor = aut
        self.__anio = an
        self.__editorial = ed
    
    @property
    def titulo(self):
        return self.__titulo
    
    #Método acceso set
    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit
    
    @property
    def autor(self):
        return self.__autor
    
    #Método acceso set
    @autor.setter
    def autor(self, aut):
        self.__autor = aut

    @property
    def anio(self):
        return self.__anio
    
    #Método acceso set
    @anio.setter
    def titulo(self, an):
        self.__anio = an

    @property
    def editorial(self):
        return self.__editorial
    
    #Método acceso set
    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    
    def __str__(self):
        return f"Título: {self.__titulo} Autor: {self.__autor} Año: {self.__anio} Editorial: {self.__editorial}"
    

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

    @classmethod
    def libro_planeta(cls, titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")
    

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.__edad  = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom


class Alumno(Persona):
    def __init__(self, nombre, edad, num_cuenta, carrera, promedio) -> None:
        super().__init__(nombre, edad)
        self.__numero_cuenta = num_cuenta
        self.__carrera = carrera
        self.__promedio = promedio
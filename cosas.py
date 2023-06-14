class Alumno:
    facultad = "FES Aragón" # Atributo de clase, el valor es el mismo para todos
    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr
        #print("constructor")
        #print(type(self))
    

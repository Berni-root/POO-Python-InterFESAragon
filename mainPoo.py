from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)

    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("------")
    #OJO 
    Alumno.facultad = "FES Aragón EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("UN VISTAZO A LOS OBJETOS")
    print(vars(al1))
    print(vars(al2))

    print(".---------modifcar atributos")
    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """

 
    al1 = Alumno("Bernabé", 22, "ICO")
    al2 = Alumno("Monse", 20, "Derecho")
    #print(al1.nombre)
    #print(al1.facultad)
    al2.edad = 999
    #print(al2.nombre)
    #print(al2.facultad)
    #print(al2.edad)
    print(vars(al1))
    print(vars(al2))
 

main()
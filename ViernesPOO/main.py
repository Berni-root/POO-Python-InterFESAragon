from cosas import *

def main():
    per1 = Persona("jose", 19)
    print(per1)
    print(Persona.descripcion)
    print("------Herencia-----")
    al1 = Alumno("Jose", 19, "454461454", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)

    al2.dormir()

    print("------Herencia Profesor-----")
    profe1 = Profesor("Jesus", 30 +16, 3453213, "Ingeniería de Software")
    print(profe1)
    profe1.dormir()

    print("------Herencia Ayudante Profesor-----")
    ayu = AyudanteProfesor("Adrián", 20, "6548465154", "ICO", 5446465, "Ing. de Software", 4)
    print(ayu)
main()
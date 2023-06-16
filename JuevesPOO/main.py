from cosas import Libro, Autor, Alumno
def main():
    li = Libro.libro_planeta("EL perfume",Autor("Patrick","PS"), 1980)
    print(li)

    print("-----Herencia-----")    
    al2 = Alumno("Jose",19,"23232","ICO",9)
    al2.nombre = "Pepe"
    print(vars(al2))
main()
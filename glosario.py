'''
Glosario de términos de programación
Autor: Sergio Serbluk
Fecha: 2024
versión: 1.0
'''
import os
import colorama
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    limpiar_pantalla()
    print(colorama.Fore.GREEN + "Glosario de términos de programación")
    print(colorama.Fore.CYAN + "\t1 para agregar:" + colorama.Fore.WHITE + " Agregar un término al glosario")
    print(colorama.Fore.CYAN + "\t2 para buscar:" + colorama.Fore.WHITE + " Buscar un término en el glosario")
    print(colorama.Fore.CYAN + "\t3 para mostrar: " + colorama.Fore.WHITE + "Mostrar el glosario")
    print(colorama.Fore.CYAN + "\t4 para modificar:" + colorama.Fore.WHITE + " Modificar un término del glosario")
    print(colorama.Fore.CYAN + "\t5 para eliminar:" + colorama.Fore.WHITE + " Eliminar un término del glosario")
    print(colorama.Fore.CYAN + "\t6 para salir: " + colorama.Fore.WHITE + "Salir del programa")
    print(colorama.Fore.RESET)
    print("Seleccione una opción: ", end="")
    op=int(input(colorama.Fore.BLUE))
    print(colorama.Fore.RESET)
    return op
def agregar():
    termino = input("Ingrese el término: ")
    while termino =="":
        print("El término no puede estar vacío")
        termino = input("Ingrese el término: ")
    if termino in [t[0] for t in terminos]:
        print("El término ya existe")
        input(colorama.Fore.RED+"Presione enter para continuar")
        return
    definicion = input("Ingrese la definición: ")
    while definicion == "":
        print("La definición no puede estar vacía")
        definicion = input("Ingrese la definición: ")
    terminos.append((termino, definicion))#agrega una tupla con el término y la definición a la lista
    print("Término agregado")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
def listar():
    for termino, definicion in terminos:
        print(f"{termino}: {definicion}")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
#programa principal
colorama.init() #inicializa colorama
terminos = [] #lista de términos
op = menu()
while op != 6:
    match op:
        case 1:
            print("Agregar")
            agregar()
            
        case 2:
            print("Buscar")
            input(colorama.Fore.RED+"Presione enter para continuar")
        case 3:
            print("Listar términos")
            listar()
            
        case 4:
            print("Modificar")
            input(colorama.Fore.RED+"Presione enter para continuar")
        case 5:
            print("Eliminar")
            input(colorama.Fore.RED+"Presione enter para continuar")
        case _:
            print("Opción no válida")
            input(colorama.Fore.RED+"Presione enter para continuar")
    op = menu()
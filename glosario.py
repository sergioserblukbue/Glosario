"""
Glosario de términos de programación
Autor: Sergio Serbluk
Fecha: 2024
versión: 1.0
"""
import os
import colorama
#importo librerias para poder guardar los datos de la lista en un archivo de texto
import json # libreria para guardar los datos en formato json
def guardar_terminos():
    """
    Función que guarda los términos en un archivo json
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    parametros: ninguno
    retorna: nada
    """
    with open("terminos.json", "w") as f:
        json.dump(terminos, f, indent=4)

def cargar_terminos():
    """
    Función que carga los términos desde un archivo binario
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    parametros: ninguno
    retorna: nada
    """
    global terminos
    try:
        with open("terminos.json", "r") as f:
            terminos = json.load(f)
    except FileNotFoundError:
        terminos = []
    except EOFError:
        terminos = []


def limpiar_pantalla():
    """
    Función que limpia la pantalla de la consola
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    """
    os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    """
    funcion que muestra el menú de opciones y retorna la opción seleccionada
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    parametros: ninguno
    retorna: la opción seleccionada
    """
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
    """
    Función que agrega un término al glosario
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    parametros: ninguno
    retorna: nada
    """
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
    guardar_terminos() #guarda los términos en el archivo binario
    print("Término agregado")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
def listar():
    """
    función que muestra la lista de términos del glosario
    Autor: Sergio Serbluk
    Fecha: 2024
    versión: 1.0
    parametros: ninguno
    retorna: nada
    """
    print("Lista de términos:")
    for termino, definicion in terminos:
        print(f"{termino}: {definicion}")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
def buscar():
    termino = input("Ingrese el término a buscar: ")
    for t, d in terminos:
        if t.lower() == termino.lower():
            print(f"{t}: {d}")
            input(colorama.Fore.RED+"Presione enter para continuar")
            return
    print("Término no encontrado")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
def modificar():
    termino = input("Ingrese el término a modificar: ")
    for i in range(len(terminos)):
        if terminos[i][0].lower() == termino.lower():
            print(f"{terminos[i][0]}: {terminos[i][1]}")
            definicion = input("Ingrese la nueva definición: ")
            while definicion == "":
                print("La definición no puede estar vacía")
                definicion = input("Ingrese la definición: ")
            terminos[i] = (terminos[i][0], definicion)
            guardar_terminos()
            print("Término modificado")
            input(colorama.Fore.RED+"Presione enter para continuar")
            return
    print("Término no encontrado")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return
def eliminar():
    termino = input("Ingrese el término a eliminar: ")
    for i in range(len(terminos)):
        if terminos[i][0].lower() == termino.lower():
            print(f"{terminos[i][0]}: {terminos[i][1]}")
            confirmacion = input("¿Está seguro que desea eliminar el término? (s/n): ")
            if confirmacion.lower() == "s":
                del terminos[i]
                guardar_terminos()
                print("Término eliminado")
                input(colorama.Fore.RED+"Presione enter para continuar")
                return
            else:
                print("Operación cancelada")
                input(colorama.Fore.RED+"Presione enter para continuar")
                return
    print("Término no encontrado")
    input(colorama.Fore.RED+"Presione enter para continuar")
    return

#programa principal
colorama.init() #inicializa colorama
terminos = [] #lista de términos
cargar_terminos() #carga los términos desde el archivo binario
op = menu()
while op != 6:
    match op:
        case 1:
            print("Agregar")
            agregar()
            
        case 2:
            print("Buscar")
            buscar()
            input(colorama.Fore.RED+"Presione enter para continuar")
        case 3:
            print("Listar términos")
            listar()
            listar()
            
        case 4:
            print("Modificar")
            modificar()
            input(colorama.Fore.RED+"Presione enter para continuar")
        case 5:
            print("Eliminar")
            eliminar()
            input(colorama.Fore.RED+"Presione enter para continuar")
        case _:
            print("Opción no válida")
            input(colorama.Fore.RED+"Presione enter para continuar")
    op = menu()
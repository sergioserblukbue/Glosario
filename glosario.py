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
    print(colorama.Fore.GREEN + "Glosario de términos de programación")
    print(colorama.Fore.CYAN + "\t1 para agregar:" + colorama.Fore.WHITE + " Agregar un término al glosario")
    print(colorama.Fore.CYAN + "\t2 para buscar:" + colorama.Fore.WHITE + " Buscar un término en el glosario")
    print(colorama.Fore.CYAN + "\t3 para mostrar: " + colorama.Fore.WHITE + "Mostrar el glosario")
    print(colorama.Fore.CYAN + "\t4 para modificar:" + colorama.Fore.WHITE + " Modificar un término del glosario")
    print(colorama.Fore.CYAN + "\t5 para eliminar:" + colorama.Fore.WHITE + " Eliminar un término del glosario")
    print(colorama.Fore.CYAN + "\t6 para salir: " + colorama.Fore.WHITE + "Salir del programa")
    print(colorama.Fore.RESET)
    op=int(input("Ingrese una opción: "))
    return op
#programa principal
colorama.init()
limpiar_pantalla()
op = menu()
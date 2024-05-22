'''
Glosario de terminos de programación
Author: Sergio Serbluk
Fecha: 2024
Version: 1.0
'''
import os
import colorama # para instalar colorama ( pip install colorama / pip3 install colorama)
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    return
def menu():
    limpiarPantalla()
    print(colorama.Fore.GREEN + "Glosario de términos de Programación".center(45))
    print(colorama.Fore.RESET + "="*45)
    print(colorama.Fore.BLUE + "1" + colorama.Fore.RESET + " para agregar un nuevo término")
    print(colorama.Fore.BLUE + "2" + colorama.Fore.RESET + " para modificar un término o su descripción")
    print(colorama.Fore.BLUE + "3" + colorama.Fore.RESET + " para eliminar un término")
    print(colorama.Fore.BLUE + "4" + colorama.Fore.RESET + " para Buscar un término")
    print(colorama.Fore.BLUE + "5" + colorama.Fore.RESET + " para listar todos")
    print(colorama.Fore.BLUE + "6" + colorama.Fore.RESET + " para salir")
    op=int(input("seleccione una opción: "))
    return op
#progra  principal
colorama.init()
op=menu()
while op != 6:
    match op:
        case 1:
            print("agregar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 2:
            print("modificar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 3:
            print("eliminar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 4:
            print("buscar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 5:
            print("listar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case _:
            print("opcion no valida!")
            input(colorama.Fore.RED + "presione enter para continuar")
    op=menu()



    
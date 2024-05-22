'''
Glosario de Términos de Programación
Autor: Serbluk Sergio
fecha: 2024
version: 1.0
'''
import os 
import colorama # para instalar colorama (pip install colorama)
def limpiarPantalla():
    '''
    funcion para limpiar la pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    os.system("cls")
    return
def menu():
    '''
    funcion para limpiar la pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    limpiarPantalla()
    print(colorama.Fore.GREEN + "Glosario de Términos de Programación".center(45))
    print("="*45)
    print(colorama.Fore.BLUE + "\t1" + colorama.Fore.RESET + " para agregar un nuevo término")
    print(colorama.Fore.BLUE + "\t2" + colorama.Fore.RESET + " para modificar un término")
    print(colorama.Fore.BLUE + "\t3" + colorama.Fore.RESET + " para eliminar un término")
    print(colorama.Fore.BLUE + "\t4" + colorama.Fore.RESET + " buscar un término")
    print(colorama.Fore.BLUE + "\t5" + colorama.Fore.RESET + " para listar todos las entradas")
    print(colorama.Fore.BLUE + "\t6" + colorama.Fore.RESET + " para Salir")
    op = int(input(colorama.Fore.CYAN + "seleccione una opción: " + colorama.Fore.RESET ))
    return op
#programa principal
colorama.init() #inicializamos colorama para poder usarlo
op = menu()
while op !=6:
    match op:
        case 1:
            print("agregar")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 2:
            print("modificar")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 3:
            print("eliminar")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 4:
            print("buscar")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 5:
            print("listar todos")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case _:
            print("error!")
            input(colorama.Fore.RED + "presione enter para continuar...")
    op = menu()

'''
Glosario de terminos de Programación
Autor: Sergio Serbluk
fecha: 2024
version: 1.0
'''
import os
import colorama # pip install colorama / pip3 install colorama
def menu():
    '''
    funcion menu 
    presenta un menu de opciones al usuario para poder seleccionar
    Parametros:
    no espera
    Retorno
    retonara la opcion seleccionada por el usuarrio
    Autor: Sergio Serbluk
    colaboradores:

    '''
    limpiarPantalla()
    print(colorama.Fore.GREEN + "Glosarionde Términos de Programación".center(50))
    print("="*50)
    print(colorama.Fore.BLUE + "\t1 agregar:" + colorama.Fore.RESET + " para agregar un nuevo término")
    print(colorama.Fore.BLUE + "\t2 modificar:" + colorama.Fore.RESET + "  para modificar un término")
    print(colorama.Fore.BLUE + "\t3 eliminar:" + colorama.Fore.RESET + "  para eliminar un Término")
    print(colorama.Fore.BLUE + "\t4 Buscar:" + colorama.Fore.RESET + "  para buscar un término")
    print(colorama.Fore.BLUE + "\t5 Listar:" + colorama.Fore.RESET + "  lista todos los terminos")
    print(colorama.Fore.BLUE + "\t6 Salir:" + colorama.Fore.RESET + "  para salir de la aplicación")
    op=int(input("Seleccione una opción: " + colorama.Fore.BLUE))
    print(colorama.Fore.RESET)
    return op
def limpiarPantalla():
    '''
    funcion limpiar pantalla  
    limpia la consola
    Parametros:
    no espera
    Retorno
    no tiene
    Autor: Sergio Serbluk
    colaboradores:

    '''
    os.system('cls' if os.name=='nt' else 'clear')
#programa principal
op = menu()
while op != 6:
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
            print("listar")
            input(colorama.Fore.RED + "presione enter para continuar...")
        case _:
            print(colorama.Fore.RED + "opcion incorrecta!")
            input(f"{colorama.Fore.RED} presione enter para continuar...")
    op=menu()
print("gracias por utilizar el programa!") 

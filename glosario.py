'''
Glosario de terminos de programación
Author: Sergio Serbluk
Fecha: 2024
Version: 1.0
'''
import os
import colorama # para instalar colorama ( pip install colorama / pip3 install colorama)
def limpiarPantalla():
    '''
    Funcion limpiarPantalla()
    Author: Sergio Serbluk
    Fecha: 2024
    Version: 1.0
    parametros:
        no requiere
    retorno:
        no tiene
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def menu():
    '''
    menu()
    Author: Sergio Serbluk
    Fecha: 2024
    Version: 1.0
    parametros:
        no requiere
    retorno:
        retorna la opcion seleccionada por el usuario
    '''
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

def agregar(lista, termino=""):
    '''
    agregar()
    Author: Sergio Serbluk
    Fecha: 2024
    Version: 1.0
    parametros:
        no requiere
    retorno:
        no tiene
    '''
    if termino == "":
        termino=input("ingrese un termino para agregar: ")
        while termino == "":
            print("el termino no puede estar vacio!!!")
            termino=input("ingrese un termino para agregar: ")
        if termino in [elemento[0] for elemento in lista ]:
            print("el termino ya existe en la lista!!")
            input(colorama.Fore.RED + "presione enter para continuar")
            return
    
    definicion=input("ingrese la definicion: ")
    while definicion == "":
        print("la definicion no puede esta vacia: ")
        definicion=input("ingrese la definicion: ")
    lista.append((termino,definicion))
    return
def listar(lista):
    limpiarPantalla()
    print("Lista de de términos del Glosario")
    print("="*45)
    for t, d in lista:
        print(f"{t}: {d}")
    print("fin de la lista!")
    input(colorama.Fore.RED + "presione enter para continuar")
    return
def buscar(lista):
    limpiarPantalla()
    termino=input("ingrese el término a buscar: ")
    for t,d in lista:
        if t.lower() == termino.lower():
            print(f"{t}: {d}")
            input(colorama.Fore.RED + "presione enter para continuar")
            return
    print("El término no se encuentra en la lista!")
    resp=input("Quiere agregar el término a la lista? s/n: ")
    if resp.lower() == "n":
        return
    elif resp.lower()== "s":
        agregar(lista,termino)
    return

#progra  principal
colorama.init()
listTerminos=[]
op=menu()
while op != 6:
    match op:
        case 1:
            print("agregar")
            agregar(listTerminos)
            print(listTerminos)
            input(colorama.Fore.RED + "presione enter para continuar")
        case 2:
            print("modificar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 3:
            print("eliminar")
            input(colorama.Fore.RED + "presione enter para continuar")
        case 4:
            print("buscar")
            buscar(listTerminos)
            input(colorama.Fore.RED + "presione enter para continuar")
        case 5:
            print("listar")
            listar(listTerminos)
            input(colorama.Fore.RED + "presione enter para continuar")
        case _:
            print("opcion no valida!")
            input(colorama.Fore.RED + "presione enter para continuar")
    op=menu()



    
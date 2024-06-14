'''
Glosario de terminos de Programación
Autor: Sergio Serbluk
fecha: 2024
version: 1.0
'''
import os
import colorama  # pip install colorama / pip3 install colorama
import pickle #libreria que permite guardar en formato binario
def guardarTerminos():
    with open("terminos.bin", "wb") as f:
        pickle.dump(terminos, f)
def cargarTerminos():
    global terminos
    try:
        with open("terminos.bin", "rb") as f:
            terminos= pickle.load(f)
    except FileNotFoundError:
        terminos=[]
    except EOFError:
        terminos=[]


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
    print(colorama.Fore.GREEN + "Glosario de Términos de Programación".center(50))
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
    return
def agregar(lista):
    termino=input("ingerse el termino: ")
    while termino == "":
        print("el termino no puede estar vacio!")
        termino=input("ingerse el termino: ")
        input(colorama.Fore.RED + "presione enter para continuar...")
    if termino in [t[0] for t in lista]:
        print("el termino ya existe!")
        input(colorama.Fore.RED + "presione enter para continuar...")
        return
    definicion=input("ingrese la definicion: ")
    while definicion=="":
        print("la definicion no puede estar vacia: ")
        definicion=input("ingrese la definicion: ")
        input(colorama.Fore.RED + "presione enter para continuar...")
    lista.append((termino,definicion))
    guardarTerminos()
    print("termino agregado!")
    print(lista)
    input(colorama.Fore.RED + "presione enter para continuar...")
    return
def listar(lista):
    print("Lista de términos")
    for termino, definicion in lista:
        print(f"{termino}: {definicion}")
    print("Fin de la lista de términos!")
    return
def buscar(lista):
    termino=input("ingrese el término a buscar: ")
    for ter, defi in lista:
        if termino.lower() == ter.lower() :
            print(f"{ter}: {defi}")
            return
    print("el término buscado no se encuentra en la lista!")
    return
def modificar(lista):
    termino=input("ingrese el término a modificar: ")
    for i in range(len(lista)):
        if termino.lower() == lista[i][0]:
            print(f"{lista[i][0]}: {lista[i][1]}")
            definicion=input("ingrese la nueva definicion: ")
            while definicion == "":
                print("la definicion no puede estar  vacia!")
                definicion=input("ingrese la nueva definicion: ")
            lista[i]=(termino, definicion)
            guardarTerminos()
            print("se modifico correctamente!")
            return
    print("termino no encontrado!")
    return
def eliminar(lista):
    termino=input("ingrese el termino a eliminar: ")
    for i in range(len(lista)):
        if termino.lower() == lista[i][0]:
            print(f"{lista[i][0]}: {lista[i][1]}")
            confirmacion=input("Realmente quiere eliminar el término? s/n ")
            if confirmacion.lower() == "s":
                del lista[i]
                guardarTerminos()
                print("se elimino correctamente!")
                return
            elif confirmacion.lower() == "n":
                print("operacion cancelada!")
                return
            else:
                print("opcion no valida")
    print("termino no encontrado!")
    return
#programa principal
cargarTerminos()
op = menu()
while op != 6:
    match op:
        case 1:
            print("agregar")
            agregar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 2:
            print("modificar")
            modificar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 3:
            print("eliminar")
            eliminar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 4:
            print("buscar")
            buscar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 5:
            print("listar")
            listar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case _:
            print(colorama.Fore.RED + "opcion incorrecta!")
            input(f"{colorama.Fore.RED} presione enter para continuar...")
    op=menu()
print("gracias por utilizar el programa!") 

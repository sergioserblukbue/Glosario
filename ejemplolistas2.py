mascotas=[]
nombre=input("ingrese el nombre de la mascota: ")
while nombre != "":
    tipo=input("Ingrese el tipo de mascota: ")
    #edad=input("ingrese la edad de la mascota")
    mascotas.append([nombre,tipo])
    print(f"la mascota {nombre} se agrego a la lista!")
    print(mascotas)
    input()
    nombre=input("ingrese el nombre de la siguiente mascota: ")



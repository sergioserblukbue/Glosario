mascotas=[]
nombre=input("ingrese el nombre de la mascota: ")
while nombre != "":
    mascotas.append(nombre)
    print(f"la mascota {nombre} se agrego a la lista!")
    nombre=input("ingrese el nombre de la siguiente mascota: ")
print(mascotas)
print("lista de mascotas con for")
input("presione enter para continuar")
for nombre in mascotas:
    print(f"el nombre de la mascota es {nombre}")
print("fin de la lista")
c=0
print("lista de mascotas con while")
input("presione enter para continuar")
while c < len(mascotas):
    print(f"el nombre de la mascota es {mascotas[c]}")
    c=c+1
print("fin de la lista")

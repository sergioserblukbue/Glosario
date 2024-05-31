empleados=[]
op=input("quiere ingresar un empleado s/n ")
while op.lower() == "s":
    hijos=[]
    nombre=input("ingrese el nombre del empleado: ")
    ape=input("ingrese el apellido del empleado: ")
    dni=input("ingrese el dni del empleado: ")
    resp=input("cargar un hijo? s/n")
    while resp.lower() == "s":
        dniH=input("ingrese el dni del hijo: ")
        hijos.append(dniH)
        resp=input("cargar otro hijo? s/n")
    
    # agregar el empleado
    empleados.append([nombre,ape,dni,hijos])
    print(empleados)
    op=input("quiere ingresar un empleado s/n ")
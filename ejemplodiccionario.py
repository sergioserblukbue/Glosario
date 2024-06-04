datosPersona = {
 "nombre": "Juan",
 "apellido": "García",
 "edad": 30,
 "ciudad": "Buenos Aires",
 "jubilado": False,
 "hijos": ["Ana", "Fernando", "Marcela"]
}
print("lista de claves")
for clave in datosPersona.keys(): 
    print("\t" , clave)
print("lista de valores")
for valor in datosPersona.values():
    print("\t" , valor)
print("claves y valores")
for clave, valor in datosPersona.items():
    print(f"clave:{clave}, valor: {valor}")
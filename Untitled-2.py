nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad: "))
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
if edad >= 18:
    print("La persona es Mayor de edad.")
else:
    print("La persona es Menor de edad.")
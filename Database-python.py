import sys

print("--Base de datos en python--")

estudiantes = [
    {"nombre": "Ana", "apellido": "Pichardo", "nota": 87},
    {"nombre": "Luis", "apellido": "Matos", "nota": 75}
]

while True:
    print("--- Menú de opciones ---")
    print("1. Agregar estudiantes")
    print("2. Ver lista de estudiantes")
    print("3. Eliminar un estudiante")
    print("4. Salir")
    opcion = input("Elige una opcion")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        nota = int(input("Nota: "))
        estudiantes.append({"nombre": nombre, "apellido": apellido, "nota": nota})
    elif opcion == "2":
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Nota: {estudiante['nota']}")
    elif opcion == "3":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        for estudiante in estudiantes:
            if estudiante["nombre"] == nombre and estudiante["apellido"] == apellido:
                estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                break
    elif opcion == "4":
        break
    else:
        print("Opcion invalida, intente de nuevo.")
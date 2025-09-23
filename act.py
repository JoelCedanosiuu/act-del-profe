def le_calificaciones():
    datos = []
    print("Por favor, ingrese 10 nombres con sus calificaciones:")
    for i in range(10):
        nombre = input(f"Nombre del estudiante {i + 1}: ")
        calificacion = float(input(f"Calificación de {nombre}: "))
        datos.append((nombre, calificacion))
    return datos

def s_superiores(datos):
    print("\nCalificaciones superiores a 8.5:")
    for nombre, calificacion in datos:
        if calificacion > 8.5:
            print(f"{nombre}: {calificacion}")


datos = le_calificaciones()
s_superiores(datos)

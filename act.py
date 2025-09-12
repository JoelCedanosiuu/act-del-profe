def le_calificaciones():
    c = []
    print("Por favor, ingrese 10 calificaciones:")
    for i in range(10):
        n = float(input(f"Calificación {i + 1}: "))
        c.append(n)
    return c

def s_superiores(c):
    print("Calificaciones Superiores a 8.5")
    for n in c:
        if n > 8.5:
            print(n)

c = le_calificaciones()
imprimir_promedios_superiores(c)

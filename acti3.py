def leer_edades():
    edades = []
    print("Ingrese las edades de 10 personas:")
    for i in range(10):
        edad = int(input("Edad de la persona " + str(i + 1) + ": "))
        edades.append(edad)
    return edades


def contar_mayores_menores(edades):
    mayores = 0
    menores = 0
    for edad in edades:
        if edad >= 18:
            mayores = mayores + 1
        else:
            menores = menores + 1
    return mayores, menores


def imprimir_resultados(mayores, menores):
    print("Cantidad de personas mayores de edad:", mayores)
    print("Cantidad de personas menores de edad:", menores)

edades = leer_edades()
mayores, menores = contar_mayores_menores(edades)
imprimir_resultados(mayores, menores)

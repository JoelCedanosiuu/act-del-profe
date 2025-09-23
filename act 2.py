empleado = []
pago = []
total_nomina = 0
max_pago = 0
empleado_max = 0

def ingresar_datos(empleado, pago):
    for i in range(5):
        print("¿Cuál es tu nombre?")
        nombre_empleado = input()
        empleado.append(nombre_empleado)
        
        print("¿Cuál es tu salario?")
        salario = float(input())
        pago.append(salario)

def calcular_nomina(empleado, pago):
    total_nomina = 0
    max_pago = 0
    empleado_max = 0
    for i in range(len(pago)):
        total_nomina += pago[i]
        if pago[i] > max_pago:
            max_pago = pago[i]
            empleado_max = empleado[i]
    return total_nomina, max_pago, empleado_max

def mostrar_resultados(total_nomina, max_pago, empleado_max):
    print("La nómina total es:", total_nomina)
    print("El empleado que más gana es:", empleado_max, "con un salario de", max_pago)

ingresar_datos(empleado, pago)
total_nomina, max_pago, empleado_max = calcular_nomina(empleado, pago)
mostrar_resultados(total_nomina, max_pago, empleado_max)

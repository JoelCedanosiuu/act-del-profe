#Cuestionario de listas
# 1️⃣ Crear una lista a_list con los siguientes elementos
a_list = [1, "hello", [1, 2, 3], True]
print(a_list)

# 2️⃣ Encontrar el valor almacenado en el índice 1
print(a_list[1])

# 3️⃣ Recuperar los elementos almacenados en el índice 1, 2 y 3
print(a_list[1:4])


#Lista de compras

# Tarea 1: Crear una lista vacía
shopping_list = []
print("Lista vacía:", shopping_list)

# Tarea 2: Agregar elementos a la lista
shopping_list = ["Reloj", "Portátil", "Calzado", "Pluma", "Ropa"]
print("Lista inicial:", shopping_list)

# Tarea 3: Agregar un nuevo elemento "Fútbol"
shopping_list.append("Fútbol")
print("Después de agregar 'Fútbol':", shopping_list)

# Tarea 4: Imprimir el primer elemento
print("Primer elemento:", shopping_list[0])

# Tarea 5: Imprimir el último elemento
print("Último elemento:", shopping_list[-1])

# Tarea 6: Imprimir toda la lista
print("Lista completa:", shopping_list)

# Tarea 7: Imprimir los artículos importantes
print("Artículos importantes:", shopping_list[1], "y", shopping_list[2])

# Tarea 8: Cambiar "Pluma" por "Cuaderno"
shopping_list[3] = "Cuaderno"
print("Después de cambiar 'Pluma' por 'Cuaderno':", shopping_list)

# Tarea 9: Eliminar "Ropa" (no es necesario comprarla)
shopping_list.remove("Ropa")
print("Después de eliminar 'Ropa':", shopping_list)

# Tarea 10: Imprimir la lista final de compras
print("Lista final de compras:", shopping_list)






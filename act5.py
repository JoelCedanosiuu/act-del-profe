temp_fahrenheit = [80, 72, 95, 82, 79, 72, 85]


temp_centigrados = []


for fahrenheit in temp_fahrenheit:


 centigrados = (fahrenheit - 32) * 5/9

 #use el round para redondear los numeros
 temp_centigrados.append(round(centigrados, 2))


print(temp_centigrados)

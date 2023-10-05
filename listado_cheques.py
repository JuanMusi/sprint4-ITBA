# Lista para almacenar DNI
listaDni = []

# Abrir el archivo 
with open("listado_cheques.csv", "r") as listadoCheques:
    # Lee el contenido 
    lineas = listadoCheques.readlines()

# Itera, divide y elimina espacios
for linea in lineas:
    campos = linea.strip().split(',')
    for campo in campos:
        if campo.isdigit():  # Verifica si es un numero
            listaDni.append(campo)

# input
dni_ingresado = input("Ingresa el número de DNI a buscar: ")

# Cheques encontrados con el dni
cheques_encontrados = []

# agrega a la lista nueva
for dni in listaDni:
    if dni == dni_ingresado:
        cheques_encontrados.append(dni)

# muestra la cantidad de cheques
if cheques_encontrados:
    cantidad_cheques = len(cheques_encontrados)
    print(f"El DNI ingresado tiene {cantidad_cheques} cheques relacionados.")
else:
    print("No se encontraron cheques relacionados al DNI ingresado.")

#Consultar si desea mostrar el resultado en pantalla o en un archivo CSV

#Consultar por cheques Emitidos o Depositados

#Crear un filtro para cheques (Pendiente, Aprobado o Rechazado)(Opcional)

#Crear un rango de fechas para filtar cheques (Opcional)




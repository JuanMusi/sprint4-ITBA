# Lista para almacenar info de los cheques relacionados al DNI
cheques_encontrados = []

# Contador para ver cuantas veces se repite el DNI
repeticiones_dni = 0

# Abrir el archivo CSV en modo lectura
with open("listado_cheques.csv", "r") as listadoCheques:
    # Leer el contenido
    lineas = listadoCheques.readlines()

# Pedir dni al usuario
dni_ingresado = input("Ingresa el número de DNI a buscar: ")

# Verificar si el DNI ingresado existe en el archivo
dni_existente = any(dni_ingresado in linea_csv for linea_csv in lineas)

if dni_existente:
    for linea in lineas:
        # Elimina espacios y separa por ","
        archivo_ordenado = linea.strip().split(',')
        # DNI esta en la posicion 8 en el archivo
        dni = archivo_ordenado[8] 
        if dni == dni_ingresado:
            # Si hay coincidencia los carga en la lista y aumenta el contador
            cheques_encontrados.append(archivo_ordenado)
            repeticiones_dni += 1

if cheques_encontrados:
    # Pedir al usuario que filtre por cheque emitido o depositado
    while True:
        opcion_filtro = input("Elige el tipo de cheque para mostrar emitido (E) o depositado (D)").upper()
        if opcion_filtro in ("E", "D"):
            break
        else:
            print("Error, debe ingresar 'E' para emitido o 'D' para depositado.")

    # Filtrar los cheques según la opción del usuario
    if opcion_filtro == "E":
        cheques_filtrados = [cheque for cheque in cheques_encontrados if cheque[9] == "EMITIDO"]
        filtro_elegido = "emitidos"
    else:
        cheques_filtrados = [cheque for cheque in cheques_encontrados if cheque[9] == "DEPOSITADO"]
        filtro_elegido = "depositados"

    # Verificar si hay cheques después del filtro
    if not cheques_filtrados:
        print(f"No se encontraron cheques {filtro_elegido} relacionados al DNI {dni_ingresado}.")
    else:
        # Pedir al usuario mostrar cheques por pantalla o csv
        while True:
            opcion_salida = input("Elige una opción de salida (PANTALLA o CSV): ").upper()
            if opcion_salida == "PANTALLA" or opcion_salida == "CSV":
                break
            else:
                print("Opción no válida. Debe ingresar 'PANTALLA' o 'CSV'.")
        
        if opcion_salida == "PANTALLA":
            # Muestra cantidad de cheques y dni en pantalla
            print(f"{len(cheques_filtrados)} cheques {filtro_elegido} encontrados relacionados al DNI {dni_ingresado}:")
            for indice, cheque in enumerate(cheques_filtrados, start=1):
                # Muestra en pantalla los datos accediendo x la posición
                print(f"Cheque {indice}:")
                print("N° de cheque:", cheque[0])
                print("Codigo Banco:", cheque[1])
                print("Codigo Sucursal:", cheque[2])
                print("N° Cuenta Origen:", cheque[3])
                print("N° Cuenta Destino:", cheque[4])
                print("Valor: $", cheque[5])
                print("Fecha Origen:", cheque[6])
                print("Fecha Pago:", cheque[7])
                print("DNI:", cheque[8])
                print("Tipo:", cheque[9])
                print("Estado:", cheque[10])
                print("------------------------------")
        elif opcion_salida == "CSV":
            # Pedir el nombre del archivo CSV de salida
            nombre_archivo_salida = input("Ingrese el nombre del archivo CSV de salida (sin la extensión): ")
            # Concatena la extension .csv al archivo
            nombre_archivo_salida += ".csv"

            # Abrir el archivo CSV de salida en modo escritura
            with open(nombre_archivo_salida, "w") as archivo_salida:
                for cheque in cheques_filtrados:
                    linea = ",".join(cheque)
                    archivo_salida.write(linea + "\n")

            print(f"Los datos de los cheques {filtro_elegido} encontrados se han guardado en el archivo {nombre_archivo_salida}.")
else:
    print(f"No se encontraron cheques relacionados al DNI {dni_ingresado}.")
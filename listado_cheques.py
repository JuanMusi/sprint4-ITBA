import datetime

# Funcion para convertir las fechas a un formato legible
def timestamp_a_fecha_legible(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%d-%m-%Y')

# Constantes descriptivas en vez de usar números mágicos (Entendí esto pero no se si está bien)
NUMERO_DE_CHEQUE = 0
CODIGO_BANCO = 1
CODIGO_SUCURSAL = 2
NUMERO_CUENTA_ORIGEN = 3
NUMERO_CUENTA_DESTINO = 4
VALOR = 5
FECHA_ORIGEN = 6
FECHA_PAGO = 7
DNI = 8
TIPO = 9
ESTADO = 10

# Función para cargar los cheques relacionados con el DNI en un diccionario
def cargar_cheques_por_dni(nombre_archivo, dni):
    cheques = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if datos[DNI] == dni:
                cheque = {
                    "N° de cheque": datos[NUMERO_DE_CHEQUE],
                    "Codigo Banco": datos[CODIGO_BANCO],
                    "Codigo Sucursal": datos[CODIGO_SUCURSAL],
                    "N° Cuenta Origen": datos[NUMERO_CUENTA_ORIGEN],
                    "N° Cuenta Destino": datos[NUMERO_CUENTA_DESTINO],
                    "Valor": datos[VALOR],
                    "Fecha Origen": datos[FECHA_ORIGEN],
                    "Fecha Pago": datos[FECHA_PAGO],
                    "DNI": datos[DNI],
                    "Tipo": datos[TIPO],
                    "Estado": datos[ESTADO]
                }
                cheques.append(cheque)
    return cheques

# Función para filtrar cheques por tipo (emitido o depositado)
def filtrar_cheques_por_tipo(cheques, tipo):
    return [cheque for cheque in cheques if cheque["Tipo"] == tipo]

# Función para mostrar los resultados en pantalla o guardar en CSV
def mostrar_resultados(cheques, filtro_elegido, opcion_salida):
    if not cheques:
        print(f"No se encontraron cheques {filtro_elegido} relacionados al DNI {dni_ingresado}.")
        return

    if opcion_salida == "PANTALLA":
        print(f"{len(cheques)} cheques {filtro_elegido} encontrados relacionados al DNI {dni_ingresado}:")
        for indice, cheque in enumerate(cheques, start=1):
            fecha_origen_legible = timestamp_a_fecha_legible(cheque["Fecha Origen"])
            fecha_pago_legible = timestamp_a_fecha_legible(cheque["Fecha Pago"])
            
            print(f"Cheque {indice}:")
            for clave, valor in cheque.items():
                if clave in ("Fecha Origen", "Fecha Pago"):
                    print(f"{clave}: {fecha_origen_legible}" if clave == "Fecha Origen" else f"{clave}: {fecha_pago_legible}")
                else:
                    print(f"{clave}: {valor}")
            print("------------------------------")
    elif opcion_salida == "CSV":
        nombre_archivo_salida = input("Ingrese el nombre del archivo CSV de salida (sin la extensión): ") + ".csv"
        with open(nombre_archivo_salida, "w") as archivo_salida:
            for cheque in cheques:
                linea = ",".join(str(valor) for valor in cheque.values())
                archivo_salida.write(linea + "\n")
        print(f"Los datos de los cheques {filtro_elegido} encontrados se han guardado en el archivo {nombre_archivo_salida}.")

# Pedir DNI al usuario
dni_ingresado = input("Ingresa el número de DNI a buscar: ")

# Cargar cheques relacionados con el DNI por medio de función
cheques_encontrados = cargar_cheques_por_dni("listado_cheques.csv", dni_ingresado)

if not cheques_encontrados:
    print(f"No se encontraron cheques relacionados al DNI {dni_ingresado}.")
else:
    while True:
        opcion_filtro = input("Elige el tipo de cheque para mostrar (E para emitido o D para depositado): ").upper()
        if opcion_filtro in ("E", "D"):
            break
        else:
            print("Error, debe ingresar 'E' para emitido o 'D' para depositado.")

    # Filtra los cheques encontrados usando una función
    cheques_filtrados = filtrar_cheques_por_tipo(cheques_encontrados, "EMITIDO" if opcion_filtro == "E" else "DEPOSITADO")
    filtro_elegido = "emitidos" if opcion_filtro == "E" else "depositados"

    while True:
        opcion_salida = input("Elige una opción de salida (PANTALLA o CSV): ").upper()
        if opcion_salida in ("PANTALLA", "CSV"):
            break
        else:
            print("Opción no válida. Debe ingresar 'PANTALLA' o 'CSV'.")

    mostrar_resultados(cheques_filtrados, filtro_elegido, opcion_salida)

    ### Falta el README 
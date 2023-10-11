# Sprint N°4
---

## Descripción del trabajo

Comenzamos a trabajar con Python, realizando un buscador de cheques según el DNI introducido, ademas el cliente puede filtrar esos cheques e indicar si quiere que salgan por pantalla o se genere un archivo.

## Características

* Filtros por tipo de cheque (EMITIDO o DEPOSITADO)
* Mostrar el resultado por pantalla o en un archivo .CSV
* Timestamp para manejo de fechas


## Codigo para destacar (Función para mostrar los resultados en pantalla o guardar en CSV)

```
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
```        

## Integrantes (Grupo 1)

* [Ana Jazmin Vazquez](https://github.com/AJVazquez27)
* [Natalia Anahí Vizcarra Savino](https://github.com/NeitRoot)
* [Juan Cruz Musi](https://github.com/JuanMusi)
* [Jorge Caballero](https://github.com/jorgecaballer0)


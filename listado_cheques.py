import csv

dni = input("Ingrese su DNI")
csv_file = csv.reader (open("test.csv", "r"))
salida = input("Opcion 1: Visualizar en Pantalla - Opcion 2:Descargar archivo csv. Opcion: ")  
archivo = open (str(dni)+".csv", "w")

def buscarValoresParaPantalla():
        for row in csv_file:
            if dni == row [8]:
                print ("Tipo de cheque: " + row[9] + "\nEstado de cheque: " + row[10] )

def buscarValoresParaArchivo():
    archivo
    for row in csv_file:
        if dni == row [8]:
            archivo.write(row [9] + row [10])

def tipoDeSalida():  
    if salida == "1":
        buscarValoresParaArchivo()
    elif salida == "2":
        buscarValoresParaPantalla()
    else:
        print ("no existe la opcion seleccionada")
tipoDeSalida()

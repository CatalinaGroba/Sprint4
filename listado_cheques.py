import csv

dni = input("Ingrese su DNI: ")
estadoCheque = input("Ingrese Estado de los cheques (1:APROBADO 2:PENDIENTE 3:RECHAZADO ): ")
csv_file = csv.reader (open("test.csv", "r"))
salida = input("Opcion 1: Visualizar en Pantalla - Opcion 2:Descargar archivo csv. Opcion: ")  
archivo = open (str(dni)+".csv", "w")

if(estadoCheque=='1'):estadoCheque='APROBADO'
if(estadoCheque=='2'):estadoCheque='PENDIENTE'
if(estadoCheque=='3'):estadoCheque='RECHAZADO'
if(estadoCheque==''):estadoCheque=''

def funcionFiltradoDni():
    arrayInfo=[]
    for row in csv_file:
        if dni == row [8]:
            arrayInfo.append(row)
    return arrayInfo

def filtradoEstadoCheque(DatafiltradoDni):
    arrayInfo=[]
    for row in DatafiltradoDni:
        if estadoCheque == row [10]:
            arrayInfo.append(row)
    return arrayInfo

def filtradoTipoCheque():
    2

def buscarValoresParaArchivo():
    archivo
    for row in csv_file:
        if dni == row [8]:
            archivo.write(row [9] + row [10])


def PrintPantalla(data):
    for row in data:
        print('------------')
        print ("Tipo de cheque: " + row[9] + "\nEstado de cheque: " + row[10]+ '\nDni:' +row[8] )
        print('------------')
        

def tipoDeSalida():  
    if salida == "2":
        buscarValoresParaArchivo()

    elif salida == "1":
        data = funcionFiltradoDni()
        if(len(data)>0):
            # print(data)
            if(estadoCheque!=''):
                return PrintPantalla(filtradoEstadoCheque(data))
            
        else:print('no hubo coincidencias')

        
    else:
        print ("no existe la opcion seleccionada")
tipoDeSalida()

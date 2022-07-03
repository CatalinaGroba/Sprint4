import csv
from datetime import datetime

dni = input("Ingrese su DNI: ")
TipoCheque = input("Ingrese Tipo de los cheques (1:EMITIDO 2:DEPOSITADO ): ")
estadoCheque = input("Ingrese Estado de los cheques (1:APROBADO 2:PENDIENTE 3:RECHAZADO ): ")

csv_file = csv.reader (open("test.csv", "r"))
salida = input("Opcion 1: Visualizar en Pantalla - Opcion 2:Descargar archivo csv. Opcion: ")

if(estadoCheque=='1'):estadoCheque='APROBADO'
elif(estadoCheque=='2'):estadoCheque='PENDIENTE'
elif(estadoCheque=='3'):estadoCheque='RECHAZADO'
else:estadoCheque=''


if(TipoCheque=='1'):TipoCheque='EMITIDO'
elif(TipoCheque=='2'):TipoCheque='DEPOSITADO'
else:TipoCheque=''

def getTimestamp(): # el pdf pide esto para el nombre del csv
    dt = datetime.now();
    ts = datetime.timestamp(dt);
    return ts

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

def filtradoTipoCheque(DatafiltradoDni):
    arrayInfo=[]
    for row in DatafiltradoDni:
        if TipoCheque == row [9]:
            arrayInfo.append(row)
    return arrayInfo

def PrintPantalla(data):
    for row in data:
        print('------------')
        print ("Tipo de cheque: " + row[9] + "\nEstado de cheque: " + row[10]+ '\nDni:' +row[8] )
        print('------------')

def printInCsv(data):
    timestamp = getTimestamp()
    f = open(str(dni) + "-" + str(timestamp) + ".csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow(("FechaOrigen", "FechaPago", "Valor", "NumeroCuentaDestino"))
    for row in data:
        writer.writerow((row[6], row[7], row[5], row[4])) # formato que pide el pdf de la consigna
    f.close() 
        

def tipoDeSalida():  
    if (TipoCheque == ''):
        return print ('Tipo de cheque no valido')
    if salida == "2":
        data = funcionFiltradoDni()
        data = filtradoTipoCheque(data)
        if(len(data)>0):
            if(estadoCheque!=''):
                printInCsv(data)
                print('CSV generado exitosamente!')
        else:
            print('no hubo coincidencias')
    elif salida == "1":
        data = funcionFiltradoDni()
        data = filtradoTipoCheque(data)
        if(len(data)>0):
            # print(data)
            if(estadoCheque!=''):
                return PrintPantalla(filtradoEstadoCheque(data))
            PrintPantalla(data)
        else:print('no hubo coincidencias')

        
    else:
        print ("no existe la opcion seleccionada")

tipoDeSalida()

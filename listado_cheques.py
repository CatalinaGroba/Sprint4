import csv
from datetime import datetime

print(' ')
dni = input("Ingrese su DNI: ")
TipoCheque = input("Ingrese Tipo de los cheques (1:EMITIDO 2:DEPOSITADO ): ")
print(' ')
estadoCheque = input("Ingrese Estado de los cheques \n1:APROBADO \n2:PENDIENTE \n3:RECHAZADO \nPor defecto Enter(todos) \nOpcion: ")
print(' ')
csv_file = csv.reader (open("test.csv", "r"))
salida = input("\n1:Visualizar en Pantalla \n2:Descargar archivo csv. \nOpcion: ")

if(estadoCheque=='1'):estadoCheque='APROBADO'
elif(estadoCheque=='2'):estadoCheque='PENDIENTE'
elif(estadoCheque=='3'):estadoCheque='RECHAZADO'
else:estadoCheque=''


if(TipoCheque=='1'):TipoCheque='EMITIDO'
elif(TipoCheque=='2'):TipoCheque='DEPOSITADO'
else:TipoCheque=''

def getTimestamp():
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    return ts

def funcionFiltradoDni():
    arrayInfo = []
    for row in csv_file:
        if dni == row[8]:
            arrayInfo.append(row)
    return arrayInfo


def filtradoEstadoCheque(DatafiltradoDni):
    arrayInfo = []
    for row in DatafiltradoDni:
        if estadoCheque == row[10]:
            arrayInfo.append(row)
    return arrayInfo


def filtradoTipoCheque(DatafiltradoDni):
    arrayInfo = []
    for row in DatafiltradoDni:
        if TipoCheque == row[9]:
            arrayInfo.append(row)
    return arrayInfo

def PrintPantalla(data):
    for row in data:
        print('------------------------')
        print(f'Nro:{row[0]}')
        print("Tipo de cheque: " + row[9] + "\nEstado de cheque: " + row[10] + '\nDni:' + row[8])
        print(datetime.fromtimestamp(int(row[6])))
        print('------------------------')


def printInCsv(data):
    timestamp = getTimestamp()
    f = open(str(dni) + "-" + str(timestamp) + ".csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow(("NroCheque","FechaOrigen", "FechaPago", "Valor", "NumeroCuentaDestino"))
    for row in data:
        writer.writerow((row[0],row[6], row[7], row[5], row[4])) 
    f.close() 
        


def verificarErrorCheque(data):
    for row in data:
        coincidencias = 0
        for row2 in data:
            if (row[0] == row2[0] and row[3] == row2[3]):
                coincidencias = coincidencias + 1
                if coincidencias >= 2:
                   print("Error: múltiples cheques existentes con el mismo número en esta cuenta")
                   return True



def tipoDeSalida():
    if (TipoCheque == ''):
        return print('Tipo de cheque no valido')
    data = funcionFiltradoDni()
    errorRepeticion = verificarErrorCheque(data)
    if errorRepeticion:
            return    
    if salida == "2":
        data = filtradoTipoCheque(data)
        if(len(data)>0):
            if(estadoCheque!=''):
                data = filtradoEstadoCheque(data)
                printInCsv(data)
                print('CSV generado exitosamente!')
            else: 
                printInCsv(data)
                print('CSV generado exitosamente!')    
        else:
            print('No hubo coincidencias')
    elif salida == "1":
        data = filtradoTipoCheque(data)
        if(len(data) > 0):
            if(estadoCheque != ''):
                return PrintPantalla(filtradoEstadoCheque(data))
            else: return PrintPantalla(data) 
        else:
            print('No hubo coincidencias')

    else:
        print ("No existe la opcion seleccionada")

tipoDeSalida()

import datetime
import time

date_time = datetime.datetime.now()
today = date_time.strftime("%d/%m/%Y")

vehiclePark = {'M1' : [] , 'M2' : [] , 'M3' : [] , 'M4' : [] , 'M5' : [] , 'M6' : [] , 'M7' : [] , 'M8' : [] , 'M9' : [] , 'M10' : [] , 'T1' : [] , 'T2' : [] , 'T3' : [] , 'T4' : [] , 'T5' : [] , 'T6' : [] , 'T7' : [] , 'T8' : [] , 'T9' : [] , 'T10' : [] , 'C1' : [] , 'C2' : [] , 'C3' : [] , 'C4' : [] , 'C5' : [] , 'C6' : [] , 'C7' : [] , 'C8' : [] , 'C9' : [] , 'C10' : [] }

def addVehicle(vehicleName , vehicleType) :
    v = vehicleType.capitalize().strip()
    vehicleParkLetter = v[0: 1]
    startingTime = time.time()
    date = today
    for i in list(vehiclePark.items()):
        if i[0][0] == vehicleParkLetter:
            if len(i[1]) == 0:
                i[1].extend([vehicleName , vehicleType , date,  startingTime])
                break

def removeVehicle(vehicleName, vehicleType):
    for i in vehiclePark:
        if len(vehiclePark[i]) > 0 :
            if vehiclePark[i][0] == vehicleName:
                vehiclePark[i].remove(vehicleName)
                vehiclePark[i].remove(vehicleType)
                vehiclePark[i].remove(vehiclePark[i][0])
                print("Current time: " , time.time() , "Starting Park time: " , vehiclePark[i][0] , "Fees: " , (time.time() - vehiclePark[i][0]) * 0.001)
                vehiclePark[i].remove(vehiclePark[i][0])
                break

def showVehicles():
    for vehicle in vehiclePark:
        if vehiclePark[vehicle] == [] :
            continue
        else :
            print(vehicle ,"          " ,  vehiclePark[vehicle][0] , "          " , vehiclePark[vehicle][1] , "          " ,  vehiclePark[vehicle][2] , "          " , vehiclePark[vehicle][3])
# test cases

addVehicle('Toyota' , 'car')
showVehicles()
removeVehicle('Toyota' , 'car')
showVehicles()
print(vehiclePark)


    

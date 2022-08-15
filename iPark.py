import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

vehicleTypes = ["Motorcycle", "Car" , "Truck"]
vehicleTypeCodes = ['M', 'C', 'T']
vehicleTypeNumber = [0, 0 , 0]
serialPlateNumbers = []
feesPerSecond = 0.000001
yAxis = np.arange(len(vehicleTypes))

date_time = datetime.datetime.now()
today = date_time.strftime("%d/%m/%Y")

vehiclePark = {'M1' : [] , 'M2' : [] , 'M3' : [] , 'M4' : [] , 'M5' : [] , 'M6' : [] , 'M7' : [] , 'M8' : [] , 'M9' : [] , 'M10' : [] , 'T1' : [] , 'T2' : [] , 'T3' : [] , 'T4' : [] , 'T5' : [] , 'T6' : [] , 'T7' : [] , 'T8' : [] , 'T9' : [] , 'T10' : [] , 'C1' : [] , 'C2' : [] , 'C3' : [] , 'C4' : [] , 'C5' : [] , 'C6' : [] , 'C7' : [] , 'C8' : [] , 'C9' : [] , 'C10' : [] }

def addVehicle(vehicleName , vehicleType , serialPlateNumber) :
    v = vehicleType.capitalize().strip()
    vehicleParkLetter = v[0: 1]
    vehicleSlotFound = False

    if serialPlateNumber in serialPlateNumbers:
        print("Invalid serial plate number.")
    elif vehicleParkLetter not in vehicleTypeCodes:
        print("Invalid vehicle type.")
    else :
        if vehicleParkLetter == "M" :
            vehicleTypeNumber[0] += 1
        elif vehicleParkLetter == "C" :
            vehicleTypeNumber[1] += 1
        else:
            vehicleTypeNumber[2] += 1

        serialPlateNumbers.append(serialPlateNumber)
        startingTime = time.time()
        date = today
        for i in list(vehiclePark.items()):
            if i[0][0] == vehicleParkLetter:
                if len(i[1]) == 0:
                    vehicleSlotFound = True
                    i[1].extend([vehicleName , vehicleType , date, vehicleParkLetter,   startingTime , serialPlateNumber])
                    break
        if not vehicleSlotFound :
            print("Slots for " , vehicleType , "s are filled. Please try again" )

def removeVehicle(serialPlateNumber):
    if serialPlateNumber in serialPlateNumbers:
        for i in vehiclePark:
            if len(vehiclePark[i]) > 0 :
                if vehiclePark[i][5] == serialPlateNumber :
                    vehicleParkLetter = vehiclePark[i][3]
                    if vehicleParkLetter == "M" :
                        vehicleTypeNumber[0] -= 1
                    elif vehicleParkLetter == "C" :
                        vehicleTypeNumber[1] -= 1
                    else:
                        vehicleTypeNumber[2] -= 1
                    serialPlateNumbers.remove(serialPlateNumber)
                    st = vehiclePark[i][4]
                    vehiclePark[i] = []
                    print("Fees: " , (time.time() - st) * feesPerSecond)
                    
                    break
    else :
        print("Invalid Serial Plate number.")
    
def showSummary():
    for v in vehiclePark:
        if vehiclePark[v] != []:
            print("Slot: " , v , " Name: " , vehiclePark[v][0] , " Type: " , vehiclePark[v][1] ," Date : " , vehiclePark[v][0] ," Time: " , vehiclePark[v][0] ," Serial Plate: " , vehiclePark[v][0] , ) 
            print("")

def showGraph():
    plt.xticks(yAxis, vehicleTypes)
    plt.ylabel("Number of vehicles")
    plt.title("Parking Lot Summary")
    plt.bar(yAxis,vehicleTypeNumber)
    plt.show()


#test cases 

addVehicle('Toyota' , 'car' , 6969)
addVehicle('Toyota' , 'car' , 6959)
addVehicle('Royal Enfield' , 'motorcycle', 4204)
addVehicle('Tesla' , 'truck', 8146)
addVehicle('Tesla' , 'truck', 5146)
addVehicle('Tesla' , 'truck', 8446)
showSummary()
showGraph()

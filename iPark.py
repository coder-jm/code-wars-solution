import time
import matplotlib.pyplot as plt
import numpy as np

vehicleTypes = ["Motorcycle", "Car" , "Truck"]
vehicleTypeCodes = ['M', 'C', 'T']
vehicleTypeNumber = [0, 0 , 0]
serialPlateNumbers = []
feesPerSecond = 0.001
yAxis = np.arange(len(vehicleTypes))
password = 'ipark123'

vehiclePark = {'M1' : [] , 'M2' : [] , 'M3' : [] , 'M4' : [] , 'M5' : [] , 'M6' : [] , 'M7' : [] , 'M8' : [] , 'M9' : [] , 'M10' : [] , 'T1' : [] , 'T2' : [] , 'T3' : [] , 'T4' : [] , 'T5' : [] , 'T6' : [] , 'T7' : [] , 'T8' : [] , 'T9' : [] , 'T10' : [] , 'C1' : [] , 'C2' : [] , 'C3' : [] , 'C4' : [] , 'C5' : [] , 'C6' : [] , 'C7' : [] , 'C8' : [] , 'C9' : [] , 'C10' : [] }

def addVehicle(vehicleName , vehicleType , serialPlateNumber) :
    v = vehicleType.capitalize().strip()
    vehicleParkLetter = v[0: 1]
    vehicleSlotFound = False
    if serialPlateNumber in serialPlateNumbers:
        print("Invalid serial plate number.")
    elif vehicleType.lower().strip() not in ["motorcycle" , "car" , "truck"]:
        print("Invalid vehicle type")
    else :
        serialPlateNumbers.append(serialPlateNumber)
        if vehicleParkLetter == "M" :
            vehicleTypeNumber[0] += 1
        elif vehicleParkLetter == "C" :
            vehicleTypeNumber[1] += 1
        else:
            vehicleTypeNumber[2] += 1

        startingTime = time.time().__round__()
        date = time.ctime()
        for i in list(vehiclePark.items()):
            if i[0][0] == vehicleParkLetter:
                if len(i[1]) == 0:
                    vehicleSlotFound = True
                    i[1].extend([vehicleName , vehicleType , date, vehicleParkLetter,   startingTime , serialPlateNumber])
                    break
        if not vehicleSlotFound :
            print("Slots for " + str(vehicleType) + "s are filled. Please try later" )

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
                    print("Duration: " , (time.time().__round__() - st ) , " seconds.  Fees: " , ((time.time().__round__() - st ) * feesPerSecond).__round__(3) , " Rial")
                    
                    break
    else :
        print("Invalid Serial Plate number.")
    
def showSummary():
    firstArray = []
    secondArray = []
    thirdArray = []
    fullArray = []

    for v in vehiclePark:
        if vehiclePark[v] != []:
            fullArray.append([v])
        else:
            fullArray.append(['  '])

    firstArray = fullArray[:10]
    secondArray = fullArray[10:20]
    thirdArray = fullArray[20:]
        

    print("|-------------------------------------------------------------------------------|")
    print(firstArray)
    print(secondArray)
    print(thirdArray)
    print("|-------------------------------------------------------------------------------|")

def showGraph():
    plt.xticks(yAxis, vehicleTypes)
    plt.ylabel("Number of vehicles")
    plt.title("Parking Lot Summary")
    plt.bar(yAxis,vehicleTypeNumber)
    plt.show()


exit = False 

print("Welcome to the iPark system")
print("Here is the menu")

print("""
a = add a vehicle
r = remove a vehicle
g = view parking lot bar graph
p = view parking lot representation
i = get vehicle details
e = exit the program
    """)


while not exit:
    print("")
    inp = input("Input: ")
    print("")
    inp = inp.lower().strip()

    if inp == 'a':
        n = input("Enter vehicle's name: ")
        t = input("Enter vehicle's type: ")
        s = input("Enter vehicle's serial plate number: ")
        addVehicle(n , t ,s)
    elif inp == 'r':
        s = input("Enter vehicle's serial plate number: ")
        removeVehicle(s)
    elif inp == 'g':
        user_pass = input("Passcode: ")
        if user_pass.lower().strip() == password:
            showGraph()
        else:
            print("Incorrect password")
    elif inp == 'p':
        showSummary()
    elif inp == 'i':
        user_pass = input("Passcode: ")
        if user_pass.lower().strip() == password:
            slot = input("Enter vehicle slot: ")
            try :
                print("Name: " , vehiclePark[slot][0])
                print("Type: " , vehiclePark[slot][1])
                print("Date of Entry: " , vehiclePark[slot][2])
                print("Serial Plate Number: " , vehiclePark[slot][5])
            except KeyError:
                print("Invalid Slot")
        else:
            print("Incorrect password")
    elif inp == 'e':
        print("Thank you ")
        exit = True 
    else:
        print("Invalid user input")
    

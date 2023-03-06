import matplotlib.pyplot as plt
import matplotlib.animation as anim


def dataGeneration():
    hostMass = float(input("Enter mass of the host planet (kg) > "))
    planetMass = float(input("Enter mass of the orbiting planet (kg) > "))
    initialyVelocity = float(input("Enter initial velocity in the y direction of the orbiting planet (m/s) > "))
    intialxPosition = float(input("Enter initial x position of the orbiting planet (m) > "))
    timeIncrement = float(input("Enter the time increment for the calculations (s) > "))
    numberLines = int(input("Enter the number of lines you want calculated > "))
    initialxVelocty = 0
    initialyPosition = 0
    gValue = float(6.67e-11)
    
    lineArray = []
    currentTime = 0

    #format of Line: Time, X pos, X vel, Y pos, Y vel, Acc X, Acc Y,
    for rowNumber in range(numberLines):
        newLine = []
        if rowNumber == 0:
            newLine.append(currentTime)
            newLine.append(intialxPosition)
            newLine.append(initialxVelocty)
            newLine.append(initialyPosition)
            newLine.append(initialyVelocity)
            newLine.append((-1 * hostMass * newLine[1] * gValue)/(((newLine[1] ** 2) + (newLine[3] ** 2))**1.5))
            newLine.append((-1 * hostMass * newLine[3] * gValue)/(((newLine[1] ** 2) + (newLine[3] ** 2))**1.5))
        
        else:
            newLine.append(currentTime)
            newLine.append(lineArray[-1][1] + lineArray[-1][2] * timeIncrement)
            newLine.append(lineArray[-1][2] + lineArray[-1][5] * timeIncrement)
            newLine.append(lineArray[-1][3] + lineArray[-1][4] * timeIncrement)
            newLine.append(lineArray[-1][4] + lineArray[-1][6] * timeIncrement)
            newLine.append((-1 * hostMass * newLine[1] * gValue)/(((newLine[1] ** 2) + (newLine[3] ** 2))**1.5))
            newLine.append((-1 * hostMass * newLine[3] * gValue)/(((newLine[1] ** 2) + (newLine[3] ** 2))**1.5))


        lineArray.append(newLine)
        currentTime += timeIncrement

    dataSet = lineArray

if __name__ == "__main__":
    dataGeneration()

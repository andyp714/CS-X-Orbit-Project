import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

#19380 is perfect circle!
def dataGeneration():
    hostMass = float(input("Enter mass of the host planet (kg) > "))
    planetMass = float(1)
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
    graphGeneration(dataSet,  numberLines)

def graphGeneration(dataSet, numberLines):
    xValues = []
    yValues = []

    for line in dataSet:
        xValues.append(line[1])
        yValues.append(line[3])
    
    fig = plt.figure()
    plt.axes(xlim=((-1.1 * max(xValues)), (1.1 * max(xValues))), ylim=((-1.1*max(yValues)), (1.1*max(yValues))))
    plt.plot(0,0, 'ro')
    plt.plot(xValues,yValues, linestyle='--',  color='#444444')
    plt.grid(visible=True, which='major', axis='both')
    plt.title("X-Position vs Y-Position")
    line, = plt.plot([],[], 'bo')
    framesNumber = math.floor((numberLines-1)/8)

    def init():
        line.set_data([],[])
        return line,

    xdata, ydata = [], []

    def animate(i):
        x = xValues[8* i]
        y = yValues[8* i]
        
        line.set_data([x], [y])
        return line, 

    anim = animation.FuncAnimation(fig, animate, init_func= init, interval = 1, blit=True, frames=framesNumber, repeat=True)
    plt.show()


    

    '''
    plt.plot(xValues,yValues, 'b-')
    plt.grid(visible=True, which='major', axis='both')
    plt.title("X Position VS Y Position")
    plt.xlabel("X Position [m]")
    plt.ylabel("Y Position [m]")
    plt.plot(0,0, 'ro')
    plt.show()
    '''



if __name__ == "__main__":
    dataGeneration()
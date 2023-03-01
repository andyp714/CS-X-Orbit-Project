def main():
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

    #format of Line: Time, X pos, X vel, Y pos, Y vel, Acc X, Acc Y,
    for rowNumber in range(numberLines):
        newLine = []
        if rowNumber == 0:
            newLine.append(timeIncrement)
            newLine.append(intialxPosition)
            newLine.append(initialxVelocty)
            newLine.append(initialyPosition)
            newLine.append(initialyVelocity)
            #Add acc x and acc y


if __name__ == "__main__":
    main()

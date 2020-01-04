'''
Distributed by the MIT License
Made by dimpetrop.me (CorruptedGov)
'''
from time import sleep
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

def writeRb():  #Writing RB prices (from RB1 to RB500)
    base = 4E8
    sum = rb = 0
    with open("rbs.txt", "w") as f:
        for i in range(1,501):
            rb+=1
            sum+=base
            f.write(str(rb) + "    " + str(sum) + "\n")  #leaving some space between for reading purposes

def calcPrice(rbfrom, rbto):  #Calculating RB Price for current rb to goal rb
    base = 4E8
    sum = 0
    counter = 1
    rbprices = []
    with open("rbs.txt", "r") as f:
        for line in f:
            if counter == rbto:
                rbprices.append(float(line[3:len(line)-1]))   #Will append the price to an array will only read from index 3 up to the last digit (excl \n)
                break
            if counter >= rbfrom:
                rbprices.append(float(line[3:len(line)-1]))
            counter += 1
        for rb in rbprices:
            sum += rb
        print("Price for RB: " + str(rbfrom) + " to " + str(rbto) + " is " + str(locale.format("%d", sum, grouping=True)))

while True:    
    rbfrom=int(input("Insert your current rebirth level "))
    rbto=int(input("Insert the rb level you want to reach "))
    writeRb()

    calcPrice(rbfrom, rbto)
    print("\nApplication will exit in 10 seconds")
    sleep(10)
    break



            
            



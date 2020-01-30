from point import *
from nearestNeighbor import *
from exhaustive import *
import time
import random




def readInputFile(pointList):
    #read in the file
    inputFile = open('../test_inputs/input.txt', 'r')

    numberOfLinesToRead = inputFile.readline().strip()

    for i in range(int(numberOfLinesToRead)):
        values = inputFile.readline().split()
        pointList.append(Point(values[0],values[1]))
    inputFile.close()

def generateInputFile(n):
    outFile = open('../test_inputs/input.txt','w')
    outFile.write(str(n))
    for i in range(n):
        firstPoint = random.randrange(0,200)
        secondPoint = random.randrange(0,200)
        toWrite = "\n" + str(firstPoint) + " " + str(secondPoint)
        outFile.write(toWrite)



def runSimulations(n):
    print("\nRUNNING SIMULATION WITH SIZE",n)

    generateInputFile(n)

    totalNnTime = 0.0
    totalExTime = 0.0
    #perform 3 trials
    for i in range(3):
        pointList = []
        readInputFile(pointList)

        master = list.copy(pointList)

        startAndEnd = pointList[0]
        totalLength = 0.0;
        nnPath = []
        nnStartTime = time.time()
        nearestNeighbor(pointList,startAndEnd,nnPath,totalLength)
        nnPath.append(startAndEnd)
        nnTotalTime = time.time() - nnStartTime
        totalNnTime += nnTotalTime
        totalLength=getTotalDistance(nnPath)


        pointList = master

        exStartTime = time.time()
        exAns=exhaustive(pointList)
        exTotalTime = time.time() - exStartTime
        totalExTime += exTotalTime
        shortestPermutation=exAns[1]
        shortestPermutationDistance=exAns[0]



    #print out paths and averages
    print("{:.3f}".format(totalLength))
    for p in nnPath:
        print(p,end='')
    print(totalNnTime/3)

    print("\n")

    print("{:.3f}".format(shortestPermutationDistance))
    for p in shortestPermutation:
        print(p,end='')
    print(totalExTime/3)


runWith = [6,7,8,9,10]

for x in runWith:
    runSimulations(x)

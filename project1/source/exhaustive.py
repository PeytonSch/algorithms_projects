import itertools
import math
def exhaustive(pointList):
    #get all permutations of list
    #remove first point to meet requirment of all permutations starting with first point in file
    firstPoint = pointList[0]
    pointList.remove(firstPoint)
    allPermutations = (list(itertools.permutations(pointList)))
    #init shortest vars
    shortestPermutation = []
    shortestPermutationDistance = -1
    for permutation in allPermutations:
        #convert permutation to list
        permutation = list(permutation)
        #put first point back in to permutation
        permutation.insert(0,firstPoint)
        permutation.append(firstPoint)

        if shortestPermutationDistance == -1:
            shortestPermutation = permutation
            shortestPermutationDistance = getTotalDistance(permutation)
        else:
            checkDistance = getTotalDistance(permutation)
            if checkDistance < shortestPermutationDistance:
                shortestPermutationDistance = checkDistance
                shortestPermutation = permutation
    return [shortestPermutationDistance,shortestPermutation]








def getTotalDistance(listOfPoints):
    total = 0
    for i in range(len(listOfPoints)-1):
        total+= listOfPoints[i].distanceTo(listOfPoints[i+1])
    return total

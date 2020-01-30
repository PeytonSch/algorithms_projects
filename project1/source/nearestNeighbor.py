def nearestNeighbor(pointList,startingPoint,path,totalLength):
    if len(pointList) == 0: return
    #pick initial point
    path.append(startingPoint)
    pointList.remove(startingPoint)
    if len(pointList) == 0: return
    #determine next closest point
    closestDistance = float(startingPoint.distanceTo(pointList[0]))
    closestPoint = pointList[0]
    for p in pointList:
        distanceToP = float(startingPoint.distanceTo(p))
        if closestDistance > distanceToP:
            closestDistance = distanceToP
            closestPoint = p
    totalLength+= closestDistance
    nearestNeighbor(pointList,closestPoint,path,totalLength)

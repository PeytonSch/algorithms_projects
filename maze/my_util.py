
def getNode(x,y,location):
    #print("Looking for ",x,y)
    for element in location:
        #print("--->  ", element.x,element.y)
        if element.x == x and element.y == y:
            return element
    print("Error, element not found")
    return None

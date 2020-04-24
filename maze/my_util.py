
def getNode(x,y,squares):
    #print("Looking for ",x,y)
    for element in squares:
        #print("--->  ", element.x,element.y)
        if element.x == x and element.y == y:
            return element
    print("Error, element not found")
    return None

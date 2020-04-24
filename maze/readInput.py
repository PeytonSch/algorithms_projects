def readFile(fileName='input.txt'):
    f = open(fileName,'r')
    firstLine = f.readline().split()
    rows = int(firstLine[0])
    cols = int(firstLine[1])
    maze = []
    for row in range(rows):
        rowLine = f.readline().split()
        maze.append(rowLine)

    return maze

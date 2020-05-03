def readFile(fileName='input.txt'):
    #open our file in read mode
    f = open(fileName,'r')
    #row and col info / size is on first line
    row_col_info = f.readline().split()
    rows = int(row_col_info[0])
    cols = int(row_col_info[1])
    #list to store nodes in
    nodes = []
    #read in rodes
    for row in range(rows):
        rowLine = f.readline().split()
        nodes.append(rowLine)

    #return list of nodes 
    return nodes

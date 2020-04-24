from square import *
from readInput import *
from my_util import *


maze = readFile()
squares = []

#generate all nodes
for y in range(1,len(maze)+1):
    for x in range(1,len(maze[0])+1):
        line = maze[0]
        node = Square(x,y,maze[x-1][y-1])
        squares.append(node)
#add pointers
for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x,y,squares)
        value = abs(int(current_node.value))
        #append straight and diagonal nodes to list

        #check left
        if int(x) - abs(value) > 0:
            current_node.append_straight(getNode(x-value,y,squares))
        #check right
        if int(x) + value < len(line)+1:
            current_node.append_straight(getNode(x+value,y,squares))
        #check up
        if int(y) - value > 0:
            current_node.append_straight(getNode(x,y-value,squares))
        #check down
        if int(y) + value < len(maze)+1:
            current_node.append_straight(getNode(x,y+value,squares))

        #check up left
        if int(x) - value > 0 and y - value > 0:
            current_node.append_diag(getNode(x-value,y-value,squares))
        #check up right
        if int(x) + value < len(line)+1 and y - value > 0:
            current_node.append_diag(getNode(x+value,y-value,squares))
        #check down left
        if int(x) - value > 0 and y + value < len(maze)+1:
            current_node.append_diag(getNode(x-value,y+value,squares))
        #check down right
        if int(x) + value < len(line)+1 and y + value < len(maze)+1:
            current_node.append_diag(getNode(x+value,y+value,squares))

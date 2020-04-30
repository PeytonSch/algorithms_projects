from square import *
from readInput import *
from my_util import *
from dfs import *


maze = readFile()
squares = []
diagonals = []

#generate all nodes
for y in range(1,len(maze)+1):
    for x in range(1,len(maze[0])+1):
        line = maze[0]
        node = Square(x,y,maze[x-1][y-1])
        squares.append(node)

diagonals = squares

#add pointers
for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):

        current_node = getNode(x,y,squares)
        value = abs(int(current_node.value))
        #append straight and diagonal nodes to list

        if current_node.color == "red":
            continue

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


for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, diagonals)
        value = abs(int(current_node.value))
        # append straight and diagonal nodes to list
        if current_node.color == "red":
            continue
        #check up left
        if int(x) - value > 0 and y - value > 0:
            current_node.append_diag(getNode(x-value,y-value,diagonals))
        #check up right
        if int(x) + value < len(line)+1 and y - value > 0:
            current_node.append_diag(getNode(x+value,y-value,diagonals))
        #check down left
        if int(x) - value > 0 and y + value < len(maze)+1:
            current_node.append_diag(getNode(x-value,y+value,diagonals))
        #check down right
        if int(x) + value < len(line)+1 and y + value < len(maze)+1:
            current_node.append_diag(getNode(x+value,y+value,diagonals))

for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, diagonals)

    if current_node.color == "black":
        continue

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

for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, squares)

    if current_node.color == "black":
        continue

    #check left
    if int(x) - abs(value) > 0:
        current_node.append_straight(getNode(x-value,y,diagonals))
    #check right
    if int(x) + value < len(line)+1:
        current_node.append_straight(getNode(x+value,y,diagonals))
    #check up
    if int(y) - value > 0:
        current_node.append_straight(getNode(x,y-value,diagonals))
    #check down
    if int(y) + value < len(maze)+1:
        current_node.append_straight(getNode(x,y+value,diagonals))


first_node = getNode(1, 1, squares)
empty = []
discovered = []
ans = ourDFS(first_node, discovered,empty)

print(type(ans))

#ans = ourDFS(first_node, empty)

for e in ans:
    print("(",e.x,",",e.y,")")

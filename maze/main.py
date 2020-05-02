from square import *
from readInput import *
from my_util import *
from dfs import *
import globals
from tests import *
from bfs import *

globals.init()
maze = readFile()
squares = []
diagonals = []

#generate all nodes
for y in range(1,len(maze)+1):
    for x in range(1,len(maze[0])+1):
        line = maze[0]
        node = Square(x,y,maze[x-1][y-1])
        squares.append(node)

for y in range(1,len(maze)+1):
    for x in range(1,len(maze[0])+1):
        line = maze[0]
        node = Square(x,y,maze[x-1][y-1])
        diagonals.append(node)
'''
Needed to make these copies rather
than referencing the same memory
'''
#diagonals = squares.copy()
#test_different_addresses(squares,diagonals)
#print(hex(id(diagonals)))
#print(hex(id(squares)))

#add pointers
for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):

        current_node = getNode(x,y,squares)
        value = abs(int(current_node.value))
        #append straight and diagonal nodes to list

        if not current_node.color == "black":
            continue
        #check left
        if int(x) - abs(value) > 0:
            current_node.append_straight(getNode(x-value,y,squares))
        #check up
        if int(y) - value > 0:
            current_node.append_straight(getNode(x,y-value,squares))
        #check down
        if int(y) + value < len(maze)+1:
            current_node.append_straight(getNode(x,y+value,squares))
        #check right
        if int(x) + value < len(line)+1:
            current_node.append_straight(getNode(x+value,y,squares))


for y in range(1,len(maze)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, diagonals)
        value = abs(int(current_node.value))
        # append straight and diagonal nodes to list
        if not current_node.color == "black":
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
        value = abs(int(current_node.value))
        if not current_node.color == "red":
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
        value = abs(int(current_node.value))
        if not current_node.color == "red":
            continue

        #check up left
        if int(x) - abs(value) > 0 and int(y) - value > 0:
            current_node.append_straight(getNode(x-value,y-value,diagonals))
        #check up right
        if int(x) - value > 0 and y + value < len(line)+1:
            current_node.append_straight(getNode(x-value,y+value,diagonals))
        #check down left
        if int(x) + value < len(line) + 1 and y - value > 0:
            current_node.append_straight(getNode(x+value,y-value,diagonals))
        #check down right
        if int(x) + value < len(line) + 1 and y + value < len(line)+1:
            current_node.append_straight(getNode(x+value,y+value,diagonals))


first_node = getNode(1, 1, squares)
finished = False

ans = []
#ourDFS(first_node, discovered,ans)

path = [first_node]
ans_string = find_path_bfs(first_node)
print(ans_string)

#test_adj_lists(first_node)
#print("Errors:",globals.error_count,"Nodes",globals.node_count)

'''
for i in ans:
    print ("(", i.x,",",i.y,")")
#ans = ourDFS(first_node, empty)
'''

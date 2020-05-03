from node import *
from readInput import *
from my_util import *
from dfs import *
import globals
from tests import *
from bfs import *



#read in board
board = readFile()

#these lists will show possible straight and
#diagonal paths for nodes, I'll use these
#to construct my edges
straight_lists = []
diagonals_list = []

#generate all nodes - straights
for y in range(1,len(board)+1):
    for x in range(1,len(board[0])+1):
        line = board[0]
        node = Node(x,y,board[x-1][y-1])
        straight_lists.append(node)

#generate all nodes - diagonals
for y in range(1,len(board)+1):
    for x in range(1,len(board[0])+1):
        line = board[0]
        node = Node(x,y,board[x-1][y-1])
        diagonals_list.append(node)


#add pointers
for y in range(1,len(board)+1):
    for x in range(1,len(line)+1):

        current_node = getNode(x,y,straight_lists)
        value = abs(int(current_node.value))

        #append straight and diagonal nodes to list
        #if the node is red then skip for now and we will fill
        #in later
        if not current_node.color == "black":
            continue
        #check left
        if int(x) - abs(value) > 0:
            current_node.add_adjacent_node(getNode(x-value,y,straight_lists))
        #check up
        if int(y) - value > 0:
            current_node.add_adjacent_node(getNode(x,y-value,straight_lists))
        #check down
        if int(y) + value < len(board)+1:
            current_node.add_adjacent_node(getNode(x,y+value,straight_lists))
        #check right
        if int(x) + value < len(line)+1:
            current_node.add_adjacent_node(getNode(x+value,y,straight_lists))



for y in range(1,len(board)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, diagonals_list)
        value = abs(int(current_node.value))
        # append straight and diagonal nodes to list
        if not current_node.color == "black":
            continue
        #check up left
        if int(x) - value > 0 and y - value > 0:
            current_node.add_adjacent_node(getNode(x-value,y-value,diagonals_list))
        #check up right
        if int(x) + value < len(line)+1 and y - value > 0:
            current_node.add_adjacent_node(getNode(x+value,y-value,diagonals_list))
        #check down left
        if int(x) - value > 0 and y + value < len(board)+1:
            current_node.add_adjacent_node(getNode(x-value,y+value,diagonals_list))
        #check down right
        if int(x) + value < len(line)+1 and y + value < len(board)+1:
            current_node.add_adjacent_node(getNode(x+value,y+value,diagonals_list))

for y in range(1,len(board)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, diagonals_list)
        value = abs(int(current_node.value))
        if not current_node.color == "red":
            continue

        #check left
        if int(x) - abs(value) > 0:
            current_node.add_adjacent_node(getNode(x-value,y,straight_lists))
        #check right
        if int(x) + value < len(line)+1:
            current_node.add_adjacent_node(getNode(x+value,y,straight_lists))
        #check up
        if int(y) - value > 0:
            current_node.add_adjacent_node(getNode(x,y-value,straight_lists))
        #check down
        if int(y) + value < len(board)+1:
            current_node.add_adjacent_node(getNode(x,y+value,straight_lists))

for y in range(1,len(board)+1):
    for x in range(1,len(line)+1):
        current_node = getNode(x, y, straight_lists)
        value = abs(int(current_node.value))
        if not current_node.color == "red":
            continue

        #check up left
        if int(x) - abs(value) > 0 and int(y) - value > 0:
            current_node.add_adjacent_node(getNode(x-value,y-value,diagonals_list))
        #check up right
        if int(x) - value > 0 and y + value < len(line)+1:
            current_node.add_adjacent_node(getNode(x-value,y+value,diagonals_list))
        #check down left
        if int(x) + value < len(line) + 1 and y - value > 0:
            current_node.add_adjacent_node(getNode(x+value,y-value,diagonals_list))
        #check down right
        if int(x) + value < len(line) + 1 and y + value < len(line)+1:
            current_node.add_adjacent_node(getNode(x+value,y+value,diagonals_list))


first_node = getNode(1, 1, straight_lists)
finished = False

ans = []
#ourDFS(first_node, discovered,ans)

path = [first_node]


ans_string = run_bfs(first_node)
print(ans_string)

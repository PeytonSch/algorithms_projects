

class Node:

    #This list will store edges / pointers to
    #the nodes each instance of a node can go to
    adjacent_nodes = []

    #instantiate each node
    def __init__(self,x_in,y_in,value_in):
        self.x = x_in
        self.y = y_in
        self.value = int(value_in)
        self.visited = "Undiscovered"
        self.adjacent_nodes = []

        #set colors so we know when to construct
        #straight or diagonal edges
        if self.value < 0:
            self.color = "red"
        elif self.value > 0:
            self.color = "black"
        else:
            self.color = "finish"


    #used for creating the adjacent_nodes
    def add_adjacent_node(self,node):
        self.adjacent_nodes.append(node)

    #used for bfs
    def set_visited(self, state):
        self.visited = state

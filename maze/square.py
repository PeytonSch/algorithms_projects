

class Square:

    straight = []
    diag = []

    adj_list = []

    def __init__(self,x_in,y_in,value_in):
        self.x = x_in
        self.y = y_in
        self.value = int(value_in)
        self.visited = "Undiscovered"

        if self.value < 0:
            self.color = "red"
        elif self.value > 0:
            self.color = "black"
        else:
            self.color = "finish"

    def append_straight(self,node):
        self.adj_list.append(node)
    def append_diag(self,node):
        self.adj_list.append(node)

    def set_visited(self, state):
        self.visited = state

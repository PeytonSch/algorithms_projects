

class Square:

    straight = []
    diag = []

    def __init__(self,x_in,y_in,value_in):
        self.x = x_in
        self.y = y_in
        self.value = int(value_in)


        if self.value < 0:
            self.color = "red"
        elif self.value > 0:
            self.color = "black"
        else:
            self.color = "finish"

    def append_straight(self,node):
        self.straight.append(node)
    def append_diag(self,node):
        self.diag.append(node)

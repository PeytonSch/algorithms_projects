import globals
def test_different_addresses(one,two):
    assert id(one) != id(two)


'''
When testing adjac list, there should be at most 4
nodes in an adj list. If there are more than 4 then something
went wrong when constructing the lists
'''
error_count = 0
node_count = 0
def test_adj_lists(node):
    node.set_visited("Discovered")

    for i in node.adj_list:
        if i.visited == "Undiscovered":
            globals.node_count = globals.node_count + 1
            print(id(node_count))
            if len(node.adj_list) > 4 or len(node.adj_list) < 1:
                print("Error: Node has",len(node.adj_list))
                globals.error_count = globals.error_count + 1

            test_adj_lists(i)

            if node.color == "finish":
                return

'''
Right now we only return if a node is finished?
But what if we hit finish and we should return on
the next one? We should be returning when nodes
are either finished or if they are processed completely
so somewhere we need to be setting them to the processed state

'''

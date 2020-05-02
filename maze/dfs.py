import globals


ans = []
finished = False

def ourDFS(node, discovered_list,ans):



    node.set_visited("Discovered")
    discovered_list.append(node)

    if node.color == "finish" and globals.finished == False:
        globals.finished = True
        for i in discovered_list:
            ans.append(i)
        print("solution found")
        return

    #print("Node Adj List Length:",len(node.adj_list),"of type",node.color)

    for i in node.adj_list:
        if i.visited == "Undiscovered":
            ourDFS(i,discovered_list,ans)



    node.set_visited="Processed"
    discovered_list.remove(node)


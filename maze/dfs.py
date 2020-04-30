def ourDFS(node, discovered_list,ans):
    if node.color == "finish":
        #print(len(discovered_list))
        #print(node.value)
        if len(ans) == 0:
            print("Setting ans")
            #print(type(discovered_list))
            ans = discovered_list
            #print(type(ans))
        return

    node.set_visited("Discovered")
    discovered_list.append(node)

    for i in node.adj_list:
        if i.visited == "Undiscovered":
            ourDFS(i,discovered_list,ans)
    node.set_visited="Processed"


    discovered_list.remove(node)

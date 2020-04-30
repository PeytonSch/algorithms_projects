def ourDFS(node, discovered_list,ans):
    if node.color == "finish":
        ans = discovered_list
        return 0

    node.set_visited("Discovered")
    discovered_list.append(node)

    for i in node.adj_list:
        if i.visited == "Undiscovered":
            ourDFS(i,discovered_list,ans)

    node.set_visited="Processed"

    discovered_list.remove(node)

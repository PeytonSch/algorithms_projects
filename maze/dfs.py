def ourDFS(self, node, discovered_list):
    if node.color == "finish":
        return discovered_list

    node.set_visited("Discovered")
    discovered_list.append(node)

    for i in node.adj_list:
        if i.visited == "Undiscovered":
            self.ourDFS(i)
    node.set_visited="Processed"

    discovered_list.remove(node)

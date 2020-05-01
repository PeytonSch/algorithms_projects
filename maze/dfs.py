def ourDFS(node, discovered_list,ans):



    node.set_visited("Discovered")
    discovered_list.append(node)

    for i in node.adj_list:
        if i.visited == "Undiscovered":


            ourDFS(i,discovered_list,ans)


            if node.color == "finish":
                ans = discovered_list.copy()
                print("Base Case")
                print(len(discovered_list))

                for e in ans:
                    print("(",e.x,",",e.y,")",e.visited)

                return





    node.set_visited="Processed"

    discovered_list.remove(node)

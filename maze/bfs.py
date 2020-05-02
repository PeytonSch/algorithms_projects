from collections import deque

def bfs(path,visited):

    while len(path) != 0:
        for i in path[0].adj_list:
            if i.color == "finish":
                visited.append(path[0])
                visited.append(i)
                return visited
            elif i.visited == "Undiscovered":
                path.append(i)

        visited.append(path[0])
        path[0].visited = "Discovered"
        path.pop(0)



def find_path_bfs(start):

    queue = deque([("(1,1) ", start)])
    visited = set()

    while queue:
        path, current = queue.popleft()
        if current.color == "finish":
            return path
        if current in visited:
            continue
        visited.add(current)
        for i in current.adj_list:
            queue.append((path + "("+ str(i.x) +","+ str(i.y) +") ", i))
    return ""

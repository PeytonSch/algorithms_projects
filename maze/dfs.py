def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end = ' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

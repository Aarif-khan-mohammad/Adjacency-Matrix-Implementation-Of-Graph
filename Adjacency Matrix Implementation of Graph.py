class Graph():
    def __init__(self , vertix_count):
        self.vertix_count = vertix_count
        self.adj_matrix = [[0]*vertix_count for x in range(vertix_count)] #here it indicates , the zeros are present repectively with nodes,( ex : if list contains 5 nodes than this contains 5 zeros ) ,, the loop helps to create number of list based on vertex nodes (ex : 5 nodes --> 5 lists --> 25 zeros)

    def add_edge(self,u , v , weight = 1): #u= intial point , v ending point
        if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
            #assigning the values based on staring and ending points in the matrix with multi directional
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid Vertex")

    def remove_edge(self, u , v):
        if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
            #removing the values based on staring and ending points in the matrix with multi directional
            self.adj_matrix[u][v]= 0
            self.adj_matrix[v][u]= 0
        else:
            print("Invalid Vertex")

    def has_edge(self , u , v):
        if 0<=u<self.vertix_count and 0<=v<self.vertix_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid Vertex")

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str , row_list)))
            

g = Graph(5)
g.add_edge(0,1,34)
g.add_edge(1,2,23)
g.add_edge(1,3,26)
g.add_edge(2,3,37)
g.add_edge(3,4,65)

g.print_adj_matrix()


# 0 34 0 0 0
# 34 0 23 26 0
# 0 23 0 37 0
# 0 26 37 0 65
# 0 0 0 65 0

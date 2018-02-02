
from graphs import Graph, Vertex, Edge

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Complete this function
    if not n:
        return 0
    if c_lib <= c_road:
        return n * c_lib
    graph = Graph()
#    for _n in range(n):
#        graph.addVertex(Vertex(str(_n+1)))
    for edge in cities:
        try:
            graph.addVertex(Vertex(str(edge[0])))
        except KeyError:
            pass
        try:
            graph.addVertex(Vertex(str(edge[1])))
        except KeyError:
            pass
        graph.createEdge(str(edge[0]), str(edge[1]))
    print graph.degree
    subgraphs = graph.listSubGraphs()
    print subgraphs
    libraries = len(subgraphs) + (n - graph.degree)
    roads = 0
    for g in subgraphs:
        roads += len(g) - 1
    return (libraries * c_lib) + (roads * c_road)
    
if __name__ != "__main__":
    exit()

with open('graph_input04.txt') as f:
    q = int(f.readline().strip())
    for a0 in xrange(q):
        n, m, c_lib, c_road = f.readline().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in xrange(m):
            cities_temp = map(int,f.readline().strip().split(' '))
            cities.append(cities_temp)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print result


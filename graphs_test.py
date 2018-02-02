
from graphs import Graph, Vertex, Edge

graph = Graph()

for n in '123456':
    graph.addVertex(Vertex(n))

graph.createEdge('1','2')
graph.createEdge('1','3')
graph.createEdge('2','3')
graph.createEdge('2','4')
graph.createEdge('3','4')
graph.createEdge('5','6')

print graph.listSubGraphs()



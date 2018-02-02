
BIDIRECTIONAL = 0
FORWARD = 1
REVERSE = 2

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.attributes = {'visited':None}
        self.edges = []

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = value

class Edge(object):
    def __init__(self, vertex1, vertex2, direction):
        self.vertices = [vertex1, vertex2]
        self.addresses = {vertex1.name: 0, vertex2.name: 1}
        vertex1.edges.append(self)
        vertex2.edges.append(self)
        self.attributes = {}

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def vertex(self, name):
        return self.vertices[self.addresses[name]]

    def neighbor(self, name):
        return self.vertices[(self.addresses[name] + 1) % 2]

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.visited_flag = 0

    @property
    def degree(self):
        return len(self.vertices)

    def addVertex(self, vertex):
        if vertex.name in self.vertices:
            raise KeyError('refusing to overwrite vertex: %s' % vertex.name)
        self.vertices[vertex.name] = vertex
        return self

    def overwriteVertex(self, vertex):
        if vertex.name in self.vertices:
            self.vertices[vertex.name] = vertex
        return self

    def createEdge(self, name1, name2, d=BIDIRECTIONAL):
        self.edges.append(Edge(self.vertices[name1], self.vertices[name2], d))
        return self

    def clearVisited(self):
        self.visited_flag += 1
#        for name in self.vertices:
#            if not self.vertices[name]['visited']:
#                continue
#            self.vertices[name]['visited'] = False

    def depthFirstSearch(self, start, end=None):
        result = []
        if end is not None and end not in self.vertices:
            return result
        proc_stack = [self.vertices[start]]
        while proc_stack:
            current_vertex = proc_stack.pop()
#            current_vertex['visited'] = True
            current_vertex['visited'] = self.visited_flag
            result.append(current_vertex.name)
            if end is not None and end == current_vertex.name:
                return result
            for edge in current_vertex.edges:
                v = edge.neighbor(current_vertex.name)
#                if v['visited']:
                if v['visited'] == self.visited_flag:
                    continue
                proc_stack.append(v)
#                v['visited'] = True
                v['visited'] = self.visited_flag
        return result

    def breadthFirstSearch(self, start, end=None):
        result = []
        if end is not None and end not in self.vertices:
            return result
        proc_queue = collections.dequeue([self.vertices[start]])
        while proc_queue:
            current_vertex = proc_queue.popleft()
#            current_vertex['visited'] = True
            current_vertex['visited'] = self.visited_flag
            result.append(current_vertex.name)
            if end is not None and end == current_vertex.name:
                return result
            for edge in current_vertex.edges:
                v = edge.neighbor(current_vertex.name)
#                if v['visited']:
                if v['visited'] == self.visited_flag:
                    continue
                proc_queue.append(v)
#                v['visited'] = True
                v['visited'] = self.visited_flag
        return result

    def listSubGraphs(self):
        result = []
        names = {}
        for name in self.vertices:
            if name in names:
                continue
            res = self.depthFirstSearch(name)
            for _r in res:
                names[_r] = True
#            names.extend(res)
            result.append(res)
            self.clearVisited()
        return result


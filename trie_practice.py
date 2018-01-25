# solution.py

PARTIAL_MAX_LENGTH = 5
CACHE_THRESHOLD = PARTIAL_MAX_LENGTH + 1

CACHE_DATA_TYPE_DICT = 'dict'
CACHE_DATA_TYPE_LIST = 'list'

DEFAULT_CACHE_DATA_TYPE = CACHE_DATA_TYPE_DICT

class TrieNode(object):
    def __init__(self, data=None, size=True,
                 data_type=DEFAULT_CACHE_DATA_TYPE):
        self.data = data
        if size:
            self.size = 0
        self.data_type = data_type
        self.vertices = []
        if data_type == CACHE_DATA_TYPE_DICT:
            self.vertices = {}
        
    def edge(self, vertex):
        if hasattr(self, 'size'):
            self.size += 1
        if self.data_type == CACHE_DATA_TYPE_DICT:
            if vertex.data not in self.vertices:
                self.vertices[vertex.data] = vertex
            return self.vertices[vertex.data]
        if vertex not in self.vertices:
            self.vertices.append(vertex)
        return self.vertices[self.vertices.index(vertex)]
    
    def __eq__(self, c):
        if isinstance(c, TrieNode):
            return self.data == c.data
        return self.data == c
    
    def __iter__(self):
        if self.data_type == CACHE_DATA_TYPE_DICT:
            for k in self.vertices.iterkeys():
                yield k
            return
        for o in self.vertices:
            yield o
            
    def __getitem__(self, c):
        if self.data_type == CACHE_DATA_TYPE_DICT:
            return self.vertices[c]
        return self.vertices[self.vertices.index(c)]
    
class Contacts(object):
    def __init__(self, default_data_type):
        self.head = TrieNode(data_type=default_data_type)
    
    def add(self, contact):
        front = self.head
        for i, c in enumerate(contact):
            if i < CACHE_THRESHOLD:
                front = front.edge(TrieNode(ord(c),
                    data_type=self.head.data_type))
                continue
            front = front.edge(TrieNode(ord(c), size=False,
                data_type=self.head.data_type))
        front.edge(TrieNode(data_type=self.head.data_type))

    def find(self, partial):
        front = self.head
        for c in partial:
            if ord(c) not in front:
                print 0
                return
            front = front[ord(c)]
        print front.size

contacts = Contacts('dict')
#contacts = Contacts('list')

with open('input03.txt') as f:
    n = int(f.readline().strip())
    for a0 in xrange(n):
        op, contact = f.readline().strip().split(' ')
        getattr(contacts, op)(contact)


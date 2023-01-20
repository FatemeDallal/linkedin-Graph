class Vertex:
    def __init__(self, user):
        self.data = user
        self.adjV = set()


class Graph:
    def __init__(self):
        self.vertexes = set()

    def add_edge(self, u, v):
        u.adjV.add(v)
        v.adjV.add(u)



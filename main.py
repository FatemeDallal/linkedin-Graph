import json

from Graph import Graph, Vertex
from User import User

if __name__ == '__main__':

    d = open('users.json')

    data = json.load(d)

    users = []

    for i in data:
        users.append(User(
            i
        ))

    d.close()



    # g = Graph()
    #
    # u = Vertex(12)
    # v = Vertex(13)
    # a = Vertex(14)
    # b = Vertex(2)
    #
    # g.add_edge(u, v)
    # g.add_edge(v, a)
    # g.add_edge(b, a)

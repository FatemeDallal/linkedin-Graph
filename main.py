import json

from Graph import Graph, Vertex
from User import User


def search_id(graph_vertex, id):

    for i in graph_vertex:
        if i.data.id == id:
            return i

    return False

if __name__ == '__main__':

    d = open('users.json')

    data = json.load(d)

    users = []

    # read file
    for i in data:
        users.append(User(
            i.get("id"),
            i.get("name"),
            i.get("dateOfBirth"),
            i.get("universityLocation"),
            i.get("field"),
            i.get("workplace"),
            i.get("specialties"),
            i.get("connectionId")
        ))

    d.close()

    graph = Graph()

    # add vertex to graph
    for i in users:
        graph.vertexes.add(Vertex(i))

    # add edge to graph
    for i in graph.vertexes:
        for j in i.data.connection_id:
            temp = search_id(graph.vertexes, j)
            if temp is not False:
                graph.add_edge(i, temp)



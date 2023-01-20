import json

from Graph import Graph, Vertex
from User import User


def search_id(graph_vertex, id):
    for i in graph_vertex:
        if i.data.id == id:
            return i

    return False


def BFS(id):
    bfs = set()
    level = set()

    cnt = 5

    tmp = search_id(id)

    level.add(tmp)

    for i in range(cnt):
        next_level = set()
        for j in level:
            for k in j.data.connection_id:
                t = search_id(k)
                next_level.add(t)
                bfs.add(t)
        level = next_level

    bfs.remove(tmp)

    return bfs


def suggestion(id):
    suggestion_list = []

    return suggestion_list


def get_user(vertexes, name, id):
    check_id = False
    check_name = False
    user = None

    for i in vertexes:
        if i.data.id == id:
            check_id = True
            user = i

    for i in vertexes:
        if i.data.name == name:
            check_name = True

    if check_name and check_id:
        return user
    else:
        return False


def login():

    n = input("Enter your name")
    i = input("Enter your id")

    user = get_user(n, i)
    if user is not False:
        print("1..View the list of users\n2..User search\n3..Offers\n")
        order = int(input("Enter the desired operation code"))

        if order == 1:
            pass

        elif order == 2:
            pass

        elif order == 3:
            pass

        else:
            print("The entered code is incorrect")
    else:
        print("No user found")


def interface():
    while True:
        print("1..signin\n2..signup\n")
        order = int(input("Enter the desired operation code"))

        if order == 1:
            login()

        elif order == 2:
            pass

        else:
            print("The entered code is incorrect")

        # exit


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

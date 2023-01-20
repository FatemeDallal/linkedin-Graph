import json

from Graph import Graph, Vertex
from User import User


def search_id(id):
    for i in graph.vertexes:
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


def more_bfs(bfs, id, first, second):
    llist = set()

    t = search_id(id)

    if first == 1:

        for i in bfs:
            if i.data.university_location == t.data.university_location and len(llist) < 21:
                llist.add(i)

    elif first == 2:

        for i in bfs:
            if i.data.field == t.data.field and len(llist) < 21:
                llist.add(i)

    elif first == 3:

        for i in bfs:
            if i.data.work_place == t.data.work_place and len(llist) < 21:
                llist.add(i)

    elif first == 4:

        for i in bfs:
            for j in i.data.specialties:
                for k in t.data.specialties:
                    if j == k:
                        llist.add(i)
                        break

    if len(llist) < 20:

        if second == 1:

            for i in bfs:
                if i.data.university_location == t.data.university_location and len(llist) < 21:
                    llist.add(i)

        elif second == 2:

            for i in bfs:
                if i.data.field == t.data.field and len(llist) < 21:
                    llist.add(i)

        elif second == 3:

            for i in bfs:
                if i.data.work_place == t.data.work_place and len(llist) < 21:
                    llist.add(i)

        elif second == 4:

            for i in bfs:
                for j in i.data.specialties:
                    for k in t.data.specialties:
                        if j == k:
                            llist.add(i)
                            break

    if len(llist) < 20:

        for i in bfs:
            llist.add(i)

    else:
        return llist


def fewer_bfs(bfs, id, first, second):

    llist = set()

    for i in bfs:
        llist.add(i)

    t = search_id(id)

    if first == 1:

        for i in graph.vertexes:
            if i.data.university_location == t.data.university_location and len(llist) < 21:
                llist.add(i)

    elif first == 2:

        for i in graph.vertexes:
            if i.data.field == t.data.field and len(llist) < 21:
                llist.add(i)

    elif first == 3:

        for i in graph.vertexes:
            if i.data.work_place == t.data.work_place and len(llist) < 21:
                llist.add(i)

    elif first == 4:

        for i in graph.vertexes:
            for j in i.data.specialties:
                for k in t.data.specialties:
                    if j == k:
                        llist.add(i)
                        break

    if len(llist) < 20:

        if second == 1:

            for i in graph.vertexes:
                if i.data.university_location == t.data.university_location and len(llist) < 21:
                    llist.add(i)

        elif second == 2:

            for i in graph.vertexes:
                if i.data.field == t.data.field and len(llist) < 21:
                    llist.add(i)

        elif second == 3:

            for i in graph.vertexes:
                if i.data.work_place == t.data.work_place and len(llist) < 21:
                    llist.add(i)

        elif second == 4:

            for i in graph.vertexes:
                for j in i.data.specialties:
                    for k in t.data.specialties:
                        if j == k:
                            llist.add(i)
                            break

    return llist


def suggestion(id, first, second):
    suggestion_list = []

    bfs_list = BFS(id)

    if len(bfs_list) > 20:

        suggestion_list = more_bfs(bfs_list, id, first, second)

    elif len(bfs_list) < 20:

        suggestion_list = fewer_bfs(bfs_list, id, first, second)

    else:
        suggestion_list = bfs_list

    return suggestion_list


def get_user(name, id):
    check_id = False
    check_name = False
    vertex = None

    for i in graph.vertexes:
        if i.data.id == id:
            check_id = True
            vertex = i

    for i in graph.vertexes:
        if i.data.name == name:
            check_name = True

    if check_name and check_id:
        return vertex
    else:
        return False


def login():
    n = input("Enter your name")
    i = input("Enter your id")

    vertex = get_user(n, i)
    if vertex is not False:
        print("1..View the list of users\n2..User search\n3..Offers\n")
        order = int(input("Enter the desired operation code"))

        if order == 1:
            pass

        elif order == 2:
            pass

        elif order == 3:
            print("1..university location\n2..field\n3..work place\n4..specialties")
            operation_first = int(input("Enter the first priority"))
            operation_second = int(input("Enter the second priority"))

            offers = suggestion(vertex.data.id, operation_first, operation_second)

            print("\n")
            cnt = 0
            for i in offers:
                if cnt < 20:
                    print(i.data.id, i.data.name, i.data.field, i.data.work_place, i.data.specialties)
                    cnt += 1
                else:
                    break
            print("\n")

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

        n = int(input("Are you exit\n1..Yes  2..No"))
        if n == 1:
            break



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
            temp = search_id(j)
            if temp is not False:
                graph.add_edge(i, temp)

    interface()

import json

from Graph import Graph, Vertex
from User import User


def contain(id, ids):
    for i in ids:
        if i == id:
            return True

    return False


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


def edit_datas(id, ids_person):

    v = search_id(id)
    ids_person = str(ids_person)
    u = search_id(ids_person)
    graph.add_edge(u, v)

    v.data.connection_id.append(ids_person)
    u.data.connection_id.append(id)

    d = open('users.json')

    data = json.load(d)

    for i in data:
        if i.get("id") == id:
            i["connectionId"].append(ids_person)

    for i in data:
        if i.get("id") == ids_person:
            i["connectionId"].append(id)

    with open('users.json', 'w') as f:
        json.dump(data, f, indent=2)

    f.close()


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
                    print(
                        "id : " + i.data.id + " , " + "name : " + i.data.name + " , " + "field : " + i.data.field + " , " +
                        "university location : " + i.data.university_location + " , " + "workplace : " + i.data.work_place + " , " +
                        "specialties :", i.data.specialties)
                    if contain(vertex.data.id, i.data.connection_id):
                        print("You connected to this person")
                    else:
                        print("You are not connected to this person")
                    cnt += 1
                else:
                    break
            print("\n")

            yse_no = int(input("Do you want to communicate with any of these people?\n1..Yes 2..No"))

            if yse_no == 1:

                while True:

                    id_person = int(input("Enter id's person"))

                    edit_datas(vertex.data.id, id_person)

                    no_yes = int(input("Is it still individual?\n1..Yes 2..No"))
                    if no_yes == 2:
                        break

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

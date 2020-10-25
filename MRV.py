import Model
import copy
import math


def dfs2(graph, domain):
    vertices = graph.getVertices()
    used_domain = []
    dfsUtil2(vertices, 0, domain, used_domain)


def dfsUtil2(vertices, k, domain, used_domain):
    if len(used_domain) == len(domain) or k == len(vertices):
        return
    for i in domain:
        if i not in used_domain:
            print(str(vertices[k]) + "=", str(i))
            used_domain_copy = copy.deepcopy(used_domain)
            used_domain_copy.append(i)

            dfsUtil2(vertices, k + 1, domain, used_domain_copy)


def getSortedVerticesMRV(graph):
    vertices = graph.getVertices()
    vertices.sort(key=lambda x: graph.degree(x), reverse=True)
    return vertices


if __name__ == "__main__":
    f1 = Model.Faculty("F1", ["8:30", "10:00", "11:40"], ["8:30", "10:00", "13:30", "15:00"], [], ["11:40", "13:30"],
                       ["10:00", "11:40", "13:30"])
    l1 = Model.Lesson("l1", "11:40", Model.Teacher("Jett"), ["s2", "s222", "s3333"], True)
    l2 = Model.Lesson("l2", "10:00", Model.Teacher("Brimstone"), ["s134", "s2", "s6"], False)
    l3 = Model.Lesson("l3", "11:40", Model.Teacher("Raze"), ["s1", "s22", "s5"], True)
    l4 = Model.Lesson("l4", "13:30", Model.Teacher("Sage"), ["s1", "s22", "s4"], False)
    l5 = Model.Lesson("l5", "8:30", Model.Teacher("Sage"), ["s111", "s2", "s3"], True)
    l6 = Model.Lesson("l6", "11:40", Model.Teacher("Cypher"), ["s1", "s2", "s8"], True)
    l7 = Model.Lesson("l7", "15:00", Model.Teacher("Brimstone"), ["s1", "s2", "s3"], True)
    l8 = Model.Lesson("l8", "8:30", Model.Teacher("Brimstone"), ["s17", "s2", "s3"], False)
    l9 = Model.Lesson("l9", "10:00", Model.Teacher("Raze"), ["s15", "s112", "s9"], True)
    l10 = Model.Lesson("l10", "10:00", Model.Teacher("t1"), ["s16", "s12", "s10"], False)
    G = Model.Graph(["a", "b", "c", "d"])
    G.addEdge("a", "b")
    G.addEdge("b", "c")

    s1 = Model.Schedule(f1, [l1, l7, l2], [l1, l3, l4], [l1, l3, l4], [l1, l3, l4], [l1, l3, l4])
    # G.addEdge("b", "d")
    # d = [1, 2, 3, 4]
    '''
    for i in range(len(s1.monday.getNeigbours(l2))):
        print(s1.monday.getNeigbours(l2)[i])

    print("_________________")
    for i in range(len(s1.monday.getNeigbours(l1))):
        print(s1.monday.getNeigbours(l1)[i])
        '''
    sorted_vertices = getSortedVerticesMRV(s1.monday)
    for i in range(len(s1.monday.getVertices())):
        print(sorted_vertices[i])
    for j in range(len(s1.monday.getVertices())):
        print(s1.monday.getVertices()[j])
    # dfs2(G, d)
    print("finish")

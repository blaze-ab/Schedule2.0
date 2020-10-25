import Model
import copy
import math


def constraintSchedule(list, i):
    return False


def constraint(list_of_pairs, i):
    list_of_val = []
    for pair in list_of_pairs:
        list_of_val.append(pair[1])
    return i in list_of_val


def CSP(schedule):
    con = constraintSchedule
    csp(schedule.monday, schedule.faculty.monday, con)
    print("\n")
    #csp(schedule.tuesday, schedule.faculty.tuesday, con)
    #print ("\n")
    #csp(schedule.wednesday, schedule.faculty.wednesday, con)
    #print ("\n")
    #csp(schedule.thursday, schedule.faculty.thursday, con)
    #print ("\n")
    #csp(schedule.friday, schedule.faculty.friday, con)


def csp(graph, domain, constraint):
    if len(domain) < graph.maxDegree():
        return "???"
    used_domain = []
    b = False
    cspUtil(graph, getSortedVerticesMRV(graph), 0, domain, used_domain, constraint, b)


def cspUtil(graph, vertices, k, domain, used_domain, constraint, finished):
    if k >= len(vertices):
        global kek
        kek = True
        print("\n")
        return
    for i in domain:
        if not constraint(graph.getNeigbours(vertices[k]), i):
            if kek:
                return 
            if not constraint(graph.getNeigbours(vertices[k]), i):
                
                print(str(vertices[k]) + "move to", str(i))
                
                graph.graph[(vertices[k][0], i)] = graph.graph.pop(vertices[k])
                used_domain_copy = copy.deepcopy(used_domain)
                used_domain_copy.append(i)
                
                cspUtil(graph, vertices, k + 1, domain, used_domain_copy, constraint, finished)
            else : 
                return


def getSortedVerticesMRV(graph):
    vertices = graph.getVertices()
    vertices.sort(key=lambda x: graph.degree(x), reverse=True)
    return vertices


kek = False


if __name__ == "__main__":
    G = Model.Graph([( "a",0), ("b",0), ("c",0), ("d",0)])
    G.addEdge(("a",0),("b",0))
    G.addEdge(("b",0),("c",0))
    G.addEdge(("c",0),("d",0))
    G.addEdge(("a",0),("d",0))
    D = [1,2,3]
    csp(G,D,constraint)

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

    s1 = Model.Schedule(f1, [l1, l7, l2, l3], [l1, l3, l4], [l1, l3, l4], [l1, l3, l4], [l1, l3, l4])

    #CSP(s1)
    print("finish")

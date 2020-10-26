import Model
import copy
import math


def constraintSchedule(lessons, time):
    for lesson in lessons:
        if lesson.time == time:
            return True
    return False


def CSP(schedule):
    con = constraintSchedule
    monday_copy = csp(schedule.monday, schedule.faculty.monday, con).getVertices()
    # print("\n")
    tuesday_copy = csp(schedule.tuesday, schedule.faculty.tuesday, con).getVertices()
    # print("\n")
    wednesday_copy = csp(schedule.wednesday, schedule.faculty.wednesday, con).getVertices()
    # print("\n")
    thursday_copy = csp(schedule.thursday, schedule.faculty.thursday, con).getVertices()
    # print("\n")
    friday_copy = csp(schedule.friday, schedule.faculty.friday, con).getVertices()
    return Model.Schedule(schedule.faculty, monday_copy, tuesday_copy, wednesday_copy, thursday_copy, friday_copy)


def csp(graph, domain, constraint):
    if len(domain) < graph.maxDegree():
        raise NameError("schedule is incompatible with the model")
    global DONE
    DONE = False
    return cspUtil(graph, copy.deepcopy(graph), getSortedVertices(graph), 0, domain, constraint)


def cspUtil(graph, graph_copy, vertices, k, domain, constraint):
    if k >= len(vertices):
        global DONE
        DONE = True
        print("\n")
        return graph_copy
    for i in domain:
        if not constraint(graph_copy.getNeighbours(vertices[k]), i):
            if DONE:
                return graph_copy

            print(str(vertices[k]) + "move to", str(i))
            changeTime(graph_copy, vertices[k], i)

            return cspUtil(graph, graph_copy, vertices, k + 1, domain, constraint)
    


def getSortedVertices(graph):
    vertices = graph.getVertices()
    vertices.sort(key=lambda x: graph.degree(x), reverse=True)
    return vertices


def changeTime(graph_day, lesson_vertex, time):
    lesson = graph_day.getVertex(lesson_vertex)
    lesson.time = time


DONE = False
if __name__ == "__main__":

    f1 = Model.Faculty("F1", ["8:30", "10:00", "11:40"], ["8:30", "10:00", "13:30", "15:00"],
                       ["10:00", "11:40", "13:30"], ["11:40", "13:30"], ["10:00", "11:40", "13:30"])
    l1 = Model.Lesson("l1", "11:40", Model.Teacher("Jett"), ["s2", "s222", "s3333"], True)
    l2 = Model.Lesson("l2", "10:00", Model.Teacher("Brimstone"), ["s134", "s2", "s6"], False)
    l3 = Model.Lesson("l3", "11:40", Model.Teacher("Raze"), ["s1", "s22", "s5"], True)
    l4 = Model.Lesson("l4", "13:30", Model.Teacher("Sage"), ["s1", "s22", "s4"], False)
    l5 = Model.Lesson("l5", "8:30", Model.Teacher("Sage"), ["s111", "s2", "s3"], True)
    l6 = Model.Lesson("l6", "11:40", Model.Teacher("Cypher"), ["s1", "s2", "s8"], True)
    l7 = Model.Lesson("l7", "15:00", Model.Teacher("Brimstone"), ["s1", "s2", "s3"], True)
    l8 = Model.Lesson("l8", "8:30", Model.Teacher("Brimstone"), ["s17", "s2", "s3"], False)
    l9 = Model.Lesson("l9", "10:00", Model.Teacher("Raze"), ["s15", "s112", "s9"], True)
    l10 = Model.Lesson("l10", "10:00", Model.Teacher("Skye"), ["s16", "s12", "s10"], False)
    G = Model.Graph(["a", "b", "c", "d"])
    G.addEdge("a", "b")
    G.addEdge("b", "c")

    s1 = Model.Schedule(f1, [l1, l7, l2, l3], [l3, l5, l6, l7],
                        [l6, l7, l8], [l8, l9, l2], [l1, l3, l9])
    #print( s1.friday.getNeighbours(l3))


    print(CSP(s1))
    print("finish")

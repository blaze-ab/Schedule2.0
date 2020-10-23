import random
import copy

DAYS = 5


class Faculty:
    def __init__(self, name, d1, d2, d3, d4, d5):
        self.name = name
        self.monday = d1
        self.tuesday = d2
        self.wednesday = d3
        self.thursday = d4
        self.friday = d5

    def get(self, i):
        if i == 1:
            return self.monday
        if i == 2:
            return self.tuesday
        if i == 3:
            return self.wednesday
        if i == 4:
            return self.thursday
        if i == 5:
            return self.friday
        return self.monday


class Teacher:
    def __init__(self, name):  # String
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name


class Lesson:
    def __init__(self, name, time, t, students, lecture, audience):  # String, Teacher, Array String, bool
        self.name = name
        self.time = time  # "01052020.1500"
        self.teacher = t
        self.students = students
        self.lecture = lecture

    def isLecture(self):
        return self.lecture

    def __eq__(self, other):
        return self.name == other.name \
               and self.teacher == other.teacher and self.isLecture() == other.isLecture()

    def __str__(self):
        objLesson = "Time: " + self.time + "\n" + "Subject: " + self.name + "\n" + \
                    "Teacher: " + self.teacher.__str__() + "\n"
        if self.lecture:
            objLesson += "Lecture." + "\n"
        return objLesson


class Schedule:
    def __init__(self, faculty, m, t, w, tr, f):  # String, rest: list of lessons that eventually turn into graphs
        self.faculty = faculty
        self.monday = Graph(m)
        self.tuesday = Graph(t)
        self.wednesday = Graph(w)
        self.thursday = Graph(tr)
        self.friday = Graph(f)

    def get(self, i):
        if i == 1:
            return self.monday
        if i == 2:
            return self.tuesday
        if i == 3:
            return self.wednesday
        if i == 4:
            return self.thursday
        if i == 5:
            return self.friday
        return self.monday

    def setDay(self, i, lessons):
        if i == 1:
            self.monday = lessons
        elif i == 2:
            self.tuesday = lessons
        elif i == 3:
            self.wednesday = lessons
        elif i == 4:
            self.thursday = lessons
        elif i == 5:
            self.friday = lessons

    def scheduleM(self):
        mon = ""
        for x in self.monday.getVertices():
            mon += x.__str__()
            mon += "____________________" + "\n"
        return mon

    def scheduleT(self):
        tues = ""
        for x in self.tuesday.getVertices():
            tues += x.__str__()
            tues += "____________________" + "\n"
        return tues

    def scheduleW(self):
        wed = ""
        for x in self.wednesday.getVertices():
            wed += x.__str__()
            wed += "____________________" + "\n"
        return wed

    def scheduleTR(self):
        thur = ""
        for x in self.thursday.getVertices():
            thur += x.__str__()
            thur += "____________________" + "\n"
        return thur

    def scheduleF(self):
        frid = ""
        for x in self.friday.getVertices():
            frid += x.__str__()
            frid += "____________________" + "\n"
        return frid

    def __str__(self):
        return "Faculty: " + self.faculty.name + "\n" + "\n" + "Monday: \n" + self.scheduleM() + "\n" + \
               "Tuesday: \n" + self.scheduleT() + "\n" + "Wednesday: \n" + self.scheduleW() + "\n" + \
               "Thursday: \n" + self.scheduleTR() + "\n" + "Friday: \n" + self.scheduleF() + "\n"


# variable is (time of a lesson, day)
# domain: time is determined by the faculty's time constraints, and Monday<=day<=Friday

# restrictions are: lesson1.time != lesson2.time if(lesson1.teacher == lesson2.teacher or
# for any i lesson1.students[i] == lesson2.students[i])
# returns true if lessons fit the constraints mentioned above
def shouldConnect(lesson1, lesson2):
    if lesson1.name != lesson2.name or lesson1.time != lesson2.time:
        return False
    if lesson1.teacher == lesson2.teacher and lesson1.lecture == lesson2.lecture:
        return True
    for student in lesson1.students:
        if student in lesson2.students:
            return False
    return True


class Graph:
    def __init__(self, graph_elements=None):
        if graph_elements is None:
            self.graph = {}
        else:
            for v in graph_elements:
                self.graph[v] = []

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.graph.keys())

    def addVertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def removeVertex(self, v):
        self.graph.pop(v)
        for vertex in self.graph:
            if v in self.graph[vertex]:
                self.removeEdge(vertex, v)

    def AddEdge(self, v1, v2):
        if v2 in self.graph[v1]:
            return
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

    def removeEdge(self, v1, v2):
        self.graph[v1].pop(v2)
        if v2 in self.graph:
            self.graph[v2].pop(v1)


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
        self.audience = audience

    def isLecture(self):
        return self.lecture

    def __eq__(self, other):
        return self.name == other.name and self.audience == other.audience \
               and self.teacher == other.teacher and self.isLecture() == other.isLecture()

    def __str__(self):
        objLesson = "Time: " + self.time + "\n" + "Subject: " + self.name + "\n" +\
                    "Teacher: " + self.teacher.__str__() + "\n" + "Audience: " + self.audience + "\n"
        if self.lecture:
            objLesson += "Lecture." + "\n"
        return objLesson


class Audience:
    def __init__(self, num, seats):  # int, int
        self.number = num
        self.seats = seats

    def __eq__(self, other):
        return self.number == other.number and self.seats == other.seats

    def __str__(self):
        return "Audience: " + self.number + "\n" + "Number of seats: " + self.seats + "\n"


class Schedule:
    def __init__(self, faculty, m, t, w, tr, f):  # String, rest: LessonArray
        self.faculty = faculty
        self.monday = m
        self.tuesday = t
        self.wednesday = w
        self.thursday = tr
        self.friday = f

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
        for x in self.monday:
            mon += x.__str__()
            mon += "____________________" + "\n"
        return mon

    def scheduleT(self):
        tues = ""
        for x in self.tuesday:
            tues += x.__str__()
            tues += "____________________" + "\n"
        return tues

    def scheduleW(self):
        wed = ""
        for x in self.wednesday:
            wed += x.__str__()
            wed += "____________________" + "\n"
        return wed

    def scheduleTR(self):
        thur = ""
        for x in self.thursday:
            thur += x.__str__()
            thur += "____________________" + "\n"
        return thur

    def scheduleF(self):
        frid = ""
        for x in self.friday:
            frid += x.__str__()
            frid += "____________________" + "\n"
        return frid

    def __str__(self):
        return "Faculty: " + self.faculty.name + "\n" + "\n" + "Monday: \n" + self.scheduleM() + "\n" + \
               "Tuesday: \n" + self.scheduleT() + "\n" + "Wednesday: \n" + self.scheduleW() + "\n" + \
               "Thursday: \n" + self.scheduleTR() + "\n" + "Friday: \n" + self.scheduleF() + "\n"


# +4 to our "weight" if there is conflict in audiences, +2 - in teachers' schedules, +1 - students
def checkConflictsStudent(ss1, ss2):
    weightCS = 0
    for s in ss1:
        if s in ss2:
            weightCS += 1
    return weightCS


def randomizedTime(l, day):
    return Lesson(l.name, random.choice(day), l.teacher, l.students, l.lecture, l.audience)


def randomizedSchedule(schedule):
    res = Schedule(schedule.faculty, [], [] ,[] , [] , [])
    for i in range(DAYS):
        for l in schedule.get(i):
            res.get(i).append(randomizedTime(l, schedule.faculty.get(i)) )
    return res




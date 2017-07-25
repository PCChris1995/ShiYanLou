#!/usr/bin/env python3

import sys
from collections import Counter

grade = sys.argv[2]
types = sys.argv[1]

class Person(object):

    def __init__(self, name):
        self.name = name

    def get_grade(self, grade):
        s = Counter(grade).most_common()
        if types  == "teacher":
            print('A: {}, B: {}, C: {}, D: {}'.format(s['A'],s['B'],s['C'],s['D']))
        elif types  == "student":
            Pass = s['A'] + s['B'] + s['C']
            Fail = s['D']
            print('Pass: {}, Fail; {}'.format(Pass, Fail))
class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers
    def get_grade():
        return "{} teaches {}".format(self.name, ','.join(self.papers))
print('type = {}, grade = {}'.format(sys.argv[1], sys.argv[2]))

print(Person.get_grade(grade))








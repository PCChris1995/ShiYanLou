#!/usr/bin/env python3

import sys
from collections import Counter

grade = sys.argv[2]
types = sys.argv[1]

class Person(object):

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_grade(self, grade):
        s = Counter(grade).most_common()
        if types  == "teacher":
            item = ['{}: {}'.format(k, v) for (k, v) in s]
            return ','.join(item)
        elif types  == "student":
            return 'Pass: {}, Fail: {}'.format(len(grade) - grade.count('D'), grade.count('D') )

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

kind = Person(types, grade)
print(kind.get_grade(grade))








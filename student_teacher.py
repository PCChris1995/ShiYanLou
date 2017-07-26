#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_grade(self, grade):
        s = Counter(self.grade).most_common()
        if self.name  == "teacher":
            item = ['{}: {}'.format(k, v) for (k, v) in s]
            return ', '.join(item)
        elif self.name  == "student":
            return 'Pass: {}, Fail: {}'.format(len(self.grade) - self.grade.count('D'), self.grade.count('D') )

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
if __name__ == '__main__':
    if len(sys.argv) > 2:
        kind = Person(sys.argv[1], sys.argv[2])
        print(kind.get_grade(sys.argv[2]))
    else:
        sys.exit(-1)







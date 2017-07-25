#!/usr/bin/env python3

import sys
from collection import counter

type = 

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_grade(self):

        s = counter(grade).most_common()

        if type == "teacher":

            print('A: {}, B: {}, C: {}, D: {}'.format(s['A'],s['B'],s['C'],s['D']))

        elif type == "student":

            Pass = s['A'] + s['B'] + s['C']

            Fail = s['D']

            print('Pass: {}, Fail; {}'.format(Pass, Fail))

class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_grade(self):
        """
        返回包含学生具体信息的字符串
        """
        

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_grade():
        return "{} teaches {}".format(self.name, ','.join(self.papers))

print()








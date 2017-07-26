#!/usr/bin/env python3

def my_decorator(func):
    
    def wrapper(*a, **b):

        print("the result is:")

        result = func(*a, **b)

        return result
    
    return wrapper

@my_decorator

def add(a, b):

    return a + b

print(add(3,4))            

@my_decorator

def funcd(A, B):

    return A * B

print(funcd(5, 6))


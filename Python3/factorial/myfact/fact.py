#!/usr/bin/env/ python3

"myfact module"

def factorial(num):
    
    if num > 0:

        return num * factorial( num - 1 )

    elif num == 0:

        return 1

    else:

        return -1




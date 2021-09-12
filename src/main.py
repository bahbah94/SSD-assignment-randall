import logging,time,inspect,contextlib,io,cmath
import pandas as pd

from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4


#takes a list and returns a list of even numbers
#@decorator_1
#@decorator_2
#@decorator_3
#@decorator_4
def f1(lst):
    '''
    This function takes a list and returns a list of numbers divisible by 2
    '''
    lst = list(filter(lambda x: x%2==0,lst))
    return lst

#takes coefficients of quadratic equation and returns the roots.
#@decorator_1
#@decorator_2
#@decorator_3
#@decorator_4
def quadratic(a,b,c):
    '''
    this function takes three coefficients and returns the root of a quadratic eqaution
    given those arguments
    '''
    discriminant = (b**2)-(4*a*c)

    sol1 = (-b-cmath.sqrt(discriminant))/(2*a)
    sol2 = (-b+cmath.sqrt(discriminant))/(2*a)

    return (sol1,sol2)

#@decorator_1
#@decorator_2
#@decorator_3
#@decorator_4
def pascal_triangle(n):
    '''
    This function takes an integer and prints the first n rows
    of pascals triangle
    '''
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow = [l+r for l,r in zip(trow+y,y+trow)]

#@decorator_1
#@decorator_2
#@decorator_3
#@decorator_4
def transform(lst):
    '''
    This function takes a list and transforms it to square the elements of the list
    '''
    lst = list(map(lambda x: x**2,lst))
    return lst



if __name__ == "__main__":
    transform([1,2,3])
    transform([2,3,4])
    pascal_triangle(5)
    quadratic(3,4,56)
    pascal_triangle(3)
    f1([3,4])
    f1([5,6,7],8)

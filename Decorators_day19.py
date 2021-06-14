# Decorators and the @ symbol (@ is just used for the convinience)

'''In general, if func is a decorator function, we decorate 
another function my_func using:'''
from typing import Counter


my_func = func(my_func)

This is so common that python provides a convinient way of writing that:


@func
def my_func(..):
    ...function


is the same as writting


def my_func(...):
    ...function


my_func = func(my_func)

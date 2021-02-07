"""importing modules"""
import calculator
"""import calculator as c/       alias"""
#import calculator as calc

result=calculator.adder(2,2)
print(result)


resultl=calculator.subtractor(2,2)
print(resultl)
""" imporitng only required functions """

from calculator import adder as plus,subtractor as minus
result=plus(7,7)
print("using alias", result)


resultl=minus(-7,-7)
print(resultl)

from package import calculator
result=calculator.adder(9,2)
print(result)


resultl=calculator.subtractor(12,2)
print("importing through packages", resultl)

from package.calculator import adder
result=calculator.adder(19,2)
print(result)

from calculator import *
print(adder(36,35))

from package import *
print(adder(2,7))


import sys
print(sys.path)

#write a sorting algorithm
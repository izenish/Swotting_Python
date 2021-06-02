#!/bin/python3
#CountingValley Challenge

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    length=10
    height=0
    count=0
    # sealevel=0
    for i in path:
        if i=="U" :
            height+=1
            if(height==0):
                count+=1
            
        elif i=="D":
            height-=1
    return count
        # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

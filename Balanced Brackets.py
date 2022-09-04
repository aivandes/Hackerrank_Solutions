#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    if len(s)<1:
        return "NO"
    
    if len(s)%2 != 0:
        return "NO"
    
    stack = []
    left = ["{",  "(",  "["]
    right = ["}", ")", "]"]
    for i in s:
        
        if i in left:
            stack.append(i)
        try:        
            if i in right and right[left.index(stack.pop())] == i:
                continue
        except:
            return "NO"
        
        if i in right and stack and right[left.index(stack.pop())] != i:
            return "NO"
    
    return "YES" if not stack else "NO"
            
        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

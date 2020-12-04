#!/usr/bin/python3
#coding=utf-8

    # Solution 1: Buggy
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
       # Solution 1
        num_lst = list(str(x))
        while(len(num_lst) > 1):
            if(num_lst.pop(-1) != num_lst.pop()):
                return False
        return True
'''

    # Solution 2
    num_lst = list(str(x))
    L = 0
    R = len(num_lst) - 1
    while (L <= R):
        if(num_lst[L] != num_lst[R]):
        return False
        L += 1
        R -= 1
    return True
        


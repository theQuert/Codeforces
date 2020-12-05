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
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_lst = list(str(x))
         L = 0
         R = len(num_lst) - 1
         while (L <= R):
             if(num_lst[L] != num_lst[R]):
                  return False
             L += 1
             R -= 1
        return True
    
    # Solution 3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            import math
            length = int(math.log(x, 10)) + 1
            reverse_x = 0
            for i in range(length // 2):
                remainder = x % 10
                x = x // 10
                reverse_x = reverse_x * 10 + remainder
            if reverse_x == x or reverse_x == x // 10:
                return True
            else:
                return False









                
            


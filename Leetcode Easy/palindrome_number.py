# -*- coding: utf-8 -*-
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

#Inputs
x = 121

#Solution
    converted_x = str(x)
    answer = True
    for i in range(len(converted_x)-1):
      if converted_x[i] == converted_x[len(converted_x)-1-i]:
        if answer == False:
          pass
        else:
          answer = True
      else:
        answer = False

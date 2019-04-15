# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:43:10 2019

@author: akash
"""
str="  123 i am a"
state = [{},{' ': 1, '+': 2, '-': 2, 'digit': 2},{'digit': 2}]
currState = 1
answer = 0
sign = 1
index = 0
while index < len(str):
    char = str[index]
            
    if char >= '0' and char <= '9':
        answer = answer * 10
        answer += ord(char) - ord('0')
        char = 'digit'
                
    if currState == 1 and char == '-':
        sign = -1
            
    if char not in state[currState].keys():
        break

    if sign * answer < -2147483648:
        print( -2147483648)
                
    if sign * answer > 2147483647:
        print( 2147483647)
                
    currState = state[currState][char]
    index = index + 1
                
print( sign * answer)
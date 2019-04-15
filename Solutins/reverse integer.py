x=123
reverse=0
sign = 1
if x < 0:
    sign = -1
x = abs(x)    
while(x>0):
    rem=x%10
    reverse=(reverse*10)+rem
    x=x//10
    if(reverse*sign>= 2147483647 or reverse*sign <= -2147483648):
        print( 0)
    else:
print( reverse*sign)
def firstcode(sum,n):
    for i in range(n):
        sum += i
    return sum
'''
this is a function to calculate the sum of first n numbers
'''
print("Sum of first 5 numbers is:",firstcode(0,5))
    

def secondcode(sub,n):
    for i in range(n):
        sub -= i
    return sub
'''
this is a function to calculate the subtraction of first n numbers
'''
print("Subtraction of first 5 numbers is:",secondcode(0,5)) 
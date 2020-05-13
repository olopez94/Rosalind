'''
Problem
  Given: Two positive integers a and b (a<b<10000).
  Return: The sum of all odd integers from a through b, inclusively.
'''

a = 100
b = 200
c = 0

for i in range(a, b):
  if i%2 == 1:
    c += i
print(c)    
 

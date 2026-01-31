'''
1 666
2 1666
3 2666

6 5666

9 8666
10 

작은 케이스


'''
import sys
n = int(input())
count = 0

for i in range(sys.maxsize):
    if str(i).count("666") >= 1:
        count += 1    
    if count == n:
        print(i)
        break


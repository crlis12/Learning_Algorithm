

a, b, c = map(int,input().split())

sorted_num = sorted([a, b, c ])
result = 0


if sorted_num[0] + sorted_num[1] > sorted_num[2]:
    result = sorted_num[0] + sorted_num[1] + sorted_num[2]
else:
    result = sorted_num[0] + sorted_num[1] + sorted_num[0] + sorted_num[1] - 1
    
print(result)
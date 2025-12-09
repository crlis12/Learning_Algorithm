n = int(input())
sum = 0
d = 0

while sum < n:
    d += 1
    sum += d
    
diff = sum - n
    
    
if d % 2 == 1:  # 홀수 줄
    num = 1 + diff
    den = d - diff
else:           # 짝수 줄
    num = d - diff
    den = 1 + diff

print(f"{num}/{den}")
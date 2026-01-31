n = int(input())
answer = []

while(True):
    # print(n)
    if n == 1:
        print(answer.count(1) + 1)
        break
    
    answer.append(n%2)
    # print(answer)
    n = n // 2
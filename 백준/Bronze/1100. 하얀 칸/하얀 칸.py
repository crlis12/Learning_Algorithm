answer = []
count = 0

for _ in range(8):
    answer.append(input().strip())   # 한 줄 문자열 그대로 저장
for i in range(8):
    j = answer[i]                    # j는 한 줄 문자열
    if i % 2 == 0:                   # 짝수 행: 0,2,4,6
        cols = range(0, 8, 2)
    else:                            # 홀수 행: 1,3,5,7
        cols = range(1, 8, 2)

    for z in cols:
        if j[z] == "F":
            count += 1

print(count)

'''
첫쨰 줄에 색종이의 수

첫 번째 자연수 = 색종이의 왼쪽   변과의 거리
두 번째 자연수 = 색종이의 아래쪽 변과의 거리


'''

n = int(input())

paper = []
for i in range(100):
    row = [0] * 100
    paper.append(row)

count = 0
for _ in range(n):
    x, y = input().split()
    
    x, y = int(x), int(y)
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1
            
for i in range(100):
        for j in range(100):
            if paper[i][j] == 1:
                count += 1
                
print(count)
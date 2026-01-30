def solution(n):
    answer = 0

    list_n = list(map(int,str(n)))
    for i in list_n:
        answer += i
    return answer
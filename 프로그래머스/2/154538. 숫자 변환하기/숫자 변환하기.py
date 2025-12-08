from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    # 방문 체크용 배열 (x와 y의 범위에 따라 적당히)
    # 문제에서 y 최대가 1,000,000 이라면 그 정도 크기까지 보면 됨
    max_val = y
    visited = [False] * (max_val + 1)

    q = deque()
    q.append((x, 0))  # (현재 값, 사용한 연산 수)
    visited[x] = True

    while q:
        cur, cnt = q.popleft()

        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt == y:
                return cnt + 1
            if nxt <= max_val and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))

    # 여기까지 왔다는 건 어떤 연산을 해도 y를 못 만든다는 뜻
    return -1

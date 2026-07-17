def solution(n):
    answer = 0
    a= len(str(n))

    n = list(str(n))
    n = list(map(int, n))

    for i in range(a):
        answer +=  n[i]

    return answer
def solution(n):
    n = list(str(n))
    n.sort()
    n.reverse()
    print(n)
    answer = int("".join(n))
    return answer
def solution(A,B):
    answer = 0
    A.sort()
    A.reverse()
    B.sort()

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
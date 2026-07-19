def solution(n):
    answer = 0

    for i in range(n-1):

        if i == 0:
            pass
        elif n%i == 1:
            answer += i
            break

    if answer == 0:
        answer += n-1

    return answer
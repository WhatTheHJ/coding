def solution(numbers):
    a = list(range(10))
    answer = 0

    for i in numbers:
        if i in a:
            a.remove(i)

    answer = sum(a)
    return answer
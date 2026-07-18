def solution(n):
    answer = 0
    a = n ** 0.5 
    print(type(a))

    if a.is_integer()  :
        answer = (a+1) * (a+1)
    else:
        return -1

    return int(answer)
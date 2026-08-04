def solution(s):
    answer = ''
    answer = list(answer)

    if len(s)%2 == 0:
        answer.append(s[(len(s)//2)-1])
        answer.append(s[(len(s)//2)])
    else:
        answer.append(s[(len(s)//2)])

    answer = ''.join(answer)

    return answer
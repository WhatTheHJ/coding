def solution(n):
    answer = True
    n = list(n.upper())
    p_count = 0
    y_count = 0

    for i in range(len(n)):
        if n[i]=="P":
            p_count +=1
        if n[i]=="Y":
            y_count += 1
    
    if p_count == y_count:
        answer= True
    else:
        answer = False

    return answer
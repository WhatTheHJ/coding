def solution(s):

    arr = s.split(" ")

    arr.sort()
    temp = 0
    count = 0

    while count < 8000:
        for i in range(len(arr)-1):
            if int(arr[i]) > int(arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            elif int(arr[i]) < int(arr[i+1]):
                pass
            count += 1

    answer = str(arr[0]) + " " + str(arr[-1])

    return answer
def f(i, N, v):    # v: 찾고자 하는 값
    if i == N:    # 끝까지 찾았는데 없으면 0을 반환
        return 0
    elif arr[i] == v:    # 찾으면 1을 반환
        return 1
    else:
        return f(i+1, N, v)    # 다음 요소에 대해서 또 함수 진행

arr = [1, 2, 3, 4]
print(f(0, 4, 3))    # 1
print(f(0, 4, 5))    # 0
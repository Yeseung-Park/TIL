arr = [3, 6, 7, 1, 5, 4]

n = len(arr)
subset_list =[]
# << 비트 연산자는 왼쪽으로 쉬프트 한다는 것으로 왼쪽으로 쉬프트 할 경우 2배가 된다.
for i in range(1<<n):    # 1<<n = 2의 n제곱 (1을 왼쪽으로 n만큼 쉬프트)
    subset=[]
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    subset_list.append(subset)

print(subset_list)

            
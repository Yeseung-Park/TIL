def select(list, k):
    
    for i in range(0, k):    # 범위가 k까지인 이유는 k번째로 작은 원소만 찾으면 되기 때문
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[min_index], list[i] = list[i], list[min_index]
    
    return list[k-1]

list = [10, 25, 64, 22, 11]
print(select(list, 4))    # 25
            
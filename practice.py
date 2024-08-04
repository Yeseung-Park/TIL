arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for i in range (0, len(arr)):
    if i%2 == 0:
        for j in range(0, len(arr[0])):
            print(arr[i][j], end = "")
    else:
        for j in range(len(arr[0])-1, -1, -1):
            print(arr[i][j], end = "")
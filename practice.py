def strlen(str):
    idx = 0
    count = 0
    while str[idx] != '\0':
        idx += 1
        count += 1
    return count

a = ['a', 'b', 'c', '\0']

print(strlen(a))
def f(t, p):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    count = 0

    while i < N and j < M:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i-j+1
            j = 0
    if j == M:
        count += 1
    else:
        return -1
    return count

t = 'TTTTABCATTABCDE'
p = 'TTA'

print(f(t, p))
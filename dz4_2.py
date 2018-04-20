def premin(*numbers):
    l=list(numbers)
    l.sort()
    i = 0
    while True:
        if l[0] == l[i]:
            i = i + 1
        else:
            return l[i]
print(premin(1,1,3, 8, 3, 5, 6, 7, 6, 6))
def premin(*num):
    l=list(num)
    l.sort()
    i = 0
    while True:
        if l[0] == l[i]:
            i = i + 1
        else:
            return l[i]
print(premin(1,1,5,5,3,3,8,8,2,2,7,7,6,6,10,10))
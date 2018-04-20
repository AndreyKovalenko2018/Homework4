st = int(input('Количество строк: '))
kvo = int(input('К-во "la": '))
en = int(input('Окончание: '))
def song(st=3, kvo=3, en=0):
    while True:
        if en == 1:
            return (st*('\n'+'la'+'-la'*(kvo-1)))+'!'
        elif en == 0:
            return (st*('\n'+'la'+'-la'*(kvo-1)))+'.'
print(song(st,kvo,en))
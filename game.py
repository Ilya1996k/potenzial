A= [ ['_']*3 for i in range(3)]
def pt():
    print(' ',0,1,2)
    for i in range(3):
        print(i,*A[i])
def g1():
    if A[0][0] == A[0][1] == A[0][2] =='X' or \
        A[1][0] == A[1][1] == A[1][2] == 'X' or \
        A[2][0] == A[2][1] == A[2][2] == 'X' or \
        A[0][0] == A[1][0] == A[2][0] =='X' or \
        A[0][1] == A[1][1] == A[2][1] == 'X' or \
        A[0][2] == A[1][2] == A[2][2] == 'X' or \
        A[0][0] == A[1][1] == A[2][2] =='X' or \
        A[2][0] == A[1][1] == A[0][2] == 'X':
        return True
    else:
        return False

def g2():
    if A[0][0] == A[0][1] == A[0][2] =='O' or \
        A[1][0] == A[1][1] == A[1][2] == 'O' or \
        A[2][0] == A[2][1] == A[2][2] == 'O' or \
        A[0][0] == A[1][0] == A[2][0] =='O' or \
        A[0][1] == A[1][1] == A[2][1] == 'O' or \
        A[0][2] == A[1][2] == A[2][2] == 'O' or \
        A[0][0] == A[1][1] == A[2][2] =='O' or \
        A[2][0] == A[1][1] == A[0][2] == 'O':
        return True
    else:
        return False
k=0
p=1
pt()
while True:
    if k == 9:
        print('Никто не выиграл')
        break
    if p ==1:
        i,j = map(int,input('Игрок 1: ').split())
        if A[i][j] != '_':
            print('Клетка уже занята, выберите другую клетку')
            continue
        A[i][j] = 'X'
        k+=1
        pt()
        if g1() == True:
            print('Выиграл Игрок 1')
            break
        p = 2
        continue
    if p == 2:
        i, j = map(int, input('Игрок 2: ').split())
        if A[i][j] != '_':
            print('Клетка уже занята, выберите другую клетку')
            continue
        A[i][j] = 'O'
        k+=1
        pt()
        if g2() == True:
            print('Выиграл Игрок 2')
            break
        p = 1



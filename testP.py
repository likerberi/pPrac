count = int(input())
for i in range(count):
    for j in range(count):
        if( i + j >= count - 1):
            print('*', end='')
        else:
            print(' ', end='')
    for k in range(count - 1):
        if( k < i ):
            print('*', end='')
        else:
            print(' ', end='')
    print()
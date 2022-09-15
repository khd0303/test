number = int(input('숫자를 입력하세요 : '))

for i in range(1,number):
    print(' ' * (number-i), '*' * i,end = ' ')
    for j in range(1):
        print(' ')

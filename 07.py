
num = int(input('1부터 9까지의 값을 입력하세요 : '))
while num not in range(1,10):
    num = int(input('1부터 9까지의 값을 다시 입력하세요 : '))

for i in range(1,10):
        print(num, ' * ', i, ' = ', num*i)

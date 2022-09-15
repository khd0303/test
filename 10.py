num = int(input('num을 입력하시오 : '))

for i in range(num):
    print(' ')
    for j in range(num):
        if(i % 2 == 1):
            k = num - j
            print(str(k + num * i),end = " ")
        else:
            print(str(j + num * i +1),end = ' ')

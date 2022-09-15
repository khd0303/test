number = int(input('숫자를 입력하세요 >> '))


for i in range(2,number):
    if number % i == 0:
        print(number,'는 소수가 아닙니다')
        break
    else:
        print(number,'는 소수입니다')
        break
'''if number == 2:
    print(number,'는 소수입니다')
elif number % 2 == 0:
    print(number,'는 소수가 아닙니다')
else:
    for i in range (3,number,2):
        if number % i == 0:
            print(number,'는 소수가 아닙니다')
            break
        else:
            continue
        print(number,'는 소수 입니다')

'''

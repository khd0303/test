'''
#1

point = int(input('게임점수를 입력하시오 : '))

print('game_score  = ',point)

if point > 1000:
    print('고수입니다')
else:
    print('입문자입니다')



#2

num1 = int(input('한 정수를 입력하세요 : '))
num2 = int(input('다른 정수를 입력하세요 : '))

if num1 == num2:
    print('두값이 일치합니다')
else:
    print('두값이 일치하지 않습니다')

#3.1
num  = int(input('성인인가요(성인이면 1, 미성년이면 0) : '))
if num == 0:
    print('당신은 미성년자입니다')
elif num == 1:
    print('당신은 성인입니다')

'''
#3.2
num1  = int(input('성인인가요(성인이면 1, 미성년이면 0) : '))
num2 = int(input('결혼했나요(기혼이면 1, 미혼이면 0) : '))

if num1 == 1:
    if num2 == 1:
        print('당신은 결혼한 성인입니다')
    elif num2 == 0:
        print('당신ㅇ느 미혼인 성인입니다')
print('맛나 식당에 오신것을 환영합니다. 메뉴는 다음과 같습니다')
print('삼겹구이 입력 s')
print('오삼불고기 입력 o')
print('된장찌개 입력 d')

put = input('메뉴를 선택하세요(알파벳 s,o,d 입력) : ')
while put not in list('sod'):
    put = input('메뉴를 다시 입력하세요 ')
if put == 's':
    print('삼겹구이를 선택하셨습니다')
elif put == 'o':
    print('오삼불고기를 선택하셨습니다')
elif put == 'd':
    print('된장찌개를 선택하셨습니다')

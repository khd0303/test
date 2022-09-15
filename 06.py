a = 0
b = 0
c = 0
print('세자리의 암스트롱 수 :', end = ' ')
for i in range(100,1000):
    a = i // 100
    b = (i - (a * 100))//10
    c = i % 10
    if (a ** 3 + b ** 3 + c ** 3) == i:
        print(i,end = ' ')

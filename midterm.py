for celcius in range(0,51,5):
    farenheight = celcius * 9 / 5 + 32

    print('화씨 : ',farenheight, '섭씨 : ',celcius)

a = 2 * 2 // 2  # a = 4 // 2 - > 2
b = 3 // 2 * 3 # b = 1 * 3 -> 3
print(a,b)

sum = 0
for i in range(1,1000):
    if i %3 == 0:
        sum += i
    elif i %5 == 0:
        sum += i
    elif i % 15 == 0:
        sum -= i

print(sum)

# scores = ['張三', 67, 86, 95]

# print(
#     f'學生: {scores[0]}\n國文成績: {scores[1]}分\n數學成績: {scores[2]}分\n英文成績: {scores[3]}分')

#
sum = 0
num = int(input('請輸入一個正整數: '))
r1 = range(1, num+1)

for i in r1:
    sum += i
print(f'1到{num}的總和是: {sum}')

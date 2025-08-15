# # 練習題_輸入溫度 轉換器

# C = input("請輸入攝氏溫度°C:")
# print(f"華氏溫度為{float(C)*9/5+32:.1f}°F")

# # -------------------------------------------------------

# # 變數

# patient_name = "Jhon Smith"
# patient_age = 20
# new_patient = True

# # -------------------------------------------------------

# # 練習題_回答名字和顏色

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(f"Hi! {name}. your favorite color is {color}, It's cool!")

# # -------------------------------------------------------

# # 練習題_體重轉換kg to lbs

# kg = input("Please type your weight(kg): ")
# print(f"your weight is {float(kg)*2.2:.1f}lbs.")

# # -------------------------------------------------------

# # String Methods

# course = 'Python for Beginners'
# print(type(course))
# print(len(course))
# print(course[0:6])
# print(course.find('B'))
# print(course.upper())
# print(course.lower())
# print(course.replace('Python', 'Java Script'))
# print(course.title())
# print('Python' in course)

# # -------------------------------------------------------

# # if 用法1

# is_hot = False
# if is_hot:
#     print("It's a hot day.")
#     print('Drink plenty of water!')
# else:
#     print("It's a cold day.")
#     print('Wear warm clothes!')
# print('Enjoy your day')

# # -------------------------------------------------------

# # if 用法2

# is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day.")
#     print('Drink plenty of water!')
# elif is_cold:
#     print("It's a cold day.")
#     print('Wear warm clothes!')
# else:
#     print("It's a lovely day.")
# print('Enjoy your day')

# # -------------------------------------------------------

# # if 練習題

# has_good_credit = True
# house_price = 1000000

# if has_good_credit:
#     down_payment = 0.1*house_price
# else:
#     down_payment = 0.2*house_price
# print(f'you have to pay a ${down_payment:.0f} down payment.')
# print('god bless you')

# # -------------------------------------------------------

# # if 邏輯

# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print("Eligable for loan")
# else:
#     print("go to hell")

# # -------------------------------------------------------

# # if 練習題 2

# name = input("輸入你的遊戲ID: ")
# if len(name) < 3:
#     print("名字至少要大於3個字")
# elif len(name) >= 10:
#     print("名字最多只能10個字")
# else:
#     print("不錯的ID!")

# # -------------------------------------------------------

# 計算平均成績

c = input("輸入國文成績: ")
m = input("輸入數學成績: ")
e = input("輸入英文成績: ")

print(f"你的平均為: {(int(c)+int(m)+int(e))/3:.1f}")

# # -------------------------------------------------------

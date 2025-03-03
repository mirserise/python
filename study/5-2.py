과자 = {
    "꼬깔꼰" : 1000,
    "빈츠" : 1200,
    "새우깡" : 1500,
    "오감자" : 1000,
    "콘칲" : 1300

}

for i in 과자:
    print(i, 과자[i])

for k, v in 과자.items():
    print(k, v)

for i in range(10):
    print(i)

for k, v in enumerate(과자):
    print(k, v)

for i in range(1, 4):
    print("파이썬" + str(i))

for i, k in enumerate(과자):
    print("정가:", 과자[k], "할인가:", 과자[k] * 0.9)

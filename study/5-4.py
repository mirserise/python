과자 = {
    "꼬깔꼰" : 800,
    "빈츠" : 600,
    "새우깡" : 500,
    "오감자" : 700,
    "자갈치" : 600,
    "콘치즈" : 800,
    "꽃게랑" : 1000,
    "오징어집" : 700,
    "쌀과자" : 800,
    "양파링" : 1000

}

tmp = 0

for k, v in 과자.items():
    tmp += v
    if tmp > 5000:
        break
    print(k, v)

print(tmp, " 이하로 구매 가능합니다. ")

for i in range(4):
    if i % 2 == 0:
        continue
    print(i)

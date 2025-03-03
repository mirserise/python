comp = [
    ["삼성전자", 15.79],
    ["현대차", 8.70],
    ["LG전자", 317.34],
    ["NAVER", 9.76]

]

result = []

for i in comp:
    name = i[0]
    per = i[1]
    if per < 10:
        result.append([name, per])

print(result)


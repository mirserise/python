class 붕어빵:
    def 앙꼬넣기(self, 앙꼬):
        self.내용물 = 앙꼬

붕어빵1 = 붕어빵()
붕어빵2 = 붕어빵()

붕어빵1.앙꼬넣기("딸기")
붕어빵2.앙꼬넣기("크림")

print(붕어빵1.내용물)
print(붕어빵2.내용물)


class 계좌: 
    def 개설(self, 이름, 잔고):
        self.이름 = 이름
        self.잔고 = 잔고
    def 출력(self):
        print("이름: ", self.이름)
        print("잔고: ", self.잔고)

계좌1 = 계좌()
계좌2 = 계좌()

계좌1.개설("김철수", 500)
계좌2.개설("이영희", 1000)


계좌1.출력()
계좌2.출력()




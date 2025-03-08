class 사람:
    def __init__(self, 이름, 생년월일, 성별):
        self.이름 = 이름
        self.생년월일 = 생년월일
        self.성별 = 성별

    def 정보출력(self):
        print("이름: ", self.이름)
        print("생년월일: ", self.생년월일)
        print("성별: ", self.성별)
    
나 = 사람("김철수", "19821218", "남자")
나.정보출력()

class 비행기:
    def __init__(self, 비행기종류):
        self.비행기종류 = 비행기종류

    def 이륙(self):
        print(self.비행기종류, "이륙합니다.")

비행기1 = 비행기("보잉787")
비행기1.이륙()

비행기2 = 비행기("에어버스A330")
비행기2.이륙()

class 계좌:
    def __init__(self, 이름, 잔고):
        self.이름 = 이름
        self.잔고 = 잔고

    def 출력(self):
        print("이름: ", self.이름)
        print("잔고: ", self.잔고)

백창범계좌 = 계좌("백창범", 1000000)
백창범계좌.출력()

        
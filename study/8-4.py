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

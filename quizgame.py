class QuizGame:
    def __init__(self):

        # 최고 점수
        self.quiz_list = None

        # 최고 점수를 저장함
        self.highest_score:int = 0

    
    
    # 원하는 메뉴를 선택하는 기능
    def menu_select(self):
        while True:
            select = input("원하시는 번호를 입력해 주세요.")
            if isinstance(select,int):
                select = int(select)
                if 1<= select <=5:
                    return select
                else:
                    print("1부터 5까지의 숫자중에서 입력해주세요.")
            else:
                print("잘못 입력하셨습니다.")
            self.menu_print()

    def menu(self):
        select = self.menu_print()
        match select:
            case 1:
                print("퀴즈 풀기를 선택하셨습니다.")
                self.quiz_solve()
            case 2:
                print("퀴즈 등록을 시작합니다..")
                self.quiz.quiz_regist()
            case 3:
                print("퀴즈 목록 출력합니다..")
                self.quiz_list_show()
            case 4:
                print("점수를 출력합니다..")
                highest_score_show()
            case 5:
                print("종료를 선택하셨습니다.")
                # 종료 하는 함수 임시로 이렇게 함
                exit -1

            # 어떻게 처리할까?
            case _:
                self.menu()
            
        # (선택지 1 : 퀴즈 풀기 /  퀴즈 등록 / 퀴즈 목록 / 점수 확인 / 종료)
    def menu_print(self):
        print("-----1. 퀴즈 풀기-----")
        print("-----2. 퀴즈 등록-----")
        print("-----3. 퀴즈 목록-----")
        print("-----4. 점수 확인-----")
        print("-----5. 종    료-----")
from quiz import Quiz
import random
import os
import json
import data_handle
from custom_input import s_input,int_input
class QuizGame:
    def __init__(self):
        self.quiz_list:list[Quiz] = []
        self.highest_score:int = 0

        self.data = {}

        # json에 있는 데이터를 불러온다.
        self.data:dict|None = data_handle.read_json_data()
        self.unpack_data()

        # 데이터를 불러오지 못했거나 오류로 실패헀을때 예비 문제를 반환함
        self.load_backup_quiz()
        
        # 종료(메뉴5번)를 선택했을때 True를 반환함
        self.is_exit_key:bool = False

    

        # Quiz클래스를 Json파일에 넣을때 에러가 나오므로 기본 클래스인 딕셔너리로 변환한다.
    def update_data(self):
        quiz_parsing = []
        if self.quiz_list == [] or self.quiz_list == None:
            print("self.quiz_list가 없습니다.")
            return
        for quiz in self.quiz_list:
            quiz_parsing.append(quiz.to_dict())
            
        self.data = {"quizzes":quiz_parsing,"best_score":self.highest_score}

    def load_backup_quiz(self):
        if self.quiz_list == []:
            sampleQuiz1 = Quiz("저의 이름은?",["김호재","휴즈","효성","삼성"],1)
            sampleQuiz2 = Quiz("코디세이의 인근역의 이름은?",["삼성역","개포동역","대모산입구역","수서역"],2)
            sampleQuiz3 = Quiz("코디세이 AI 올일원 2기 오리엔테이션을 진행한 날은?",["260727","260627","260617","260330"],1)
            sampleQuiz4 = Quiz("코디세이 서울 교육장의 캐빈5가 위치한 층은?",["2층","3층","4층","5층"],4)
            sampleQuiz5 = Quiz("코디세이가 제공하는 AI 이름은?",["제미나이","X AI","클로드","네이토"],4)

            self.quiz_list =[sampleQuiz1,sampleQuiz2,sampleQuiz3,sampleQuiz4,sampleQuiz5]

            self.update_data()

            data_handle.save_json_data(data=self.data)

    # quiz는 json형식으로 넣을수 없어서 dict로 변환함
    def updating_quiz(self):
        quiz_parsing = []
        for quiz in self.quiz_list:
            quiz_parsing.append(quiz.to_dict())
        self.data["quizzes"] = quiz_parsing


    def unpack_data(self):
        if self.data == None:
            print("data가 비었습니다.")
            return
        self.quiz_list = []
        for di in self.data["quizzes"]:
            unpacking_quiz = Quiz(di["question"],di["choices"],di["answer"])
            self.quiz_list.append(unpacking_quiz)
        self.highest_score = self.data["best_score"]

    def printing_data(self):
        print(self.data)

    # 무작위의 퀴즈 번호를 인덱스로 전달한다.
    def random_quiz_getter(self,random_quiz_list:list[Quiz])->int:
        if len(random_quiz_list) == 1:
            return 0
        # 0부터 최대 크기의 인덱스 (len(random_quiz_list)- 1) 중에 int 값을 반환합니다. 
        return random.randint(0,len(random_quiz_list)-1)

    # 메뉴1 문제를 풉니다.
    def quiz_solve(self):
        # 게임내 점수를 기록함
        self.score = 0

        # 퀴즈 없으면 복귀한다.
        if self.quiz_list ==0:
            print("퀴즈가 하나도 없습니다. 새로운 퀴즈를 등록해주세요.")
            return
        
        unsolved_quiz_list = self.quiz_list.copy()

        while len(unsolved_quiz_list) > 0:
            random_quiz_index = self.random_quiz_getter(unsolved_quiz_list)

            random_quiz = unsolved_quiz_list.pop(random_quiz_index)
            
            random_quiz.printQuestion()

            select = int_input("정답(숫자)을 입력해주세요.",1,4,random_quiz.printQuestion)

            # select = self.answer_select(random_quiz)
            if select == random_quiz.answer:
                print("정답입니다.~~~~")
                self.score += 20
                print(f"현재 점수는 {self.score}입니다.")
                print("\n")
            else:
                print("틀렸습니다.")
                print(f"정답은 {random_quiz.answer}입니다.","\n")

        print(f"최종 점수는 {self.score}입니다.")
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            print("새로운 기록을 경신하셨습니다!!")
            self.data["best_score"] = self.score
            data_handle.save_json_data(data=self.data)


    # 메뉴2 문제를 등록합니다.
    def quiz_regist(self):
        new_quiz = None
        question= s_input("문제를 입력해주세요: >")
        if question[-1] == "." :
            question = question[:-1] + "?"
        elif question[-1] != "?":
            question = question + "?"

        choices1 = s_input("선택지 1번 : >")
        choices2 = s_input("선택지 2번 : >")
        choices3 = s_input("선택지 3번 : >")
        choices4 = s_input("선택지 4번 : >")

        answer = int_input("정답을 입력해주세요 : >",1,4)
        new_quiz = Quiz(question=question,choices=[choices1,choices2,choices3,choices4],answer=answer)

        self.quiz_list.append(new_quiz)
        self.data["quizzes"] = self.quiz_list
        self.updating_quiz()
        data_handle.save_json_data(data=self.data)


    # 메뉴3 문제의 리스트를 봅니다.
    def quiz_list_show(self):

        if len(self.quiz_list) == 0:
            print("아직 문제가 등록 되지 않았습니다.")
            
        else:

            for i,li in enumerate(self.quiz_list):
            
                print(f"{i+1}번 문제 > {li.question_getter()}")
            print("\n")


    # 메뉴4 가장 높은 점수를 확인합니다.
    def highest_score_show(self):
        print("-----------------------------")
        print(f"{self.highest_score}점 입니다.")
        print("-----------------------------")

    # 원하는 정답을 선택하는 기능
    def answer_select(self,quiz:Quiz):
        return int_input("정답(숫자)을 입력해주세요.",1,4,quiz.printQuestion)
    
            

        # (선택지 1 : 퀴즈 풀기 /  퀴즈 등록 / 퀴즈 목록 / 점수 확인 / 종료)
    def menu_print(self):
        print("-----1. 퀴즈 풀기-----")
        print("-----2. 퀴즈 등록-----")
        print("-----3. 퀴즈 목록-----")
        print("-----4. 점수 확인-----")
        print("-----5. 종    료-----")
        print()

    def menu(self):
        self.menu_print()

        select = int_input("원하시는 번호를 입력해 주세요.",1,5,self.menu_print)

        match select:
            case 1:
                print("퀴즈 풀기를 선택하셨습니다.")
                self.quiz_solve()
            case 2:
                print("퀴즈 등록을 시작합니다..")
                self.quiz_regist()
            case 3:
                print("퀴즈 목록 출력합니다..")
                self.quiz_list_show()
            case 4:
                print("가장 높은 점수를 출력합니다..")
                self.highest_score_show()
            case 5:
                print("종료를 선택하셨습니다.")
                # 메인파일(main.py)에 종료한다는 신호를 보내준다.
                self.is_exit_key = True

            # 어떻게 처리할까?
            case _:
                self.menu()
            

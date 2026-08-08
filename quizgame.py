from quiz import Quiz
import random
import os
import json

folder = os.path.dirname(__file__)
file = os.path.join(os.path.dirname(__file__),"state.json")

def read_json_data():
    if not os.path.exists(file):
        print("state.json 파일이 없습니다.")
        return None
    try:
        with open(file,'rt',encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        print("파일을 찾지 못했습니다. ",e)
    except PermissionError as e:
        print("권한이 없습니다. ",e)
    except json.JSONDecodeError as e:
        print("JSON 파일 포맷이 아닙니다.")
    except Exception as e:
        print("오류가 발생했습니다. " ,e)

def save_json_data(data:dict):
    try:
        with open(file,'wt',encoding="UTF-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    except PermissionError as e:
        print("파일 저장 권한이 없습니다. ",e)
    except TypeError as e:
        print(f"JSON 포맷이 손상되었습니다. ", e)
    except Exception as e:
        print("오류가 발생했습니다. ", e)

class QuizGame:
    def __init__(self):

        self.quiz_list:list[Quiz] = []
        self.highest_score:int = 0

        self.data = {}

        # json에 있는 데이터를 불러온다.
        self.data = read_json_data()
        self.unpack_data()

        
        # 종료(메뉴5번)를 선택했을때 True를 반환함
        self.is_exit_key:bool = False

        if self.quiz_list == None:
            sampleQuiz1 = Quiz("저의 이름은?",["김호재","휴즈","효성","삼성"],1)
            sampleQuiz2 = Quiz("코디세이의 인근역의 이름은?",["삼성역","개포동역","대모산입구역","수서역"],2)
            sampleQuiz3 = Quiz("코디세이 AI 올일원 2기 오리엔테이션을 진행한 날은?",["260727","260627","260617","260330"],1)
            sampleQuiz4 = Quiz("코디세이 서울 교육장의 캐빈5가 위치한 층은?",["2층","3층","4층","5층"],4)
            sampleQuiz5 = Quiz("코디세이가 제공하는 AI 이름은?",["제미나이","X AI","클로드","네이토"],4)

            self.quiz_list =[sampleQuiz1,sampleQuiz2,sampleQuiz3,sampleQuiz4,sampleQuiz5]
        self.update_data()
        if self.data != None:
            print(self.data)
        
    def update_data(self):
        quiz_parsing = []
        for quiz in self.quiz_list:
            quiz_parsing.append(quiz.to_dict())
            
        self.data = {"quiz_list":quiz_parsing,"highest_score":self.highest_score}

    def unpack_data(self):
        if self.data == None:
            return
        self.quiz_list = []
        quiz_list = self.data["quiz_list"]
        for di in quiz_list:
            unpacking_quiz = Quiz(di["question"],di["option"],di["answer_number"])
            self.quiz_list.append(unpacking_quiz)

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

        unsolved_quiz_list = self.quiz_list.copy()

        while len(unsolved_quiz_list) > 0:
            random_quiz_index = self.random_quiz_getter(unsolved_quiz_list)

            random_quiz = unsolved_quiz_list.pop(random_quiz_index)
            
            # random_quiz = unsolved_quiz_list[random_quiz_index]
            # unsolved_quiz_list.pop(random_quiz_index)
            
            random_quiz.printQuestion()
            select = self.answer_select(random_quiz)
            if select == random_quiz.answer_number:
                print("정답입니다.~~~~")
                self.score += 20
                print(f"현재 점수는 {self.score}입니다.")
                print("\n\n")
            else:
                print("틀렸습니다.")
                print(f"정답은 {random_quiz.answer_number}입니다.")
                print("\n\n")

        print(f"최종 점수는 {self.score}입니다.")
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            print("새로운 기록을 경신하셨습니다!!")
            self.update_data()
            
    # 메뉴2 문제를 등록합니다.
    def quiz_regist(self):
        new_quiz = None
        question= s_input("문제를 입력해주세요: >")
        if question[-1] == "." :
            question = question[:-1] + "?"
        elif question[-1] != "?":
            question = question + "?"

        option1 = s_input("선택지 1번 : >")
        option2 = s_input("선택지 2번 : >")
        option3 = s_input("선택지 3번 : >")
        option4 = s_input("선택지 4번 : >")

        answer = int_input("정답을 입력해주세요 : >",1,4)

        new_quiz = Quiz(question=question,option=[option1,option2,option3,option4],answer_number=answer)

        self.quiz_list.append(new_quiz)
        self.update_data()


    # 메뉴3 문제의 리스트를 봅니다.
    def quiz_list_show(self):
        if len(self.quiz_list) == 0:
            print("아직 문제가 등록 되지 않았습니다.")
        for i,li in enumerate(self.quiz_list):
            print(f"{i+1}번 문제 > {li.question_getter()}")
        print("\n")


    # 메뉴4 가장 높은 점수를 확인합니다.
    def highest_score_show(self):
        ...

    # 원하는 정답을 선택하는 기능
    def answer_select(self,quiz:Quiz):
        while True:

            try:
                select = input("정답(숫자)을 입력해주세요.").strip()
            except KeyboardInterrupt:
                print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
                print()
                exit(-1)
            except EOFError:
                print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
                print()
                exit(-1)
            if select != "" or select is None:
                if select.isdigit():
                    select = int(select)
                    if 1 <= select <= 4:
                        return int(select)
                    else:
                        print("1 2 3 4 중에 골라주세요.")

                else:
                    print("숫자를 입력해 주세요. (1 ~ 4)")
            else:
                print("'공백'을 입력 받았습니다.")

            quiz.printQuestion()
            

    # 원하는 메뉴를 선택하는 기능
    def menu_select(self):
        is_valid_input = False
        while not is_valid_input:
            try:
                select = input("원하시는 번호를 입력해 주세요.").strip()
            except KeyboardInterrupt:
                print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
                exit(-1)
            except EOFError:
                print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
                exit(-1)
            print()
                #공백
            if select == "" or select is None:
                print("아무 입력도 받지 못했습니다.")

                #공백이 아닐때
            else:
                if select.isdigit():
                    select = int(select)
                    if 1<= select <=5:
                        return select
                    else:
                        print("1부터 5까지의 숫자중에서 입력해주세요.")
                else:
                    print("숫자를 입력해주세요.")
            
            self.menu_print()

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
        select = self.menu_select()
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
                save_json_data(data=self.data)
                # 메인파일(main.py)에 종료한다는 신호를 보내준다.
                self.is_exit_key = True

            # 어떻게 처리할까?
            # case _:
            #     self.menu()
            
def s_input(inquiry:str)->str:
    while True:
        try:
            select = input(inquiry).strip()
        except KeyboardInterrupt:
            print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
            exit(-1)
        except EOFError:
            print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
            exit(-1)
        if select == "" or select == None:
            print("아무 입력도 받지 못했습니다.")
        else:
            return select
        
def int_input(inquiry:str,lower:int,upper:int)->int:
    while True:
        try:
            select = input(inquiry).strip()
        except KeyboardInterrupt:
            print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
            print()
            exit(-1)
        except EOFError:
            print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
            print()
            exit(-1)
        if select == "" or select == None:
            print("아무 입력도 받지 못했습니다.")
        else:
            if select.isdigit():
                select = int(select)
                if lower <= select <= upper:
                    return select
                else:
                    print(f"{lower}  ~ {upper} 사이로 입력해주세요.")
            else:
                print("숫자를 입력해주세요.")

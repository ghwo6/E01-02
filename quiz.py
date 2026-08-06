class Quiz:

    def __init__(self,question:str,option:list,answer_number:int):
        self.question = question
        self.option = option
        self.answer_number = answer_number

    def printQuestion(self):
        print(self.question)
        for i,li in enumerate(self.option):
            print(f"{i}).   {li}")
        print("정답(숫자)을 입력해주세요.")

    def print_answer(self):
        print(f"정답은 {self.answer_number}번 입니다!")
        print(self.option[self.answer_number-1])

    def answer_getter(self)-> int:
        return self.answer_number
    def question_getter(self)->str:
        return self.question
        
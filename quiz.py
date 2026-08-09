class Quiz:

    def __init__(self,question:str,choices:list,answer:int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def printQuestion(self):
        print(self.question)
        for i,li in enumerate(self.choices):
            print(f"{i+1}).   {li}")

    def print_answer(self):
        print(f"정답은 {self.answer}번 입니다!")
        print(self.choices[self.answer-1])
        print("\n\n")

    def question_getter(self)->str:
        return self.question
    
    def to_dict(self)->dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }
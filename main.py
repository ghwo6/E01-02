
from quizgame import QuizGame

if __name__ == "__main__":
    try:
        quizgame = QuizGame()
        print()
        while not quizgame.is_exit_key:
            quizgame.menu()
    except KeyboardInterrupt:
        print("\n","(Ctrl + C) 를 입력 받았습니다.","\n")
        exit(-1)
    except EOFError:
        print("\n","(Ctrl + D)를 입력 받았습니다.","\n")
        exit(-1)

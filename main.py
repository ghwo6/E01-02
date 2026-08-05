
from quizgame import QuizGame

if __name__ == "__main__":
    quizgame = QuizGame()
    while not quizgame.is_exit_key:
        try:
            quizgame.menu()
        except KeyboardInterrupt:
            print("\n","ctrl + c를 인식했습니다.")
            exit(-1)

            


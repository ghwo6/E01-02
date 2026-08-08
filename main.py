
from quizgame import QuizGame

if __name__ == "__main__":
    quizgame = QuizGame()
    while not quizgame.is_exit_key:
        quizgame.menu()

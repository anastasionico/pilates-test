from question_processor import Question_processor
from question_loader import Question_loader


if __name__ == '__main__':
  difficulty: int = int(input("Choose the difficulty of the questions: \n 1 - Easy \n 2 - Medium \n 3 - Difficult \n 0 - Mixed "))

  ql = Question_loader()
  questions: dict = ql.get_questions(difficulty)


  qp = Question_processor()

  qp.main(questions)

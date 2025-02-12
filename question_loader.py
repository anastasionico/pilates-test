import json 


class Question_loader():
  def get_questions(self, difficulty: int) -> list:
    values: list = [] 

    with open("questions.json") as file:
      questions = json.load(file)
     
      for question in questions["questions"]:
        if question["difficulty"] == difficulty or difficulty == 0:
          values.append(question)
    return values

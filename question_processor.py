import json
import random

class Question_processor:
  def __init__(self):
    pass


  def main(self):
    point = 0
    
    with open("questions.json") as file:
      questions = json.load(file)

      for question in questions["questions"]:      
        print("__________________________")
        print(f"{question['question']}\n")
        print(f"\nhint:{question['hint']}\n")   
      
        correct_answer = self.show_options(question)
    
        answer = self.get_answer()

        point = self.process_answer(question = question, answer = answer, point = point, correct_answer = correct_answer)


  def show_options(self, question: dict) -> int:
    options: list = self.randomize_options(question)
    correct: int = 1
    
    for idx, option in enumerate(options, start = 1):
      if option == "correct":
        correct = idx
      
      print(f" {question['options'][option]}")

    #found_correct: bool = False
    
    #for option in options:
      
     # if option == "correct":
       # found_correct = True
      #elif option != "correct" and found_correct is False:
       # correct += 1
      
      #print(f" {question['options'][option]}")

    return correct

   
  def randomize_options(self, question: dict) -> dict:
    values: list = question["options"].values()
    keys: list = question["options"].keys()
    temp = list(zip(values, keys))

    random.shuffle(temp)
    v, k = zip(*temp)

    options = dict(zip(k,v))
    
    return options


  def get_answer(self) -> int:
    print("\n1,2,3 to answer")
    
    return int(input("insert your answer\n"))


  def process_answer(self, question: dict, answer: int, point: int, correct_answer: int) -> int:
    if answer != correct_answer:
      print("wrong\n")
      print(f"explanation: {question['explanation']}\n")
    
    elif answer == correct_answer:        
      print("correct\n")
      point += 1;
      print(f"current point: {point}\n")
    
    return point

if __name__ == "__main__":
  qp = Question_processor()
  qp.main()

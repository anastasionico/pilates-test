import json
import random

def main():

  point = 0
  
  with open("questions.json") as file:
    questions = json.load(file)

    for question in questions["questions"]:      
      print("__________________________")
      print(f"{question['question']}\n")
      print(f"\nhint:{question['hint']}\n")   
    
      correct_answer = show_options(question)
  
      answer = get_answer()

      point = process_answer(question = question, answer = answer, point = point, correct_answer = correct_answer)


def show_options(question: dict) -> int:
  options: list = randomize_options(question)
  correct: int = 1
  found_correct: bool = False
  
  for option in options:
    
    if option == "correct":
      found_correct = True
    elif option != "correct" and found_correct is False:
      correct += 1
    
    print(f" {question['options'][option]}")

  return correct

 
def randomize_options(question: dict) -> dict:
  values: list = question["options"].values()
  keys: list = question["options"].keys()
  temp = list(zip(values, keys))

  random.shuffle(temp)
  v, k = zip(*temp)

  options = dict(zip(k,v))
  
  return options


def get_answer() -> int:
  print("\n1,2,3 to answer - 0 to see the current points")
  
  return int(input("insert your answer\n"))


def process_answer(question: dict, answer: int, point: int, correct_answer: int) -> int:
  if answer != correct_answer:
    print("wrong\n")
    print(f"explanation: {question['explanation']}\n")
  
  elif answer == correct_answer:        
    print("correct\n")
    point += 1;
    print(f"current point: {point}\n")
  
  return point


if __name__ == '__main__':
  main()

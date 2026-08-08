from quiz_data import question_data
logo=r'''
             _   
            (_)    
  __ _ _   _ _ ____
 / _` | | | | |_  /
| (_| | |_| | |/ / 
 \__, |\__,_|_/___|
    | |            
    |_| 
'''

print(logo)
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,answer,correct_answer):
        if correct_answer.lower() == answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
            print(f"The correct answer is {correct_answer}.")
        print(f"Score: {self.score} out of {self.question_number} questions.")

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()



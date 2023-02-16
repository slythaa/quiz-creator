print("Quiz maker made by Christian! Have fun!")
#basically kahoot but helped me understand dictionaries more in python

input("Press enter!")

creator = input("What is your name?: ")
quizDetails = input("What is the quiz details? (one word that describes the quiz you are going to make): ")
number = int(input("How many questions will this quiz have? (just put in a number): "))

quizQuestions = {}

#print(numOfQuestions)


def checkAnswer(): #checks if answer is in the dictionary
    if answer in quizQuestions.values():
        print("You got it right! ")
    else:
        print("You got it wrong...")


for n in range(number): #asks for a question the amount of time in the number variable

    inputQuestion = input("Enter a question: ")
    inputAnswer = input("Enter the answer to that question: ")
    questions = quizQuestions[inputQuestion] = inputAnswer
    #print(len(quizQuestions))

print(f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"\n"
      f"This quiz is made by {creator}, it is about {quizDetails}, and has {number} question/s.\n")

#keys = quizQuestions.keys()
#print(keys)

for n in quizQuestions:
    print(f"Question: {n}")
    answer = input("Enter answer here: ")
    checkAnswer()

print("Thanks for playing!")
    #I dont need to check one specific value in the dictionary,
    # I can just see if the answer is in the dictionary and say that it's correct!













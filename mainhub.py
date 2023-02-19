import json



#SELECT SCREEN

global quizName

def mainHub():
    print("Hello, what do you want to do today?\n"
          "(1) Create a quiz \n"
          "(2) Open a quiz \n"
          "(3) Quit \n")

    select = input("(Enter a number): ")

    while True:

        if select == "1":
            createQuiz()
            break

        elif select == "2":
            openPlay()
            break

        elif select == "3":
            print("See you next time!")
            exit()
            break

        else:
            print("That's not a choice!\n"
                    "(1) Create a quiz then play it \n"
                    "(2) Open and play \n"
                    "(3) Quit \n")
            select = input("(Enter a number): ")




#CREATE A QUIZ (CHOICE #1)

def createQuiz():

    print("\n")

    quizName = input("Name of quiz?: ")

    data = {
        "quizName": quizName,
        "creator": input("What is your name?: "),
        "quizDetails": input("What are the quiz details?: "),
        "number": int(input("How many questions will this quiz have? (just put in a number): ")),
        "quizQuestions": {}
    }

    for n in range(data["number"]):
        inputQuestion = input("Enter a question: ")
        inputAnswer = input("Enter the answer to that question: ")
        data["quizQuestions"][inputQuestion] = inputAnswer

    with open(f'{quizName}.json', 'w') as f:
        json.dump(data, f)

    print("\n")

    print("Quiz created!")

    print("\n")


#OPEN AND PLAY (CHOICE #2)

def openPlay():

    print("\n")

    openQuiz = input("Enter quiz name: ")

    with open(f'{openQuiz}.json', 'r') as f:
        stuff = json.load(f)

    creator = stuff["creator"]
    quizQuestions = stuff["quizQuestions"]
    number = stuff["number"]
    quizDetails = stuff["quizDetails"]

    print("\n")

    print(f"This quiz is made by {creator}, it is about {quizDetails}, and has {number} question/s.")

    print("\n")

    def checkAnswer():  # checks if answer is in the dictionary

        if answer in quizQuestions.values():
            print("You got it right! ")

        else:
            print("You got it wrong...")

    for n in quizQuestions:
        print(f"Question: {n}")
        answer = input("Enter answer here: ")
        checkAnswer()

    #print(stuff["quizName"])

    print("\n")


#RETURN TO MAIN MENU LOOP

running = None

while running != "n":

    mainHub()
    running = input("Back to main menu?(y/n): ")


print("\n"
    "See you next time!")


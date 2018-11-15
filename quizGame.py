# Making a Quiz Game


import json
import random
#import os


def choice_fifty_fifty(question_dict, rightAnswer): # to deduct any two wrong answers. Parameters to receive question dictionary ani rightAnswer count    
    key_list = [] # to hold key of every option (answer)
    c_ans = question_dict['ca'] # correct answer
      
    for key in question_dict.keys():
        key_list.append(key) 
        if key == c_ans:
            correctAns = c_ans 
            
    key_list.pop(5) # to remove the last key ('ca') that is not needed 
    key_list.pop(0) # to remove the first key ('q') that is not needed    
         
    while True: # to generate a random option
        rand_wrong_choice = random.choice(key_list) # choose one of the wrong answer randomly
        
        if rand_wrong_choice == c_ans:
            continue
        else:
            break
    
    if ord(correctAns) < ord(rand_wrong_choice): # compare the ascii value of keys
        print("{}) {}\n{}) {}\n".format(correctAns, question_dict[correctAns], rand_wrong_choice, question_dict[rand_wrong_choice]))
        answer = input("\nEnter your answer here ({}/{}) : ".format(correctAns, rand_wrong_choice))
    else:
        print("{}) {}\n{}) {}\n".format(rand_wrong_choice, question_dict[rand_wrong_choice], correctAns, question_dict[correctAns]))
        answer = input("\nEnter your answer here ({}/{}) : ".format(rand_wrong_choice, correctAns))
    
    
    if question_dict['ca'] == answer:
        print("Correct answer.\t +10 points")
        print("------------------------------------------------------")
        rightAnswer += 1
                        
    else:
        print("\nYour answer is wrong.")
        print("Correct answer is '{correctAns}'.".format(correctAns = question_dict['ca']))
    
    return rightAnswer


with open("ques_ans.json", "r") as qa:
    questionSet = qa.read() # read json file
    questionList = json.loads(questionSet) # load content of file in list form
    rightAnswer = 0
    user_name = input("Enter your name")
    print("WELCOME {}, be ready for your questions\n".format(user_name))
    
    for i in range(len(questionList)): 
        question_dict = questionList[i] # access the first item of list (first question of quiz)
        
        print("\n{questionNo}.  {question}".format(questionNo = i+1, question = question_dict['q'])) # print question
        # print options
        print(" a) {}\n b) {}\n c) {}\n d) {}".format(question_dict['a'], question_dict['b'], question_dict['c'], question_dict['d']))
        print("\nLifelines: \n1) 50/50")
        
        answer = input("\nEnter your answer here (a/b/c/d) : ")
        
        if question_dict['ca'] == answer:
            print("Correct answer.\t +10 points")
            print("------------------------------------------------------")
            rightAnswer += 1
            
        elif answer == '1': # user asks for 50/50 lifeline
            rightAnswer = choice_fifty_fifty(question_dict, rightAnswer)
            
        else:
            print("\nYour answer is wrong.")
            print("Correct answer is '{correctAns}'.".format(correctAns = question_dict['ca']))
            print("------------------------------------------------------")
        #os.system('cls')
        
    else:
        print("\nGame Over")
        print("You made {} right. Your score is {} out of 100\n".format(rightAnswer, str(rightAnswer*10)))


with open("record.txt", "w") as f:
    f.write("Name = {}\t Score = {}\n".format(user_name, str(rightAnswer*10)))

choice = input("Do yo want us to show the dashboard? (y/n)")
if choice == 'y':
    with open("record.txt", "r") as f:
        print(f.read())
    

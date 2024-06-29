print("Welcome to the Maitery's Quiz Game.....")
# here we will ask to user that you want to play or not
playing = input("Do you want to play the Quiz Game---> ")
# now generating the conditions
if playing != 'yes':
    quit()

print("Okay, Let's play the Quiz the game :) ")
score = 0
# making the ques and its asnwer...
answer = input("1. What does the CPU Stand for? ")
if answer.lower() == "central processing unit":
    print("Yep, Your Answer is Correct")
    score += 1

else:
    print("Opps, Your answer is Wrong!")

answer = input("2. What does RAM Stands for? ")
if answer.lower() == "random access memory":
    print("Wow, You Give right Answer...")
    score += 1
else:
    print("Wrong Answer!")

answer = input("3. What does ROM Stands for? ")
if answer.lower() == "read only memory":
    print("Correct Answer Again...:)")
    score += 1

else:
    print("Wrong!!!")


print("You Got " + str(score) + " questions Correct.....:)")
print("You Got " + str((score/3)*100) + " %")









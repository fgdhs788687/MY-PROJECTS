score=0
print("-----WELCOME TO THIS QUIZ GAME-----")
ask=input("Do you want to play (yes/no)? ").lower()

if ask!="yes":
    quit() # This function exits the program.


answer1=input("Q1> Which is the largest planet of our solar system?\nA. earth\nB. saturn\nC. jupiter\nD. mars\nANS->")

if answer1=="c" or answer1=="C":
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT! the correct answer was c or C which is jupiter.")    
print("---------------------------------")
answer2=input("Q2> How many bones are their in an human body?\nA. 226\nB. 206\nC. 256\nD. 236\nANS->")

if answer2=="b" or answer2=="B":
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT! the correct answer was b or B which is 206.")    
print("---------------------------------")
answer3=input("Q3> What is the full form of CPU?\nA. central processor unit\nB. central processing unit\nC. center processing unit\nD. central processing units\nANS->")

if answer3=="b" or answer3=="B":
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT! the correct answer was b or B which is central processing unit.")    
print("---------------------------------")
print(f"YOUR SCORE IS {score} OUT OF 3")
print("THANKS FOR PLAYING......")
print("---------------------------------")
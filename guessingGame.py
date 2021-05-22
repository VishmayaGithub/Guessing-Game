from random import randrange
random = randrange(15)
name=input("Enter Your name : ")

print("Hello",name,"welcome to the guessing game.I am thinking of a number between 1 and 15.")

for numberOfGuesses in range(1,6):
    
    guess = int(input("Enter Your guess : "))
    
    if(guess<random):
        print("I am thinking of a number bigger than ",guess)
    elif(guess>random) :
        print("I am thinking of a number smaller than",guess)   
    else:  break    

if(guess==random):
    print("Yay you won",name," !!!")        
if(guess!=random):
    print("Sorry you lost",name)            





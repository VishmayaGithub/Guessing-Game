from random import randrange
random = randrange(15)
name=input("Enter Your name : ")

print("Hello",name,"welcome to the guessing game. All you need to do is guess a number between 1 and 15")

for numberOfGuesses in range(1,6):
    
    guess = int(input("Enter Your guess : "))
    
    if(guess<random):
        print("Your guess is bigger than",guess)
    elif(guess>random) :
        print("Your guess is smaller than",guess)   
    else:  break    

if(guess==random):
    print("Yay you won!!!😁")        
if(guess!=random):
    print("Sorry you lost",name)            





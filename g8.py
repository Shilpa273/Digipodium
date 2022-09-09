# Text - based quiz games

print('enter your name')
x = input()
print('hello',x)
if x == "richard":
    print("That is a very cool name")
elif x == 'nick':
    print('That is a rubbish name')    
else:  
    print('I do not know your name',x)

# getting input from the keyboard
import random
n = random.randint(0,10)
print("What is",n, "plus 7?")
g = int(input()) 
if g == n + 7:
    print ('correct') 
else:
    print('wrong')
#making dicision :if,elif,else
#keeping score

score = 0
print('what is 1 + 1 ?')
g = int(input())
if g == 2:
    print('correct') 
score = score + 1
print("what is 35 - 25 ?")
g = int(input())
if g == 10:
    print('correct')
    score = score + 1
print("Your Score -->",score) 

# with the loop
import random 
n = random.randint(0,10)
while True:
    print("I am thinking of a number,can you guess what it is ?")
    g = int(input())
    if g == n:
        break
    else:
        print("wrong")
print('correct') 


# improved guessing game
import random
n = random.randint(0,100)
guesses = 0
while True:
    print("I am thinking of a number, can you guess what it is ?")
    g = int(input())
    if g == n:
        break
    elif g < n:
        print("Too low")
    elif g > n:
        print("Too high")
print('correct! You took', guesses,"guesses.")             

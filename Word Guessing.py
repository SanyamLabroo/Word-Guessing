import random
from itertools import chain, repeat
import time
import os

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

time.sleep(1)

tries = 0

Instructions = ["This is word guessing game.","I have chosen a word from the given list of the words.",
                "I will show you the  words and you will have to choose the correct word.",
                "The words are as follows:"]

for i in chain.from_iterable(repeat(Instructions, 1)):
    time.sleep(2)
    print(i)
    

WORDS = ["Red", "Green", "Yellow", "Blue", "Violet", "Tesla", "Google", "Apple", "IBM", "Instagram",
            "Twitter", "Facebook", "Youtube", "Telegram"]

def myFun(arg1,*argv): 
    print("First word is:",arg1)
    time.sleep(2)
    for arg in argv:
        time.sleep(2)
        print("Next word is:",arg) 
    
	
myFun("Red", "Green", "Yellow", "Blue", "Violet", "Tesla", "Google", "Apple", "IBM", "Instagram",
            "Twitter", "Facebook", "Youtube", "Telegram") 

word = random.choice(WORDS)

correct = word
length = len(word)
length = str(length)

hint = random.choice(length)

while tries < 3:
    
    print("Hint is the word is " + hint + " letters long")
    
    guess = input("Guess the Word: ")
    
    if guess not in WORDS:
        
        print("Word not in list!")
        see = input("Do you want to see the list of words again?\nPlease enter 'yes' or 'no': ")
        if see == 'yes':
            for i in chain.from_iterable(repeat(WORDS, 1)):
                time.sleep(1)
                print(i)
        elif see == 'no':
            guess = input("Guess the Word: ")
            
    tries = tries + 1
            
    if guess == word:
        print("Congratulations!..You won...:)")
        exit()
        
    elif guess != word:
        print("Sorry Your guess is wrong!\nPlease try again...")
        continue
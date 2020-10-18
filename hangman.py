#importing the time module
import time
import random
import string


#welcoming the user
name = input("What is your name? ")

print ("The next input is not for the person or people guessing!")
print ("If you are guessing please look away")

#wait for 1 second
time.sleep(5)

#here we set the secret
wordType = input('''Would you like to have someone select a word, 
or have a random string generated? Please say either random or select: ''')

def random_string(length):
    letters = string.ascii_lowercase
    result_str = ' '.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is: ", result_str)
    return result_str

if wordType == 'select':
    word = input("What will be the word?")
if wordType == 'random':
    length = int(input("How many letters in the random string? "))
    word = random_string(length)

print ("Hello, " + name, "Time to play hangman!")
print ('''The Judge must inform the player(s) if a random string has been generated, if so, 
the space character will be present between each letter, so input that as the first guess.
If a word was selected by the judge, please ensure the word and guesses are all the same case,
selected words should be either all upper or all lower case.''')

print ("Start guessing, may the odds be ever in your favor...")
time.sleep(0.5)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10
if wordType == 'random':
    turns = 20

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char)    

        else:
    
        # if not found, print a dash
            print ("_"),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word.lower():  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")
 
    # how many turns are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")
            print ("The word was ", word)
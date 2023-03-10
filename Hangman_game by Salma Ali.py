#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# ## Description
# > ##### The Hangman program randomly selects a secret word from a list of secret words.
# > ##### The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
# > ##### When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way,all letters of the word are to be guessed before all the chances are over.
# > ##### For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five letter word.

# In[ ]:


### pesudocode

1st Identify a Worrd , a variable for guessed letters & a variable for number of guesses
2nd start a while loop for number of guesses / take input from user / iterate over word letters /
add letter to guessed var if correct
3rd number of guesses decreases by 1 for each entry right or wrong
4th add back up if conditions for all typs of wrong input in the same loop
5th if word is guessed user wins 
6th if number of guesses zero and word not guessed break the loop and user loses.
7th choice for user to play again 


# ### simple system 

# In[25]:


word = 'apple'
chances = len(word) + 2
guessed_word = ''

for i in word:
    print('_' , end = ' ')
    
print()

while chances:
    chances -= 1
    
    letter = input('Guess a letter:').lower()
    
    if len(letter) > 1:
        print('ENTER ONLY 1 LETTER!!')
        continue 
        
    elif letter in guessed_word:
        print('YOU ALREADY GUESSSED THAT LETTER!!')
        continue
    
    elif letter.isalpha() == False:
        print('ENTER LETTERS ONLY!!')
        continue
        
            
    if letter in word:
        cntr= word.count(letter)
        for i in range(cntr):
            guessed_word += letter
            
        
    else:
        print('WRONG GUESS!!')
        continue
        
        
    for l in word:
        if l in guessed_word:
            print(l , end = ' ')
        else:
            print ('_' , end = ' ')
    print()
    
    

    if len(guessed_word) == len(word):
        print('CONGRATULATIONS, YOU WIN')
        break 
else:
    print('YOU LOST, HARD LUCK')
     


# ## A More Accurate System

# In[115]:


import random 
from collections import Counter 
Fruite_sellection ='''apple mango peach grapes pineapple orange'''
Fruite_sellection 
Fruite_sellection = Fruite_sellection.split(' ')
word = random.choice(Fruite_sellection )


# In[118]:


while True:
    print('Guess The Word!!! Hint: it is a fruite')
    import random 
    from collections import Counter 
    Fruite_sellection ='''apple mango peach grapes pineapple orange'''
    Fruite_sellection 
    Fruite_sellection = Fruite_sellection.split(' ')
    word = random.choice(Fruite_sellection )

    chances = len(word) + 2
    guessed_word = ''
    
    
    
    for i in word:
        print('_' , end = ' ')

    print()



    while chances:
        chances -= 1

        letter = input('Guess a letter:').lower()

        if len(letter) > 1:
            print('ENTER ONLY 1 LETTER!!')
            continue 

        elif letter in guessed_word:
            print('YOU ALREADY GUESSSED THAT LETTER!!')
            continue

        elif letter.isalpha() == False:
            print('ENTER LETTERS ONLY!!')
            continue


        if letter in word:
            counter= word.count(letter)
            for i in range(counter):
                guessed_word += letter


        else:
            print('WRONG GUESS!!')
            continue


        for l in word:
            if l in guessed_word:
                print(l , end = ' ')
            else:
                print ('_' , end = ' ')
        print()



        if len(guessed_word) == len(word):
            print('CONGRATULATIONS, YOU WIN')
            break 
    else:
        print('YOU LOST, HARD LUCK')
        
    print()
    

    end = input('DO YOU WANT TO PLAY AGAIN? Yes/No :').lower()
    if end == 'no' :
        break
         



# In[ ]:





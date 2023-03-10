#!/usr/bin/env python
# coding: utf-8

# In[101]:


while True:
    
    choice = input('Press 0 to convert from binary to Decimal \n Press 1 to convert from decimal to binary :')
    
    while choice not in  ['0' , '1']:
        print ('Invalid Input !!')
        choice = input('Press 0 to convert from binary to Decimal \n Press 1 to convert from decimal to binary :')


    if choice == '0':
        Decimal_Number = 0
        
        Binary_Number= (input('Enter Binary Number :' )) 
        
        while set(Binary_Number) != {'0' , '1'}:
            print ('Invalid Input !! Only 0 or 1 numbers')
            Binary_Number= (input('Enter Binary Number :' ))
            
        Binary_Number_r = Binary_Number[::-1]

        
        for i in range(len(Binary_Number_r)):
            Decimal_Number += int(Binary_Number_r[i]) * 2 ** i
            
        print (f'your binary number {Binary_Number} equals {Decimal_Number} in decimal ')
        
        
    else:
        
        while True:
            try:
                decimal_number = int(input('Enter Decimal Number :'))
                break 
                
            except Ex:
                print(type(e).__name__)
                
                
                
        binary_number= ''
        n = decimal_number
            
    
        while n >= 1:
                if n % 2 == 0:
                    binary_number+= '0'
                else:
                    binary_number+= '1'
                    
                n = int(n/2)
                
        print(f'your decimal number {decimal_number} equals {binary_number[::-1]} in binary')

    end = input('Do you want to continue converting? yes/no:')
    if end == 'no':
        break
        


# In[48]:


def check_binary_input(Binary_Number):
    if set(Binary_Number) == {'0' , '1'}:
        return True
    else:
        return False
                   
            


# In[49]:


check_binary_input('123')


# In[74]:


def convert_B_to_D (Binary_Number):  

    Decimal_Number = 0   
    Binary_Number_r = Binary_Number[::-1]
    
    for i in range(len(Binary_Number_r)):
        Decimal_Number += int(Binary_Number_r[i]) * 2 ** i
    return Decimal_Number 


# In[75]:


convert_B_to_D ('1000')


# In[ ]:


'''convertor = convert_B_to_D (Binary_Number)
while convertor == True :
    convertor = convert_B_to_D (Binary_Number)'''
 


# In[ ]:


def convert_D_to_B(n):
    binary_number= ''
    while n >= 1:
        if n % 2 == 0:
            binary_number+= '0'
        else:
            binary_number+= '1'
                    
        n = int(n/2)
    return binary_number[::-1]


# In[95]:


convert_D_to_B(80)


# ### Optimized wih functions 

# In[100]:


while True:
    
    choice = input('Press 0 to convert from binary to Decimal \n Press 1 to convert from decimal to binary :')
    
    while choice not in  ['0' , '1']:
        print ('Invalid Input !!')
        choice = input('Press 0 to convert from binary to Decimal \n Press 1 to convert from decimal to binary :')
        
#--------------------------------------------------------------------------------------------------------------

    if choice == '0':
        
        Binary_Number= (input('Enter Binary Number :' )) 
        
        checker = check_binary_input(Binary_Number)
        
        while checker != True:
            print ('Invalid Input !! Only 0 or 1 numbers')
            Binary_Number= (input('Enter Binary Number :' ))
            checker = check_binary_input(Binary_Number)
        
        Decimal_Number = convert_B_to_D (Binary_Number)
        
        print (f'your binary number {Binary_Number} equals {Decimal_Number} in decimal ')
        
 #-------------------------------------------------------------------------------------------------------       
        
    else:
        
        while True:
            try:
                decimal_number = int(input('Enter Decimal Number :'))
                break 
                
            except Exception as e:
                print(type(e).__name__)
                
            
        binary_number = convert_D_to_B(decimal_number)  
        
        print(f'your decimal number {decimal_number} equals {binary_number} in binary')

#----------------------------------------------------------------------------------------------------------

    end = input('Do you want to continue converting? yes/no:')
    if end == 'no':
        break
        


# # Rock, Paper, Scissors

# In[ ]:


#pseudocode
'''game's premise is, rock breaks scissors >> rock wins
                  paper slides rock >> paper wins 
                  scissors cuts paper >> scissors wins'''
1st input from user (R,P or S) + validate input
2nd a random generator is required with (R, P or S)
3rd set of conditions based on the premise , decide winner or loser, break loop each time
4th repeat if user wants to play again 


# In[57]:


import random 
from collections import Counter


# In[58]:


options = ['rock', 'paper' , 'scissors']


# In[71]:


while True: 
 
    while True:
        user_choice = input('What is your choice Rock, Paper or Scissors??! :').lower()
        computer_choice = random.choice(options)
        num_of_tries = 3
        
        while user_choice not in options:
            print('WRONG INPUT , CHOOSE AGAIN')
            user_choice = input('What is your choice Rock, Paper or Scissors??! :').lower()
            

        if user_choice == 'rock' and computer_choice == 'paper':
            print('computer choice is paper')
            print('paper slides rock')
            print('YOU LOSE!')
            break

        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('computer choice is scissors')
            print('rock breaks scissors')
            print('YOU WIN!')
            break


        elif user_choice == 'scissors' and computer_choice == 'rock':
            print('computer choice is rock')
            print('rock breaks scissors')
            print('YOU LOSE!')
            break

        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('computer choice is paper')
            print('scissors cuts paper')
            print('YOU WIN!')
            break

        
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('computer choice is rock')
            print('paper slides rock')
            print('YOU WIN!')
            break

        elif user_choice == 'paper' and computer_choice == 'scissors':
            print('computer choice is scissors')
            print('scissors cuts paper')
            print('YOU LOSE!')
            break

        elif user_choice == computer_choice:
            print(f'computer choice is {computer_choice} and your choice is {user_choice}')
            print('IT IS A TIE , CHOOSE AGAIN')
            continue

    end = input('Do you want to play again??  yes or no :').lower()
    if end in ['yes' , 'y']:
        continue
    else:
        break 


# In[ ]:





# In[ ]:





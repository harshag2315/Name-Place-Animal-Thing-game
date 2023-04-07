import time
import random
import string
from animal_checker import is_animal
from thing_checker import is_thing
from country_checker import is_place
x=0
while(x!=1):
    num_player=int(input('Enter the number of players:'))      #enter number of players
    marks=[]
    player_name=[]
    print('***************************************************RULES**************************************************')
    print('1.Maximum time is 40 sec for each player if time exceed player is elimnatd automatically from the game')
    print('2.Any invalid character in the game may result into elimination also')
    print('3.player is rewarded 10 points for every correct answer')
    print('4.player is rewarded 0 points for every incorrect answer')
    print('************************************************GAME STARTS***********************************************')


    #enter palyer name with error detection
    for i in range(0,num_player):
        user_name=input('Enter your player name:')
        try:
            if user_name.isalpha():
                player_name.append(user_name)
            else:
                raise ValueError('Invalid input: name must not be a number')
        except ValueError as e:
            print(f'Input not valid: {e}')
    q=random.choice(string.ascii_uppercase)
    q_lower = q.lower()
    print(f'Please form the name, place, animal and thing from letter : "{q}"')
    elapsed_time_total=[]
    player_data=[]

    #input of data
    for i in range(0, len(player_name)):
        user_marks=0                  #intial score is '0'
        start_time = time.time()
        print('--------------------------------------------------------------------------------------------------------')
        try:
            player={
                'Name':input('Enter the Name:'),
                'Place':input('Enter the place:'),
                'Animal':input('Enter the Animal:'),
                'Thing':input('Enter the Thing:')
            }
            for value in player.values():
                if not value.isalpha():
                    raise ValueError("Error: Please enter a valid string.")
        except ValueError as e:
            print(f'Please enter valid data and error occured : {e}')
        print('--------------------------------------------------------------------------------------------------------')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'The time consumed by {player_name[i]} is {elapsed_time}')
        elapsed_time_total.append(elapsed_time)
        player_data.append(player)

        #marks giving
        if player['Animal'][0]==q or player['Animal'][0]==q_lower:
            if is_animal(player['Animal']):
                user_marks+=10
                print('Y1')
        elif player['Animal']!=q or player['Animal'][0]!=q_lower:
            player['Animal']=''
        if player['Name'][0]==q or player['Name'][0]==q_lower:
            user_marks+=10
            print('Y2')
        elif player['Name'][0]!=q or player['Name'][0]!=q_lower:
            player['Name']=''
        if player['Place'][0]==q or player['Place'][0]==q_lower:
            if is_place(player['Place']):    
                user_marks+=10     
                print('Y3') 
        elif player['Place'][0]!=q or player['Place'][0]!=q_lower:
            player['Place']=''
        if player['Thing'][0]==q or player['Thing'][0]==q_lower:
            if is_thing(player['Thing']):
                user_marks+=10
                print('Y4')
        elif player['Thing'][0]!=q or player['Thing'][0]!=q_lower:
            player['Thing']=''
        marks.append(user_marks)
        print('-----------------------------------------------------------------------------------------------------')



    #time checking
    for i in range(0, len(player_name)):
        if elapsed_time_total[i]>40:
            print(f'Due to time limitations, Data and Name of {player_name[i]} are removed from the game.')
            del player_name[i]
            del player_data[i]
    


    #human data display
    max_marks = 0
    temp_name = [player_name[0]]
    for i in range(0, len(player_name)):
        
        print(f'Input by {player_name[i]} is {player_data[i]}')
        print(f'Marks scored by {player_name[i]} is {marks[i]}')
    
        if marks[i] > max_marks:
            max_marks=marks[i]
            temp_name=[player_name[i]]
        elif marks[i] == max_marks:
            temp_name.append(player_name[i])
        print('-----------------------------------------------------------------------------------------------------')
    
    if len(temp_name) == 1:
        print(f'The player {temp_name[0]} win the game with max score is : {max_marks}')
        print('Want to play more.....')
        a=int(input('If you want to play more press 0... else to exit game press 1....'))
        if a==1:
            print('Thanks for playing the game')
            x+=1
    else:
        print(f'More than 1 player has scored the same score of {max_marks}')
        print(f'Play again to decide the game....')
        a=int(input('If you want to play again press 0... else to exit game press 1....'))
        if a==1:
            print('Thanks for playing the game')
            x+=1
    print('---------------------------------------------------------------------------------------------------------')
        
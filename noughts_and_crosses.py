#!/usr/bin/env python
# coding: utf-8

from IPython.display import clear_output
from random import shuffle

# 

def display_board(board):
    
    pass

# 

def noughts_and_crosses():
    player1 = input('Name of Player 1: ').capitalize()
    player2 = input('\nName of Player 2: ').capitalize()
    
    player1_symb = input(f'\n\n{player1}: Do you want to be X or O? ').capitalize()
    
   
    if player1_symb == 'X' or player1_symb == 'O':
        if player1_symb == 'X':
            player2_symb = 'O'
            print (f'\n{player2} that makes you O')
            
        
        elif player1_symb == 'O':
            player2_symb = 'X'
            print (f'\n{player2} that makes you X')
            
        
    else:
        while player1_symb !='X' or player1_symb !='O':
            print("\nOops! Try again! You seem to have entered a character this game doesn't like! \nRemember it needs to be an X or an O...")
            player1_symb = input(f'\n{player1}: Do you want to be X or O? ').capitalize()
        
            if player1_symb == 'X':
                player2_symb = 'O'
                print (f'\n{player2} that makes you O')
                break
            
        
            elif player1_symb == 'O':
                player2_symb = 'X'
                print (f'\n{player2} that makes you X')
                break
    
    return [player1,player1_symb,player2,player2_symb]

# 

def randomiser (player1,player1_symb,player2,player2_symb):
    
    players = [player1,player2]

        
    #shuffle order of players
    
    shuffle(players)
    shuffle_player1 = players[0]
    shuffle_player2 = players[1]
    
    
    #assign previously chosen player symbols to shuffled players
    
    if shuffle_player1 == player1:
        shuffle_player1_symb = player1_symb
        shuffle_player2_symb = player2_symb
    elif shuffle_player1 == player2:
        shuffle_player1_symb = player2_symb
        shuffle_player2_symb = player1_symb

      
    return [shuffle_player1,shuffle_player1_symb,shuffle_player2,shuffle_player2_symb]

# 

def win_check(my_list,player1,player1_symb,player2,player2_symb):
      

            # grid position 1,2,3

    if my_list[0] == my_list[1] == my_list[2]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[0] == my_list[1] == my_list[2]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')


                # grid position 1,5,9

    elif my_list[0] == my_list[4] == my_list[8]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[0] == my_list[4] == my_list[8]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')


                # grid position 1,4,7 

    elif my_list[0] == my_list[3] == my_list[6]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[0] == my_list[3] == my_list[6]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')


                # grid position 2,5,8  

    elif my_list[1] == my_list[4] == my_list[7]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[1] == my_list[4] == my_list[7]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')


                # grid position 3,6,9  

    elif my_list[2] == my_list[5] == my_list[8]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[2] == my_list[5] == my_list[8]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')



                # grid position 3,5,7 

    elif my_list[2] == my_list[4] == my_list[6]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[2] == my_list[4] == my_list[6]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')


                # grid position 4,5,6

    elif my_list[3] == my_list[4] == my_list[5]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[3] == my_list[4] == my_list[5]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')



                # grid position 7,8,9 

    elif my_list[6] == my_list[7] == my_list[8]=='X':
        if player1_symb == 'X':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'X':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

    elif my_list[6] == my_list[7] == my_list[8]=='O':
        if player1_symb == 'O':
            print (f'\n\n{player1} YOU WIN!')
            return ('YOU WIN')
        elif player2_symb == 'O':
            print (f'\n\n{player2} YOU WIN!')
            return ('YOU WIN')

# 

def no_win(my_list,player1,player1_symb,player2,player2_symb):
    
 
            # grid position 1,2,3

    if (my_list[0] == my_list[1] == my_list[2]) == False:

        # grid position 1,5,9

        if (my_list[0] == my_list[4] == my_list[8]) == False:
     
            # grid position 1,4,7 

            if (my_list[0] == my_list[3] == my_list[6]) == False:
      
            # grid position 2,5,8  

                if (my_list[1] == my_list[4] == my_list[7]) == False:
       
            # grid position 3,6,9  

                    if (my_list[2] == my_list[5] == my_list[8]) == False:
        
            # grid position 3,5,7 

                        if (my_list[2] == my_list[4] == my_list[6]) == False:
       
            # grid position 4,5,6

                            if (my_list[3] == my_list[4] == my_list[5]) == False:
       

            # grid position 7,8,9 

                                if (my_list[6] == my_list[7] == my_list[8]) == False:
    
                                    print (f"\n\nAh I'm sorry to say it, but {player1} and {player2} neither of you have won...")

# 

def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

#

def game_on (player1,player1_symb,player2,player2_symb):
    

    my_list = ['1','2','3','4','5','6','7','8','9']
    print ("       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*my_list))

  
    try:

        ################
        #### Turn 1 ####
        ################


        player1_choice = input(f'\n\n{player1}, looking at the board, where would you like to place your first {player1_symb}? \n(Choose the corresponding digit):    ')

        while (player1_choice.isdigit() == False) or (player1_choice not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player1_choice = input(f'\n\n{player1}, looking at the board, where would you like to place your first {player1_symb}? \n(Choose the corresponding digit):    ')

        clear_output()

        new_list = []

        for num in my_list:
            alpha = num.replace(player1_choice,player1_symb)
            new_list.append(alpha)



        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list))



        ################
        #### Turn 2 ####
        ################

        player2_choice = input(f'\n\n{player2}, looking at the board, where would you like to place your first {player2_symb}? \n(Choose the corresponding digit):    ')


        while (player2_choice == player1_choice) or (player2_choice.isdigit() == False) or (player2_choice not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player2_choice = input(f'\n\n{player2}, looking at the board, where would you like to place your first {player2_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list2 = []

        for num in new_list:
            bravo = num.replace(player2_choice,player2_symb)
            new_list2.append(bravo)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list2))



        ################
        #### Turn 3 ####
        ################

        player1_choice2 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')

        while (player1_choice2 == player2_choice) or (player1_choice2 == player1_choice) or (player1_choice2.isdigit() == False) or (player1_choice2 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player1_choice2 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list3 = []

        for num in new_list2:
            charlie = num.replace(player1_choice2,player1_symb)
            new_list3.append(charlie)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list3))



        ################
        #### Turn 4 ####
        ################

        player2_choice2 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')

        while (player2_choice2 == player1_choice2) or (player2_choice2 == player2_choice) or (player2_choice2 == player1_choice) or (player2_choice2.isdigit() == False) or (player2_choice2 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player2_choice2 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list4 = []

        for num in new_list3:
            delta = num.replace(player2_choice2,player2_symb)
            new_list4.append(delta)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list4))



        ################
        #### Turn 5 ####
        ################

        player1_choice3 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')

        while (player1_choice3 == player2_choice2) or (player1_choice3 == player1_choice2) or (player1_choice3 == player2_choice) or (player1_choice3 == player1_choice) or (player1_choice3.isdigit() == False) or (player1_choice3 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player1_choice3 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list5 = []

        for num in new_list4:
            echo = num.replace(player1_choice3,player1_symb)
            new_list5.append(echo)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list5))




        sierra = win_check(new_list5,player1,player1_symb,player2,player2_symb)

       
        if sierra == 'YOU WIN':
            raise RuntimeError ('!')
        else:
            pass
        


        ################
        #### Turn 6 ####
        ################

        player2_choice3 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')

        while (player2_choice3 == player1_choice3) or (player2_choice3 == player2_choice2) or (player2_choice3 == player1_choice2) or (player2_choice3 == player2_choice) or (player2_choice3 == player1_choice) or (player2_choice3.isdigit() == False) or (player2_choice3 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player2_choice3 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list6 = []

        for num in new_list5:
            foxtrot = num.replace(player2_choice3,player2_symb)
            new_list6.append(foxtrot)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list6))



        sierra = win_check(new_list6,player1,player1_symb,player2,player2_symb)

        if sierra == 'YOU WIN':
            raise RuntimeError ('!')
        else:
            pass
        


        ################
        #### Turn 7 ####
        ################

        player1_choice4 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')

        while (player1_choice4 == player2_choice3) or (player1_choice4 == player1_choice3) or (player1_choice4 == player2_choice2) or (player1_choice4 == player1_choice2) or (player1_choice4 == player2_choice) or (player1_choice4 == player1_choice) or (player1_choice4.isdigit() == False) or (player1_choice4 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player1_choice4 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list7 = []

        for num in new_list6:
            golf = num.replace(player1_choice4,player1_symb)
            new_list7.append(golf)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list7))



        sierra = win_check(new_list7,player1,player1_symb,player2,player2_symb)

        if sierra == 'YOU WIN':
            raise RuntimeError ('!')
        else:
            pass
        


        ################
        #### Turn 8 ####
        ################

        player2_choice4 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')

        while (player2_choice4 == player1_choice4) or (player2_choice4 == player2_choice3) or (player2_choice4 == player1_choice3) or (player2_choice4 == player2_choice2) or (player2_choice4 == player1_choice2) or (player2_choice4 == player2_choice) or (player2_choice4 == player1_choice) or (player2_choice4.isdigit() == False) or (player2_choice4 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player2_choice4 = input(f'\n\n{player2}, looking at the board, where would you like to place your next {player2_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list8 = []

        for num in new_list7:
            hotel = num.replace(player2_choice4,player2_symb)
            new_list8.append(hotel)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list8))


        sierra = win_check(new_list8,player1,player1_symb,player2,player2_symb)

        if sierra == 'YOU WIN':
            raise RuntimeError ('!')
        else:
            pass
        


        ################
        #### Turn 9 ####
        ################

        player1_choice5 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')

        while (player1_choice5 == player2_choice4) or (player1_choice5 == player1_choice4) or (player1_choice5 == player2_choice3) or (player1_choice5 == player1_choice3) or (player1_choice5 == player2_choice2) or (player1_choice5 == player1_choice2) or (player1_choice5 == player2_choice) or (player1_choice5 == player1_choice) or (player1_choice5.isdigit() == False) or (player1_choice5 not in ['1','2','3','4','5','6','7','8','9']):
            print ("Oops! Something seems off with what you entered... remember it needs to be one of the digits from the playing grid, but not one that's already been chosen! Try again")
            player1_choice5 = input(f'\n\n{player1}, looking at the board, where would you like to place your next {player1_symb}? \n(Choose the corresponding digit):    ')


        clear_output()

        new_list9 = []

        for num in new_list8:
            india = num.replace(player1_choice5,player1_symb)
            new_list9.append(india)

        print ("\n\n\n\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       \n-----------------------\n       |       |       \n   {}   |   {}   |   {}   \n       |       |       ".format(*new_list9))



        sierra = win_check(new_list9,player1,player1_symb,player2,player2_symb)
        
        if sierra == 'YOU WIN':
            raise RuntimeError ('!')
        else:
            pass
                

        no_win(new_list9,player1,player1_symb,player2,player2_symb)
  


        print('\n\n\n')

    except RuntimeError as msg:
        print('\n\nWooooooooo',msg)

    if yes_or_no("\n\nWould you like to play again?"):
        return 'new_game'
    else:
        return 'no_play'
        

# 

def are_we_ready(player1,player1_symb,player2,player2_symb):
    
    answer = input(f"\n\n\n\n{player1} and {player2}, are you ready to play?" + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(f"\n\n\n\n\n{player1} and {player2}, are you ready to play!" + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        #print (f"\n\nAwesome!\n\nLet's play!\n\n\n\nRemember:\n\n{player1} you're {player1_symb}\n{player2} you're {player2_symb}")
        return 'y'
    else:
        
        return'n'

# 

def start_screen ():
    print ("\n\n                                  \n               X      O       X  \n                                  \n                                  \n                   NOUGHTS        \n               O      &       O   \n                   CROSSES        \n                           \n                                  \n               X      O       X  \n                                  \n\n")
    print("          --------------------------\n             Press ENTER to play!  \n          --------------------------\n")
    oscar = input()
    return oscar

# 

def start_game ():
    papa = start_screen()
    if papa == ():
        pass
    else:
        pass
    
    clear_output()
    a = noughts_and_crosses()
    c = are_we_ready(a[0],a[1],a[2],a[3])
    while c == 'y':
        clear_output()
        print (f"\n\nAwesome!\n\nLet's play!\n\n\n\nRemember:\n\n{a[0]} you're {a[1]}\n{a[2]} you're {a[3]}")

        b = randomiser(a[0],a[1],a[2],a[3])
        print (f'\n\n\nOur randomiser has decided that...')
        print (f'{b[0]} will go first and {b[2]} will go second!\n\n\n\n\n')
        print("          --------------------------\n             Press ENTER to play!  \n          --------------------------\n")

        romeo = input()
        if romeo == ():
            pass
        else:
            pass

        clear_output()
        print('\n\n\n')
        d = game_on(b[0],b[1],b[2],b[3])

        if d == 'no_play':
            clear_output()
            print("\nThat's okay! See you next time!")
            print("\n\n                      \n   X      O       X  \n                      \n              \n       NOUGHTS        \n   O      &       O   \n       CROSSES        \n               \n                      \n   X      O       X  \n                      \n")
            break
        elif d == 'new_game':
            print ("Let's play again!")
            # go back to beginning - play again

    if c == 'n':
        clear_output()
        #print ('NOUGHTS & CROSSES')
        print ('\nOh :( maybe next time then!')
        print ('Have a good one!')
        print ("\n\n                      \n   X      O       X  \n                      \n              \n       NOUGHTS        \n   O      &       O   \n       CROSSES        \n               \n                      \n   X      O       X  \n                      \n\n")


#

start_game()



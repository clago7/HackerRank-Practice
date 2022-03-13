# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem

import math
def minion_game(string, player_con, player_vow):
    player_con_score, player_vow_score = 0, 0
    vowels = ['A','E','I','O','U']
    # for sub_len in range(len(string)):
    #     iterations = math.floor(len(string)-sub_len)
    #     for iteration in range(iterations):
    #         sub_string = string[iteration:iteration+sub_len+1]
    #         if sub_string[0].upper() in vowels:
    #             player_vow_score += 1
    #         else: player_con_score += 1
    # nested loops above went through every possible sub_string...which gave rise to time exceeded error
    # alternatively...can be done with one loop by calculating total possible points for each letter of string
    for pos in range(len(string)):
        pos_points = len(string) - pos
        if string[pos].upper() in vowels:
            player_vow_score += pos_points
        else: player_con_score += pos_points

    if player_con_score > player_vow_score:
        print(f'{player_con.title()} {player_con_score}')
    elif player_con_score < player_vow_score:
        print(f'{player_vow.title()} {player_vow_score}')
    elif player_con_score == player_vow_score:
        print('Draw')

string = input('Enter string: ')
player_con = input('Enter name of player making consonants: ')
player_vow = input('Enter name of player making vowels: ')
minion_game(string, player_con, player_vow)
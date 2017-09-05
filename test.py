#!/usr/bin/env python

import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Rester', 'Exit']

letter_codes = [ord(ch) for ch in 'wasdrqWASDRQ']

action_dict = dict(zip(letter_codes, action * 2))

class Game_field(object):
    def _init_(self, height=4, width=4, win = 2048):
        self.height = height
        self.width = width
        self.win_walue = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def reset(self):
        if self.score > self.highscore:
            self.score = self.highscore
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range ]
    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [for i in range(self.row) if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):           
                    if pair:
                        new_row.append( 2 * row[i] )
                        self.score += 2*row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i-1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field

  





    def draw(self, screen):

    def is_win(self):

    def is_gameover(self):
 
    def spawn(self):

    def move_is_possible

def main(stdscr):

    state_action = {
             'Init': init,
             'Win': lambda: not_game('Win'),
             'Gameover': lambda: not_game('Game'),

    def init():
        return 'Game'

    def not_game():
        #picture the 'game over' or 'win'
        #input action and judge reset the game or end the game\
        
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():

        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        
        if action = 'Restart':
            return 'init'

        elif action = 'Exit':
            return 'Exit'

        else game_field.move(action):
        
            if game_field.is_win():
                return 'Win'
   
            if game_field.is_gameover():
                return 'Gameover'
        
        return 'Game'
        
    state_action = {
             'Init': init,
             'Win': lambda: not_game('Win'),
             'Gameover': lambda: not_game('Gameover'),
             'Game': game
            }

    curses.use_default_colors()
    game_field = Game_field(win = 32)

    state = 'Init'
                
    while state != 'Exit':
         state = state_actions[state]()

curses.wrapper(main)



        





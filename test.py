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

    def move(self, direction):


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



        





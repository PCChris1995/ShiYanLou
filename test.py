#!/usr/bin/env python

import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Rester', 'Exit']

letter_codes = [ord(ch) for ch in 'wasdrqWASDRQ']

action_dict = dict(zip(letter_codes, action * 2))

def main(stdscr):

    def init():
        return 'Game'

    def not_game():
        





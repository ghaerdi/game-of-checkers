import os
import time
class View:
    def __init__(self, start_view):
        self.cache = []
        self.start_view = start_view
        self.trim = 180 # limit to trim
        self.view = None

    def render_view(self, view, error, move_error): # rendering the table
        self.cache.append(view) # add table to cache

        if len(self.cache[-1]) <= self.trim:
            os.system('clear')
            if error != None and error != [] or move_error != [] and move_error != None:
                print(f'type error => {error or move_error}')
                time.sleep(2.5)
                os.system('clear')
            self.view = self.cache[-1][:self.trim]
            print(self.view)

        if len(self.cache[-1]) > self.trim:
            os.system('clear')
            if error != None and error != [] or move_error != [] and move_error != None:
                print(f'type error => {error or move_error}') # log errors
                time.sleep(2.5)
                os.system('clear')
            self.view = self.cache[-1][self.cache[-1].rfind('\n') - self.trim:self.cache[-1].rfind('\n')] # cut the table on the last play
            print(self.view)
        self.cache[:] # clean cache

    def consult_dead_token(self): # consult player winner
        stade = [0, -1]

        for token in range(len(self.view)):
            if self.view[token] == '⭕' or self.view[token] == 'R':
                stade[0] += 1
            if self.view[token] == '⚫' or self.view[token] == 'B':
                stade[1] += 1

        if stade[0] == 0:
            return 'black'
        if stade[1] == 0:
            return 'red'

    def start_render_view(self, turn): # rende start game
        self.loading()
        print(self.start_view)

    def print_turn(self, turn): # handle the turn
        if turn == 0:
            print('Turn for ⭕  or R token')
            print('\n')
        elif turn == 1:
            print('Turn for ⚫ or B token')
            print('\n')

    def loading(self): # loading screen
        for i in range(101):
            time.sleep(0.015)
            os.system('clear')
            print('                                                     loading')
            print('[{}] {}'.format(('◾' * i), (str(i) + ' %')))

        time.sleep(0.2)
        os.system('clear')
        print('                                 ===========================================================')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                        checkers                         ॥')
        print('                                 ॥                        中国女士                         ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ===========================================================')
        time.sleep(2)
        os.system('clear')
        print('                                 ====================================================================')
        print('                                 ॥                           How to play 🎮                          ॥')
        print('                                 ॥ ⚫ select a coordinate for example A2 and then assign an address  ॥')
        print('                                 ॥                                                                  ॥')
        print('                                 ॥ ✅ the Black pieces have "rd" (right down) and "ld" (left down)   ॥')
        print('                                 ॥ ✅ the Red pieces have "ru" (right up) and "lu" (left up)         ॥')
        print('                                 ॥ ✅ the Dames have all directions  ( ru, lu, rd, ld )              ॥')
        print('                                 ॥                                                                  ॥')
        print('                                 ====================================================================')
        time.sleep(7)
        os.system('clear')
        print(' _________________       _________________       _       ________________        _______    _______ _______ _______ _______')
        print('(  ____ \__   __( (    /(  ____ \__   __( (    /( (    /(  ___  )__   __/\     /(  ____ \  (  ____ (  ___  |       |  ____ \ ')
        print('| (    \/  ) (  |  \  ( | (    \/  ) (  |  \  ( |  \  ( | (   ) |  ) (  | )   ( | (    \/  | (    \/ (   ) | () () | (    \/')
        print('| |        | |  |   \ | | |        | |  |   \ | |   \ | | (___) |  | |  | |   | | (_____   | |     | (___) | || || | (__    ')
        print('| |        | |  | (\ \) | |        | |  | (\ \) | (\ \) |  ___  |  | |  | |   | (_____  )  | | ____|  ___  | |(_)| |  __)   ')
        print('| |        | |  | | \   | |        | |  | | \   | | \   | (   ) |  | |  | |   | |     ) |  | | \_  ) (   ) | |   | | (      ')
        print('| (____/\__) (__| )  \  | (____/\__) (__| )  \  | )  \  | )   ( |  | |  | (___) /\____) |  | (___) | )   ( | )   ( | (____/\ ')
        print('(_______|_______//    )_|_______|_______//    )_)/    )_)/     \|  )_(  (_______)_______)  (_______)/     \|/     \(_______/')
        time.sleep(3)
        os.system('clear')
import os
import time
class View:
    def __init__(self, start_view):
        self.cache = []
        self.start_view = start_view
        self.trim = 180
        self.view = None
    def render_view(self, view, error, move_error):
        self.cache.append(view)
        if len(self.cache[-1]) <= self.trim:
            os.system('clear')
            if error != None or error != []:
                print(f'type error => {error or move_error}')
            time.sleep(2)
            os.system('clear')
            self.view = self.cache[-1][:self.trim]
            print(self.view)
        if len(self.cache[-1]) > self.trim:
            os.system('clear')
            if error != None:
                print(f'type error => {error or move_error}')
            time.sleep(2)
            os.system('clear')
            self.view = self.cache[-1][self.cache[-1].rfind('\n') - self.trim:self.cache[-1].rfind('\n')]
            print(self.view)
        self.cache[:]
    def consult_dead_token(self):
        stade = [0, -1]
        for token in range(len(self.view)):
            if self.view[token] == '⭕' or self.view[token] == 'R':
                stade[0] += 1
            if self.view[token] == '⚫' or self.view[token] == 'B':
                stade[1] += 1
        return stade
    def rende_history(self):
        os.system('clear')
        print(self.cache[-1])
    def start_render_view(self, turno):
        self.loading()
        print(turno)
        print(self.start_view)
    def loading(self):
        for i in range(101):
            time.sleep(0.03)
            os.system('clear')
            print('                                                     loading')
            print('[{}] {}'.format(('◾' * i), (str(i) + ' %')))
        time.sleep(0.8)
        os.system('clear')
        print('                                 ===========================================================')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                     Chinese checkers                    ॥')
        print('                                 ॥                         中国女士                        ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ॥                                                         ॥')
        print('                                 ===========================================================')
        time.sleep(1)
        os.system('clear')
        tutorial = input('skip tutorial? [yes / no] ')
        if tutorial.lower() == 'n' or tutorial.lower() == 'no':
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
            time.sleep(10)
            os.system('clear')
        os.system('clear')
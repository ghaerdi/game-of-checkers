import os
class View:
    def __init__(self):
        self.cache = []
        self.trim = 180
    def render_view(self, view):
        self.cache.append(view)
        if len(self.cache[-1]) <= self.trim:
            os.system('clear')
            print(self.cache[-1][:self.trim])
        if len(self.cache[-1]) > self.trim:
            os.system('clear')
            print(self.cache[-1][self.cache[-1].rfind('\n') - self.trim:self.cache[-1].rfind('\n')])
        self.cache[:]
class Model:
    def __init__(self):
        self.Table = [  # the table for game
            ['1','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['2','⬛', '⬜', '⬛', '⬜', '⭕', '⬜', '⬛' ,'⬜', '\n'],
            ['3','⬜', '⭕', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['4','⬛', '⬜', '⬛', '⬜', '⚫', '⬜', '⭕' ,'⬜', '\n'],
            ['5','⬜', '⭕', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['6','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⭕' ,'⬜', '\n'],
            ['7','⬜', '⬛', '⬜', '⭕', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['8','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            [' ','A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', '\n']
        ]
        self.generated_table = []
        self.cache = ' '
        self.view = ''
        self.error = None
    def input_instructions(self, instructions):
        print(instructions)
        try:
            self.tokens_cache = self.Table[instructions[0]][instructions[1]]
            if self.tokens_cache != '⬛' or self.tokens_cache != '⬜':
            # <----------------------for recursive eat---------------------------->
                if len(instructions) == 5:
                    self.eat_recursive(instructions[0], instructions[1], instructions[4])
                else:
                    self.Table[instructions[0]][instructions[1]] = '⬛'
                    if self.tokens_cache == '⭕' and instructions[2] == 0: # Add instructions convert a red token to dame
                        self.Table[instructions[2]][instructions[3]] = 'R'
                    elif self.tokens_cache == '⚫' and instructions[2] == 7: # Same whit black token
                        self.Table[instructions[2]][instructions[3]] = 'B'
                    else:
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            for j in self.Table:
                for i in j:
                    self.generated_table.append(i)
            self.generated_table.insert(0, '')
            self.view = self.cache.join(self.generated_table)
            self.testing = instructions
        except:
            print(instructions)
    def return_model_view(self):
        return self.view # return compile table for view
    def return_raw_table(self):
        return self.Table # return raw table for controller
    def return_render_view(self):# compiler
        for j in self.Table:
            for i in j:
                self.generated_table.append(i)
        self.generated_table.insert(0, '')
        self.view = self.cache.join(self.generated_table)
        return self.view
    def eat_recursive(self, cordinate0, cordinate1, direction): # generate move and eat enemy tokens
        self.token = self.Table[cordinate0][cordinate1]
        if self.token == '⚫' or self.token == 'B': # make the movements of the black pieces
            if direction == 'rd':
                if self.Table[cordinate0 + 1][cordinate1 + 1] == '⭕' or self.Table[cordinate0 + 1][cordinate1 + 1] == 'R':
                    if self.Table[cordinate0 + 2][cordinate1 + 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 + 1][cordinate1 + 1] = '⬛'
                        if (cordinate0 + 2) == 7:
                            self.Table[cordinate0 + 2][cordinate1 + 2] = 'B'
                            return ''
                        else:
                            self.Table[cordinate0 + 2][cordinate1 + 2] = self.token
                        return self.eat_recursive((cordinate0 + 2), (cordinate1 + 2), 'rd')
                    if self.Table[cordinate0 + 2][cordinate1 + 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                else:
                    if self.Table[cordinate0 + 1][cordinate1 + 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'ld')
            if direction == 'ld':
                if self.Table[cordinate0 + 1][cordinate1 - 1] == '⭕' or self.Table[cordinate0 + 1][cordinate1 - 1] == 'R':
                    if self.Table[cordinate0 + 2][cordinate1 - 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 + 1][cordinate1 - 1] = '⬛'
                        if (cordinate0 + 2) == 7: # if you manage to reach the opposite side he become a dame
                            self.Table[cordinate0 + 2][cordinate1 - 2] = 'B'
                            return ''
                        else:
                            self.Table[cordinate0 + 2][cordinate1 - 2] = self.token
                        return self.eat_recursive((cordinate0 + 2), (cordinate1 - 2), 'ld')
                    if self.Table[cordinate0 + 2][cordinate1 - 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                        # test <----------------------klk-------------------------->
                else:
                    if self.Table[cordinate0 + 1][cordinate1 - 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'rd')
        if self.token == '⭕' or self.token == 'R': # make the movements of the red pieces
            if direction == 'ru':
                if self.Table[cordinate0 - 1][cordinate1 + 1] == '⚫' or self.Table[cordinate0 - 1][cordinate1 + 1] == 'B':
                    if self.Table[cordinate0 - 2][cordinate1 + 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 + 1] = '⬛'
                        if (cordinate0 - 2) == 0:
                            self.Table[cordinate0 - 2][cordinate1 + 2] = 'R'
                            # return ''
                        else:
                            self.Table[cordinate0 - 2][cordinate1 + 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 + 2), 'ru')
                    if self.Table[cordinate0 - 2][cordinate1 + 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                else:
                    if self.Table[cordinate0 - 1][cordinate1 + 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'lu')
            if direction == 'lu':
                if self.Table[cordinate0 - 1][cordinate1 - 1] == '⚫' or self.Table[cordinate0 - 1][cordinate1 - 1] == 'B':
                    if self.Table[cordinate0 - 2][cordinate1 - 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 - 1] = '⬛'
                        if (cordinate0 - 2) == 0: # if you manage to reach the opposite side he become a dame
                            self.Table[cordinate0 - 2][cordinate1 - 2] = 'R'
                            return ''
                        else:
                            self.Table[cordinate0 - 2][cordinate1 - 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 - 2), 'lu')
                    if self.Table[cordinate0 - 2][cordinate1 - 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                else:
                    if self.Table[cordinate0 - 1][cordinate1 - 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'ru')
        if self.token == 'B': # make the movements of the black dame pieces
            if direction == 'ru':
                if self.Table[cordinate0 - 1][cordinate1 + 1] == '⭕' or self.Table[cordinate0 - 1][cordinate1 + 1] == 'R':
                    if self.Table[cordinate0 - 2][cordinate1 + 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 + 1] = '⬛'
                        self.Table[cordinate0 - 2][cordinate1 + 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 + 2), 'ru')
                    if self.Table[cordinate0 - 2][cordinate1 + 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                else:
                    if self.Table[cordinate0 - 1][cordinate1 + 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'lu')
            if direction == 'lu':
                if self.Table[cordinate0 - 1][cordinate1 - 1] == '⭕' or self.Table[cordinate0 - 1][cordinate1 - 1] == 'R':
                    if self.Table[cordinate0 - 2][cordinate1 - 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 - 1] = '⬛'
                        self.Table[cordinate0 - 2][cordinate1 - 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 - 2), 'lu')
                    if self.Table[cordinate0 - 2][cordinate1 - 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                else:
                    if self.Table[cordinate0 - 1][cordinate1 - 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'rd')
        if self.token == 'R': # make the movements of the red dame pieces
            if direction == 'rd':
                if self.Table[cordinate0 + 1][cordinate1 + 1] == '⚫' or self.Table[cordinate0 + 1][cordinate1 + 1] == 'B':
                    if self.Table[cordinate0 + 2][cordinate1 + 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 + 1][cordinate1 + 1] = '⬛'
                        self.Table[cordinate0 + 2][cordinate1 + 2] = self.token
                        return self.eat_recursive((cordinate0 + 2), (cordinate1 + 2), 'rd')
                    if self.Table[cordinate0 + 2][cordinate1 + 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                else:
                    if self.Table[cordinate0 + 1][cordinate1 + 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'ld')
            if direction == 'ld':
                if self.Table[cordinate0 + 1][cordinate1 - 1] == '⚫' or self.Table[cordinate0 + 1][cordinate1 - 1] == 'B':
                    if self.Table[cordinate0 + 2][cordinate1 - 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 + 1][cordinate1 - 1] = '⬛'
                        self.Table[cordinate0 + 2][cordinate1 - 2] = self.token
                        return self.eat_recursive((cordinate0 + 2), (cordinate1 - 2), 'ld')
                    if self.Table[cordinate0 + 2][cordinate1 - 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                else:
                    if self.Table[cordinate0 + 1][cordinate1 - 1] == '⬛':
                        return ''
                    return self.eat_recursive((cordinate0), (cordinate1), 'rd')
        else:
            return '' # for stop the recursive cicle
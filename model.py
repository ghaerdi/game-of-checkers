import random
class Model:
    def __init__(self):
        self.Table = [  # the table for game
            ['1','⬜', '⬛', '⬜', '⚫', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['2','⬛', '⬜', '⬛', '⬜', '⭕', '⬜', '⬛' ,'⬜', '\n'],
            ['3','⬜', '⬛', '⬜', '⚫', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['4','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            ['5','⬜', '⬛', '⬜', '⬛', '⬜', '⚫', '⬜' ,'⬛', '\n'],
            ['6','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            ['7','⬜', '⚫', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['8','⭕', '⬜', '⬛', '⬜', 'B', '⬜', '⬛' ,'⬜', '\n'],
            [' ','A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', '\n']
        ]
        self.generated_table = []
        self.cache = ' '
        self.view = ''
        self.force_eat = None
        self.error = None
        self.turn = random.randint(0, 1)
    def input_instructions(self, instructions):
        try:
            self.tokens_cache = self.Table[instructions[0]][instructions[1]]
            if (self.turn == 0 and self.tokens_cache == '⭕') or (self.turn == 0 and self.tokens_cache == 'R') or (self.turn == 1 and self.tokens_cache == '⚫') or (self.turn == 1 and self.tokens_cache == 'B'):
                self.error = None
                self.force_eat = self.__can_eat(self.tokens_cache)
                if self.force_eat != []:
                    for coordinate in self.force_eat:
                        self.error = None
                        if coordinate[0] == instructions[0] and coordinate[1] == instructions[1]:
                            self.eat_recursive(instructions[0], instructions[1], instructions[4])
                            break
                        else:
                            self.error = 'you need eat in => ' + str((self.traslate_words()))[1:-1]
                else:
                    self.Table[instructions[0]][instructions[1]] = '⬛'
                    if self.tokens_cache == '⭕' and instructions[2] == 0:
                        self.Table[instructions[2]][instructions[3]] = 'R'
                    elif self.tokens_cache == '⚫' and instructions[2] == 7:
                        self.Table[instructions[2]][instructions[3]] = 'B'
                    else:
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
                if self.tokens_cache == '⭕' or self.token == 'R':
                    self.turn = 1
                else:
                    self.turn = 0
            else:
                self.error = 'is not your turn'
            for j in self.Table:
                for i in j:
                    self.generated_table.append(i)
            self.generated_table.insert(0, '')
            self.view = self.cache.join(self.generated_table)
            self.testing = instructions
        except:
            pass
    def traslate_words(self):
        translate = []
        for translate0 in self.force_eat:
            translate.append(self.Table[8][translate0[1]] + self.Table[translate0[0]][0])
        return translate
    def return_error_move(self):
        return self.error
    def return_model_view(self):
        return self.view # return compile table for view
    def return_raw_table(self):
        return self.Table # return raw table for controller
    def return_turn(self):
        return self.turn
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
                    if self.token == 'B':
                        if self.Table[cordinate0 - 1][cordinate1 + 1] == '⭕':
                            return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                    if self.Table[cordinate0 + 1][cordinate1 - 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                    return ''
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
                else:
                    if self.token == 'B':
                        if self.Table[cordinate0 - 1][cordinate1 - 1] == '⭕':
                            return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                    if self.Table[cordinate0 + 1][cordinate1 + 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                    return ''
        if self.token == '⭕' or self.token == 'R': # make the movements of the red pieces
            if direction == 'ru':
                if self.Table[cordinate0 - 1][cordinate1 + 1] == '⚫' or self.Table[cordinate0 - 1][cordinate1 + 1] == 'B':
                    if self.Table[cordinate0 - 2][cordinate1 + 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 + 1] = '⬛'
                        if (cordinate0 - 2) == 0:
                            self.Table[cordinate0 - 2][cordinate1 + 2] = 'R'
                            return ''
                        else:
                            self.Table[cordinate0 - 2][cordinate1 + 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 + 2), 'ru')
                    if self.Table[cordinate0 - 2][cordinate1 + 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                else:
                    if self.token == 'R':
                        if self.Table[cordinate0 + 1][cordinate1 + 1] == '⚫':
                            return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                    if self.Table[cordinate0 - 1][cordinate1 - 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                    return ''
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
                        return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                else:
                    if self.token == 'R':
                        if self.Table[cordinate0 + 1][cordinate1 - 1] == '⚫':
                            return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                    if self.Table[cordinate0 - 1][cordinate1 + 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                    return ''
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
                    if self.Table[cordinate0 + 1][cordinate1 + 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                    if self.Table[cordinate0 - 1][cordinate1 - 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                    return ''
            if direction == 'lu':
                if self.Table[cordinate0 - 1][cordinate1 - 1] == '⭕' or self.Table[cordinate0 - 1][cordinate1 - 1] == 'R':
                    if self.Table[cordinate0 - 2][cordinate1 - 2] == '⬛':
                        self.Table[cordinate0][cordinate1] = '⬛'
                        self.Table[cordinate0 - 1][cordinate1 - 1] = '⬛'
                        self.Table[cordinate0 - 2][cordinate1 - 2] = self.token
                        return self.eat_recursive((cordinate0 - 2), (cordinate1 - 2), 'lu')
                    if self.Table[cordinate0 - 2][cordinate1 - 2] != '⬛':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                else:
                    if self.Table[cordinate0 + 1][cordinate1 - 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                    if self.Table[cordinate0 - 1][cordinate1 + 1] == '⭕':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                    return ''
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
                    if self.Table[cordinate0 - 1][cordinate1 + 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ru')
                    if self.Table[cordinate0 + 1][cordinate1 - 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'ld')
                    return ''
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
                    if self.Table[cordinate0 - 1][cordinate1 - 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'lu')
                    if self.Table[cordinate0 + 1][cordinate1 + 1] == '⚫':
                        return self.eat_recursive((cordinate0), (cordinate1), 'rd')
                    return ''
        else:
            return '' # for stop the recursive cicle
    #                      <----------------------force eat----------------------------------->
    def __can_eat(self, token): # Look if a token must Eat
        tokens_can_eat = []
        try:
            for row_table in range(len(self.Table)):
                for single_piece in range(len(self.Table[row_table])):
                    if token == '⭕' or token == 'R':
                        if self.Table[row_table][single_piece] == '⭕' or self.Table[row_table][single_piece] == 'R':
                            # LEFT UP
                            if self.Table[row_table - 1][single_piece - 1] == '⚫' or self.Table[row_table - 1][single_piece - 1] == 'B':
                                if self.Table[row_table - 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            # RIGHT UP
                            if self.Table[row_table - 1][single_piece + 1] == '⚫' or self.Table[row_table - 1][single_piece + 1] == 'B':
                                if self.Table[row_table - 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                    if token == 'R':
                        if self.Table[row_table][single_piece] == 'R':
                            # LEFT DOWN
                            if self.Table[row_table + 1][single_piece - 1] == '⚫' or self.Table[row_table + 1][single_piece - 1] == 'B':
                                if self.Table[row_table + 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            # RIGHT DOWN
                            if self.Table[row_table + 1][single_piece + 1] == '⚫' or self.Table[row_table + 1][single_piece + 1] == 'B':
                                if self.Table[row_table + 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                    if token == '⚫' or token == 'B':
                        if self.Table[row_table][single_piece] == '⚫' or self.Table[row_table][single_piece] == 'B':
                            # LEFT DOWN
                            if self.Table[row_table + 1][single_piece - 1] == '⭕' or self.Table[row_table + 1][single_piece - 1] == 'R':
                                if self.Table[row_table + 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            # RIGHT DOWN
                            if self.Table[row_table + 1][single_piece + 1] == '⭕' or self.Table[row_table + 1][single_piece + 1] == 'R':
                                if self.Table[row_table + 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                    if token == 'B':
                        if self.Table[row_table][single_piece] == 'B':
                            # LEFT UP
                            if self.Table[row_table - 1][single_piece - 1] == '⭕' or self.Table[row_table - 1][single_piece - 1] == 'R':
                                if self.Table[row_table - 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            # RIGTH UP
                            if self.Table[row_table - 1][single_piece + 1] == '⭕' or self.Table[row_table - 1][single_piece + 1] == 'R':
                                if self.Table[row_table - 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
        except:
            pass
        return tokens_can_eat
import random
class Model:
    def __init__(self):
        self.Table = [  # the table for game
            ['1','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' , 'R', '\n'],
            ['2','⚫', '⬜', '⬛', '⬜', '⬛', '⬜', '⚫' , '⬜', '\n'],
            ['3','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' , 'R', '\n'],
            ['4','⬛', '⬜', '⬛', '⬜', 'R', '⬜', '⬛' ,'⬜', '\n'],
            ['5','⬜', '⬛', '⬜', '⚫', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['6','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            ['7','⬜', '⚫', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['8','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            [' ','a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', '\n']
        ]
        self.generated_table = [] # store the compiled table
        self.cache = ' '
        self.view = '' # store the string view
        self.force_eat = None
        self.error = None # store errors model
        self.turn = random.randint(0, 1) # assign a random number for the start of the game

    def input_instructions(self, instructions): #.
        try:
            self.tokens_cache = self.Table[instructions[0]][instructions[1]]
            if ((self.turn == 0 and self.tokens_cache == '⭕') or
                (self.turn == 0 and self.tokens_cache == 'R') or
                (self.turn == 1 and self.tokens_cache == '⚫') or
                (self.turn == 1 and self.tokens_cache == 'B')):
                self.error = None
                self.force_eat = self.__can_eat(self.tokens_cache)

                if self.force_eat != []: # Look if a token must eat
                    for coordinate in self.force_eat:
                        self.error = None
                        if coordinate[0] == instructions[0] and coordinate[1] == instructions[1]: # Look if instrucctions is same to the position of a token who must eat
                            self.eat_recursive(instructions[0], instructions[1], instructions[4])
                            break # Stop cycle and miss ejecute the else.
                        else:
                            self.error = 'you need eat in => ' + str((self.__traslate_words()))[1:-1] # return where you need to eat

                else: # make a simple move if you don't have to eat
                    self.Table[instructions[0]][instructions[1]] = '⬛'
                    if self.tokens_cache == '⭕' and instructions[2] == 0:
                        # transform the token when it reaches the beginning of the enemy
                        self.Table[instructions[2]][instructions[3]] = 'R'
                    elif self.tokens_cache == '⚫' and instructions[2] == 7:
                        self.Table[instructions[2]][instructions[3]] = 'B'
                    else:
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache

                # Change turn after play
                if self.error == None:
                    if self.tokens_cache == '⭕' or self.tokens_cache == 'R':
                        self.turn = 1
                    else:
                        self.turn = 0
            #  throw error if is not your turn
            else:
                self.error = 'is not your turn'
            #  compile the table to a string
            for row in self.Table:
                for piece in row:
                    self.generated_table.append(piece)
            self.generated_table.insert(0, '')
            self.view = self.cache.join(self.generated_table) # join table
        #  throw error if you try eat in wrong direction
        except:
            self.error = 'try on other direction'

    def __traslate_words(self): # Translate coordiantes for the error 'you need eat'
        translates = []
        for translate in self.force_eat:
            translates.append(self.Table[8][translate[1]] + self.Table[translate[0]][0])
        return translates # return coordinate where you can eat

    def return_error_move(self): # return errors for the view
        return self.error

    def return_model_view(self): # return compile table for view
        return self.view

    def return_raw_table(self): # return raw table for controller
        return self.Table

    def return_turn(self): # return turn for the view
        return self.turn

    def return_render_view(self):# compiler and return table for the firts launch
        for row in self.Table:
            for piece in row:
                self.generated_table.append(piece)
        self.generated_table.insert(0, '')
        self.view = self.cache.join(self.generated_table) # join table
        return self.view

    #  moves and eat recursive
    def eat_recursive(self, coordinate_x, coordinate_y, direction): # generate move and eat enemy tokens
        self.token = self.Table[coordinate_x][coordinate_y] # current token
        if self.token == '⚫' or self.token == 'B':
            # black piece validation
            if direction == 'rd':
                if self.Table[coordinate_x + 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'R':

                    if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x + 1][coordinate_y + 1] = '⬛'
                        if (coordinate_x + 2) == 7 and self.token == '⚫': # transform the token when it reaches the beginning of the enemy
                            self.Table[coordinate_x + 2][coordinate_y + 2] = 'B'
                            return ''
                        else:
                            self.Table[coordinate_x + 2][coordinate_y + 2] = self.token
                        return self.eat_recursive((coordinate_x + 2), (coordinate_y + 2), 'rd') # Call the method again for eat in the same direction
                    # If cant eat in the same direction check for the other direction
                    if self.Table[coordinate_x + 2][coordinate_y + 2] != '⬛':
                        # Check if can eat in ld direction before call the method
                        if self.Table[coordinate_x + 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'R':
                            if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                        else:
                            return '' # Stop the cycle if cant eat

                else:
                    if self.token == 'B': # if token is a dame check for ru moevement
                        if self.Table[coordinate_x - 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'R':
                            if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                    # If a token find anything in the same direction after eat, check if can eat in the other direction, ld
                    if self.Table[coordinate_x + 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'R':
                            if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                    else:
                        return '' # Stop the cycle if cant eat

            if direction == 'ld':
                if self.Table[coordinate_x + 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'R':

                    if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x + 1][coordinate_y - 1] = '⬛'
                        if (coordinate_x + 2) == 7 and self.token == '⚫': # # transform the token when it reaches the beginning of the enemy
                            self.Table[coordinate_x + 2][coordinate_y - 2] = 'B'
                            return ''
                        else:
                            self.Table[coordinate_x + 2][coordinate_y - 2] = self.token
                        return self.eat_recursive((coordinate_x + 2), (coordinate_y - 2), 'ld')

                    if self.Table[coordinate_x + 2][coordinate_y - 2] != '⬛':
                        if self.Table[coordinate_x + 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'R':
                            if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                        return ''

                else:

                    if self.token == 'B':
                        if self.Table[coordinate_x - 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'R':
                            if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                    if self.Table[coordinate_x + 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'R':
                        if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                    return ''

            # red piece validation
        if self.token == '⭕' or self.token == 'R': # make the movements of the red pieces
            if direction == 'ru':

                if self.Table[coordinate_x - 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'B':
                    if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x - 1][coordinate_y + 1] = '⬛'
                        if (coordinate_x - 2) == 0 and self.token == '⭕': # transform the token when it reaches the beginning of the enemy
                            self.Table[coordinate_x - 2][coordinate_y + 2] = 'R'
                            return ''
                        else:
                            self.Table[coordinate_x - 2][coordinate_y + 2] = self.token
                        return self.eat_recursive((coordinate_x - 2), (coordinate_y + 2), 'ru')

                    if self.Table[coordinate_x - 2][coordinate_y + 2] != '⬛':
                        if self.Table[coordinate_x - 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'B':
                            if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                        else:
                            return ''

                else:
                    if self.token == 'R':
                        if self.Table[coordinate_x + 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'B':
                            if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                    if self.Table[coordinate_x - 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'B':
                        if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                    else:
                        return ''

            if direction == 'lu':
                if self.Table[coordinate_x - 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'B':
                    if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x - 1][coordinate_y - 1] = '⬛'
                        if (coordinate_x - 2) == 0 and self.token == '⭕': # if you manage to reach the opposite side he become a dame
                            self.Table[coordinate_x - 2][coordinate_y - 2] = 'R'
                            return ''
                        else:
                            self.Table[coordinate_x - 2][coordinate_y - 2] = self.token
                        return self.eat_recursive((coordinate_x - 2), (coordinate_y - 2), 'lu')

                    if self.Table[coordinate_x - 2][coordinate_y - 2] != '⬛':
                        if self.Table[coordinate_x - 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'B':
                            if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                        else:
                            return ''

                else:
                    if self.token == 'R':
                        if self.Table[coordinate_x + 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'B':
                            if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                    if self.Table[coordinate_x - 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'B':
                        if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                    else:
                        return ''

            #  black dame piece validation
        if self.token == 'B': # make the movements of the black dame pieces
            if direction == 'ru':
                # Dame movement is like normal movemnt but for the opposite direction
                if self.Table[coordinate_x - 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'R':
                    if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x - 1][coordinate_y + 1] = '⬛'
                        self.Table[coordinate_x - 2][coordinate_y + 2] = self.token
                        return self.eat_recursive((coordinate_x - 2), (coordinate_y + 2), 'ru')

                    if self.Table[coordinate_x - 2][coordinate_y + 2] != '⬛':
                        if self.Table[coordinate_x - 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'R':
                            if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                    else:
                        return ''

                else:
                    if self.Table[coordinate_x + 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'R':
                        if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                    if self.Table[coordinate_x - 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'R':
                        if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                        else:
                            return ''

            if direction == 'lu':
                if self.Table[coordinate_x - 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'R':

                    if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x - 1][coordinate_y - 1] = '⬛'
                        self.Table[coordinate_x - 2][coordinate_y - 2] = self.token
                        return self.eat_recursive((coordinate_x - 2), (coordinate_y - 2), 'lu')

                    if self.Table[coordinate_x - 2][coordinate_y - 2] != '⬛':
                        if self.Table[coordinate_x - 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'R':
                            if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                        else:
                            return ''

                else:
                    if self.Table[coordinate_x + 1][coordinate_y - 1] == '⭕' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'R':
                        if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                    if self.Table[coordinate_x - 1][coordinate_y + 1] == '⭕' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'R':
                        if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                    else:
                        return ''

            # red dame piece validation
        if self.token == 'R': # make the movements of the red dame pieces

            if direction == 'rd':
                if self.Table[coordinate_x + 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'B':
                    if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x + 1][coordinate_y + 1] = '⬛'
                        self.Table[coordinate_x + 2][coordinate_y + 2] = self.token
                        return self.eat_recursive((coordinate_x + 2), (coordinate_y + 2), 'rd')

                    if self.Table[coordinate_x + 2][coordinate_y + 2] != '⬛':
                        if self.Table[coordinate_x + 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'B':
                            if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                        else:
                            return ''

                else:
                    if self.Table[coordinate_x - 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y + 1] == 'B':
                        if self.Table[coordinate_x - 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'ru')
                    if self.Table[coordinate_x + 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'B':
                        if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'ld')
                    else:
                        return ''

            if direction == 'ld':

                if self.Table[coordinate_x + 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y - 1] == 'B':
                    if self.Table[coordinate_x + 2][coordinate_y - 2] == '⬛':
                        self.Table[coordinate_x][coordinate_y] = '⬛'
                        self.Table[coordinate_x + 1][coordinate_y - 1] = '⬛'
                        self.Table[coordinate_x + 2][coordinate_y - 2] = self.token
                        return self.eat_recursive((coordinate_x + 2), (coordinate_y - 2), 'ld')

                    if self.Table[coordinate_x + 2][coordinate_y - 2] != '⬛':
                        if self.Table[coordinate_x + 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'B':
                            if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                                return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                        else:
                            return ''

                else:
                    if self.Table[coordinate_x - 1][coordinate_y - 1] == '⚫' or self.Table[coordinate_x - 1][coordinate_y - 1] == 'B':
                        if self.Table[coordinate_x - 2][coordinate_y - 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'lu')
                    if self.Table[coordinate_x + 1][coordinate_y + 1] == '⚫' or self.Table[coordinate_x + 1][coordinate_y + 1] == 'B':
                        if self.Table[coordinate_x + 2][coordinate_y + 2] == '⬛':
                            return self.eat_recursive((coordinate_x), (coordinate_y), 'rd')
                    else:
                        return ''
        else:
            return '' # for stop the recursive cycle

    # force eat
    def __can_eat(self, token): # Look if a token must Eat
        tokens_can_eat = [] # Array for save tokens position
        try:
            for row_table in range(len(self.Table)):
                for single_piece in range(len(self.Table[row_table])):

                    if token == '⭕' or token == 'R':
                        if self.Table[row_table][single_piece] == '⭕' or self.Table[row_table][single_piece] == 'R':
                            # Look if in lu find a enemy token
                            if self.Table[row_table - 1][single_piece - 1] == '⚫' or self.Table[row_table - 1][single_piece - 1] == 'B':
                                if self.Table[row_table - 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece]) # Save the position of the token who must eat
                            # Look if in ru find a enemy token
                            if self.Table[row_table - 1][single_piece + 1] == '⚫' or self.Table[row_table - 1][single_piece + 1] == 'B':
                                if self.Table[row_table - 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece]) # Save the position of the token who must eat

                    if token == 'R':

                        if self.Table[row_table][single_piece] == 'R':
                            if self.Table[row_table + 1][single_piece - 1] == '⚫' or self.Table[row_table + 1][single_piece - 1] == 'B':
                                if self.Table[row_table + 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            if self.Table[row_table + 1][single_piece + 1] == '⚫' or self.Table[row_table + 1][single_piece + 1] == 'B':
                                if self.Table[row_table + 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])

                    if token == '⚫' or token == 'B':

                        if self.Table[row_table][single_piece] == '⚫' or self.Table[row_table][single_piece] == 'B':
                            if self.Table[row_table + 1][single_piece - 1] == '⭕' or self.Table[row_table + 1][single_piece - 1] == 'R':
                                if self.Table[row_table + 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            if self.Table[row_table + 1][single_piece + 1] == '⭕' or self.Table[row_table + 1][single_piece + 1] == 'R':
                                if self.Table[row_table + 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])

                    if token == 'B':

                        if self.Table[row_table][single_piece] == 'B':
                            if self.Table[row_table - 1][single_piece - 1] == '⭕' or self.Table[row_table - 1][single_piece - 1] == 'R':
                                if self.Table[row_table - 2][single_piece - 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])
                            if self.Table[row_table - 1][single_piece + 1] == '⭕' or self.Table[row_table - 1][single_piece + 1] == 'R':
                                if self.Table[row_table - 2][single_piece + 2] == '⬛':
                                    tokens_can_eat.append([row_table, single_piece])

        except:
            pass
        return tokens_can_eat # return all the tokens position who must eat
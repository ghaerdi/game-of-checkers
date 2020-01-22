class Controller:
    def __init__(self):
        self.table = None
        self.position_token_x = None
        self.position_token_y = None
        self.direction = None
        self.token = None
    def get_table(self, table): # Get the table
        self.table = table
    def __token_to_move(self, position_token_x, position_token_y, direction): # Select a token whit the actual position
        self.position_token_x = int(position_token_x)
        self.position_token_y = int(position_token_y)
        self.direction = direction.lower()
    def move_token(self):
        self.__token_to_move(input(': '), input(': '), input('direction: '))
        if self.__valid_to_move():
            if self.table[self.position_token_x][self.position_token_y] == '⚫' and self.next_not_block(self.direction):
                if self.direction == 'l':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y - 1)
                elif self.direction == 'r':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y + 1)
            if self.table[self.position_token_x][self.position_token_y] == '⭕':
                return 'tested', self.table[self.position_token_x][self.position_token_y]
                if self.direction == 'l':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y - 1)
                elif self.direction == 'r':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y + 1)
    def next_not_block(self, direction):
        return self.__if_token_is_black(self.table[self.position_token_x][self.position_token_y], direction)
        # this is for red token move
        # if self.table[self.position_token_x][self.position_token_y] == '⭕':
        #     if direction == 'r':
        #         move = self.table[self.position_token_x - 1][self.position_token_y + 1]
        #         if move == '⬛':
        #             return True
        #         if move == '⭕':
        #             return False
        #         if move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
        #             return True
        #         if move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y + 2] != '⬛':
        #             return False
        #     if direction == 'l':
        #         move = self.table[self.position_token_x - 1][self.position_token_y - 1]
        #         if move == '⬛':
        #             return True
        #         if move == '⭕':
        #             return False
        #         if move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
        #             return True
        #         if move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
        #             return False
    def __if_token_is_black(self, color_token, direction):
        if color_token == '⚫':
            if direction == 'r':
                move = self.table[self.position_token_x + 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⚫':
                    return False
                elif move == '⭕' and self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                    return True
                elif move == '⭕' and self.table[self.position_token_x + 2][self.position_token_y + 2] != '⬛':
                    return False
            elif direction == 'l':
                move = self.table[self.position_token_x + 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                elif move == '⚫':
                    return False
                elif move == '⭕' and self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                    return True
                elif move == '⭕' and self.table[self.position_token_x + 2][self.position_token_y - 2] != '⬛':
                    return False
    def __if_token_is_red(self, color_token, direction):
        # if color_token == '⭕':
        #     if direction = 'r':
        #         move = self.table[self.position_token_x + 1][self.position_token_y + 1]
        pass
    def __valid_to_move(self):
        if self.table[self.position_token_x][self.position_token_y] == '⬜' or self.table[self.position_token_x][self.position_token_y] == '⬛':
            return False
        else:
            return True
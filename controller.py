class Controller:
    def __init__(self):
        self.table = None
        self.position_token_x = None
        self.position_token_y = None
        self.direction = None
        self.token = None
    def get_table(self, table): # Get the table
        self.table = table
    def move_token(self):
        self.__token_to_move(input('Coordinate: '), input('Direction: '))
        if self.__valid_to_move():
            if self.table[self.position_token_x][self.position_token_y] == '⚫' and self.next_not_block(self.direction):
                if self.direction == 'l':
                    if self.table[self.position_token_x + 1][self.position_token_y - 1] == '⭕' and self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                        return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y - 2), 'l'
                    else:
                        return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y - 1)
                elif self.direction == 'r':
                    if self.table[self.position_token_x + 1][self.position_token_y + 1] == '⭕' and self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                        return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y + 2), 'r'
                    else:
                        return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y + 1)
            if self.table[self.position_token_x][self.position_token_y] == '⭕' and self.next_not_block(self.direction):
                if self.direction == 'l':
                    if self.table[self.position_token_x - 1][self.position_token_y - 1] == '⚫' and self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                        return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y - 2), 'l'
                    else:
                        return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y - 1)
                elif self.direction == 'r':
                    if self.table[self.position_token_x - 1][self.position_token_y + 1] == '⚫' and self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                        return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y + 2), 'r'
                    else:
                        return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y + 1)
    def next_not_block(self, direction):
        if self.table[self.position_token_x][self.position_token_y] == '⚫':
            return self.__if_token_is_black(self.table[self.position_token_x][self.position_token_y], direction)
        elif self.table[self.position_token_x][self.position_token_y] == '⭕':
            return self.__if_token_is_red(self.table[self.position_token_x][self.position_token_y], direction)
        else:
            print('error: -> no pass next not block')
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
        if color_token == '⭕':
            if direction == 'r':
                move = self.table[self.position_token_x - 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⭕':
                    return False
                elif move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                    return True
                elif move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y + 2] != '⬛':
                    return False
            elif direction == 'l':
                move = self.table[self.position_token_x - 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                if self.table[self.position_token_x - 1][self.position_token_y - 1] == '5':
                    return False
                elif move == '⭕':
                    return False
                elif move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                    return True
                elif move == '⚫' and self.table[self.position_token_x - 2][self.position_token_y - 2] != '⬛':
                    return False
    def __valid_to_move(self):
        if self.table[self.position_token_x][self.position_token_y] == '⬜' or self.table[self.position_token_x][self.position_token_y] == '⬛':
            return False
        else:
            return True
    def __token_to_move(self, input_coordinate, direction): # Select a token whit the actual position
        self.input_coordinate = input_coordinate.upper()
        self.direction = direction.lower()
        # Table of coordinates
        abc, table_coordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], []
        for i in range(1, 9):
            for l in abc:
                table_coordinates.append(l + str(i))
        # Checking input and coordinates
        coordinate_x = 0
        coordinate_y = 1
        for all_coordinates in table_coordinates:
            if input_coordinate == all_coordinates:
                self.position_token_x = coordinate_x
                self.position_token_y = coordinate_y
            else:
                if coordinate_y < 8:
                    coordinate_y = coordinate_y + 1
                else:
                    coordinate_y = 1
                    coordinate_x = coordinate_x + 1
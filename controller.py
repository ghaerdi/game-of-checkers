class Controller:
    def __init__(self):
        self.table = None
        self.position_token_x = None
        self.position_token_y = None
        self.direction = None
        self.token = None
        self.error = []
    def handle_error(self):
        return self.error[-1]
    def get_table(self, table): # Get the table
        self.table = table
    def move_token(self):
        self.__token_to_move(input('Coordinate: '), input('Direction: '))
        if self.__valid_to_move():
            self.error.append('')
            if self.table[self.position_token_x][self.position_token_y] == '⚫' and self.next_not_block(self.direction):
                return self.__instructions_black_for_model(self.direction)
            if self.table[self.position_token_x][self.position_token_y] == '⭕' and self.next_not_block(self.direction):
                return self.__instructions_red_for_model(self.direction)
            if self.table[self.position_token_x][self.position_token_y] == 'B' and self.next_not_block(self.direction):
                return self.__instructions_black_dame_for_model(self.direction)
            if self.table[self.position_token_x][self.position_token_y] == 'R' and self.next_not_block(self.direction):
                return self.__instructions_red_dame_for_model(self.direction)
            else:
                self.error.append('No valid move')
        else:
            self.error.append('Invalid token')
    def next_not_block(self, direction):
        if self.table[self.position_token_x][self.position_token_y] == '⚫' or self.table[self.position_token_x][self.position_token_y] == 'B':
            return self.__if_valid(self.table[self.position_token_x][self.position_token_y], direction)
        elif self.table[self.position_token_x][self.position_token_y] == '⭕' or self.table[self.position_token_x][self.position_token_y] == 'R':
            return self.__if_valid(self.table[self.position_token_x][self.position_token_y], direction)
        else:
            return False
    def __if_valid(self, token, direction):
        if token == '⚫' or token == 'B':
            if direction == 'rd':
                move = self.table[self.position_token_x + 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⚫' or move == 'B':
                    return False
                elif move == '⭕' or move == 'R':
                    if self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                        return True
                else:
                    return False
            elif direction == 'ld':
                move = self.table[self.position_token_x + 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                elif move == '⚫' or move == 'B':
                    return False
                elif move == '⭕' or move == 'R':
                    if self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                        return True
                else:
                    return False
        if token == '⭕' or token == 'R':
            if direction == 'ru':
                move = self.table[self.position_token_x - 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⭕' or move == 'R':
                    return False
                elif move == '⚫' or move == 'B':
                    if self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                        return True
                else:
                    return False
            elif direction == 'lu':
                move = self.table[self.position_token_x - 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                elif move == '⭕' or move == 'R':
                    return False
                elif move == '⚫' or move == 'B':
                    if self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                        return True
                else:
                    return False
        if token == 'B':
            if direction == 'ru':
                move = self.table[self.position_token_x - 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⚫' or move == 'B':
                    return False
                elif move == '⭕' or move == 'R':
                    if self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                        return True
                else:
                    return False
            elif direction == 'lu':
                move = self.table[self.position_token_x - 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                elif move == '⚫' or move == 'B':
                    return False
                elif move == '⭕' or move == 'R':
                    if self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                        return True
                else:
                    return True
        if token == 'R':
            if direction == 'rd':
                move = self.table[self.position_token_x + 1][self.position_token_y + 1]
                if move == '⬛':
                    return True
                elif move == '⭕' or move == 'R':
                    return False
                elif move == '⚫' or move == 'B':
                    if self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                        return True
                else:
                    return False
            elif direction == 'ld':
                move = self.table[self.position_token_x + 1][self.position_token_y - 1]
                if move == '⬛':
                    return True
                elif move == '⭕' or move == 'R':
                    return False
                elif move == '⚫' or move == 'B':
                    if self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                        return True
                else:
                    return False
    def __valid_to_move(self):
        if self.table[self.position_token_x][self.position_token_y] != '⬜' and self.table[self.position_token_x][self.position_token_y] != '⬛':
            return True
        else:
            return False
    def __token_to_move(self, input_coordinate, direction): # Select a token whit the actual position
        self.input_coordinate = input_coordinate[0].upper() + input_coordinate[1]
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
    def __instructions_black_for_model(self, direction):
        if direction == 'ld':
            if self.table[self.position_token_x + 1][self.position_token_y - 1] == '⭕' or self.table[self.position_token_x + 1][self.position_token_y - 1] == 'R':
                if self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y - 2), 'ld'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y - 1)
        elif direction == 'rd':
            if self.table[self.position_token_x + 1][self.position_token_y + 1] == '⭕' or self.table[self.position_token_x + 1][self.position_token_y + 1] == 'R':
                if self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y + 2), 'rd'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y + 1)
        elif direction == 'ru' and self.table[self.position_token_x][self.position_token_y] == 'B':
            if self.table[self.position_token_x - 1][self.position_token_y + 1] == '⭕' or self.table[self.position_token_x - 1][self.position_token_y + 1] == 'R':
                if self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y + 2), 'ru'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y + 1)
        elif direction == 'lu' and self.table[self.position_token_x][self.position_token_y] == 'B':
            if self.table[self.position_token_x - 1][self.position_token_y - 1] == '⭕' or self.table[self.position_token_x - 1][self.position_token_y - 1] == 'R':
                if self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y - 2), 'lu'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y - 1)
    def __instructions_red_for_model(self, direction):
        if direction == 'lu':
            if self.table[self.position_token_x - 1][self.position_token_y - 1] == '⚫' or self.table[self.position_token_x - 1][self.position_token_y - 1] == 'B':
                if self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y - 2), 'lu'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y - 1)
        elif direction == 'ru':
            if self.table[self.position_token_x - 1][self.position_token_y + 1] == '⚫' or self.table[self.position_token_x - 1][self.position_token_y + 1] == 'B':
                if self.table[self.position_token_x - 2][self.position_token_y + 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y + 2), 'ru'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x - 1), (self.position_token_y + 1)
        elif direction == 'rd' and self.table[self.position_token_x][self.position_token_y] == 'R':
            if self.table[self.position_token_x + 1][self.position_token_y + 1] == '⚫' or self.table[self.position_token_x + 1][self.position_token_y + 1] == 'B':
                if self.table[self.position_token_x + 2][self.position_token_y + 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y + 2), 'rd'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y + 1)
        elif direction == 'ld' and self.table[self.position_token_x][self.position_token_y] == 'R':
            if self.table[self.position_token_x + 1][self.position_token_y - 1] == '⚫' or self.table[self.position_token_x + 1][self.position_token_y - 1] == 'B':
                if self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y - 2), 'ld'
            else:
                return self.position_token_x, self.position_token_y, (self.position_token_x + 1), (self.position_token_y - 1)
    def __instructions_black_dame_for_model(self, direction):
        return self.__instructions_black_for_model(direction)
    def __instructions_red_dame_for_model(self, direction):
        return self.__instructions_red_for_model(direction)
#                      <----------------------force eat----------------------------------->
    def can_eat(self, token): # Look if a token must Eat
        for row_table in range(len(self.table)):
            for single_piece in range(len(self.table[row_table])):
                try:
                    if token == '⭕' or token == 'R':
                        if self.table[row_table][single_piece] == '⭕' or self.table[row_table][single_piece] == 'R':
                            # LEFT UP
                            if self.table[row_table - 1][single_piece - 1] == '⚫' or self.table[row_table - 1][single_piece - 1] == 'B':
                                if self.table[row_table - 2][single_piece - 2] == '⬛':
                                    return row_table, single_piece
                            # RIGHT UP
                            if self.table[row_table - 1][single_piece + 1] == '⚫' or self.table[row_table - 1][single_piece + 1] == 'B':
                                if self.table[row_table - 2][single_piece + 2] == '⬛':
                                    return row_table, single_piece
                    if token == 'R':
                        if self.table[row_table][single_piece] == 'R':
                            # LEFT DOWN
                            if self.table[row_table + 1][single_piece - 1] == '⚫' or self.table[row_table + 1][single_piece - 1] == 'B':
                                if self.table[row_table + 2][single_piece - 2] == '⬛':
                                    return row_table, single_piece
                            # RIGHT DOWN
                            if self.table[row_table + 1][single_piece + 1] == '⚫' or self.table[row_table + 1][single_piece + 1] == 'B':
                                if self.table[row_table + 2][single_piece + 2] == '⬛':
                                    return row_table, single_piece
                    if token == '⚫' or token == 'B':
                        if self.table[row_table][single_piece] == '⚫' or self.table[row_table][single_piece] == 'B':
                            # LEFT DOWN
                            if self.table[row_table + 1][single_piece - 1] == '⭕' or self.table[row_table + 1][single_piece - 1] == 'R':
                                if self.table[row_table + 2][single_piece - 2] == '⬛':
                                    return row_table, single_piece
                            # RIGHT DOWN
                            if self.table[row_table + 1][single_piece + 1] == '⭕' or self.table[row_table + 1][single_piece + 1] == 'R':
                                if self.table[row_table + 2][single_piece + 2] == '⬛':
                                    return row_table, single_piece
                    if token == 'B':
                        if self.table[row_table][single_piece] == 'B':
                            # LEFT UP
                            if self.table[row_table - 1][single_piece - 1] == '⭕' or self.table[row_table - 1][single_piece - 1] == 'R':
                                if self.table[row_table - 2][single_piece - 2] == '⬛':
                                    return row_table, single_piece
                            # RIGTH UP
                            if self.table[row_table - 1][single_piece + 1] == '⭕' or self.table[row_table - 1][single_piece + 1] == 'R':
                                if self.table[row_table - 2][single_piece + 2] == '⬛':
                                    return row_table, single_piece
                except:
                    pass
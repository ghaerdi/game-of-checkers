class Controller:
    def __init__(self):
        self.position_token_x = None
        self.position_token_y = None
        self.direction = None

    def get_table(self, table): # Get the table
        self.table = table

    def move_token(self): # return instructions for model
        self.__token_to_move(input('Coordinate: '), input('Direction: ')) # get the movements and directions
        if self.__valid_to_move():
            self.error = None

            if self.table[self.position_token_x][self.position_token_y] == '⚫' and self.__next_not_block(self.direction):
                return self.__instructions_black_for_model(self.direction)

            if self.table[self.position_token_x][self.position_token_y] == '⭕' and self.__next_not_block(self.direction):
                return self.__instructions_red_for_model(self.direction)

            if self.table[self.position_token_x][self.position_token_y] == 'B' and self.__next_not_block(self.direction):
                return self.__instructions_black_dame_for_model(self.direction)

            if self.table[self.position_token_x][self.position_token_y] == 'R' and self.__next_not_block(self.direction):
                return self.__instructions_red_dame_for_model(self.direction)
            # if you try to move in a wrong direction return error
            else:
                self.error = 'the move you are trying to make is not valid' # returns error if you move is not valid
            # if you try to move a wrong token return error
        else:
            self.error = 'the piece you are trying to move is not valid' # returns error if you try move a invalid piece

    def handle_error(self): # return all errors
        return self.error

    def __next_not_block(self, direction): # its valid if you move, and it's not blocked
        if self.table[self.position_token_x][self.position_token_y] == '⚫' or self.table[self.position_token_x][self.position_token_y] == 'B':
            return self.__if_valid(self.table[self.position_token_x][self.position_token_y], direction)

        elif self.table[self.position_token_x][self.position_token_y] == '⭕' or self.table[self.position_token_x][self.position_token_y] == 'R':
            return self.__if_valid(self.table[self.position_token_x][self.position_token_y], direction)

        else:
            return False

    def __if_valid(self, token, direction): # returns True or False if your move is valid in each case
        if token == '⚫' or token == 'B':

            if direction == 'rd' or direction =='ld':
                return self.__if_valid_black(direction)
            else:
                return self.__if_valid_black_dame(direction)

        if token == '⭕' or token == 'R':

            if direction == 'ru' or direction == 'lu':
                return self.__if_valid_red(direction)
            else:
                return self.__if_valid_red_dame(direction)

    def __if_valid_black(self, direction): # ask if you black token can move in that direction
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

    def __if_valid_black_dame(self,direction): # ask if you black dame token can move in that direction
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

    def __if_valid_red(self, direction): # ask if you red token can move in that direction
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

    def __if_valid_red_dame(self, direction): # ask if you red dame token can move in that direction
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

    def __valid_to_move(self): # ask if your token is valid to move
        try:
            if self.table[self.position_token_x][self.position_token_y] != '⬜' and self.table[self.position_token_x][self.position_token_y] != '⬛':
                return True
            else:
                return False

        except:
            return False

    def __token_to_move(self, input_coordinate, direction):
        try:
            faild = int(input_coordinate[1]) # if failed is for a wrong coordinate
            input_coordinate = input_coordinate[0].upper() + input_coordinate[1]
            self.direction = direction.lower()
            # Table of coordinates
            abc, table_coordinates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], []

            # This bucle generate all coordinates (A1, A2, A3...)
            for numbers in range(1, 9):
                for letters in abc:
                    table_coordinates.append(letters + str(numbers))
            # This bucle translate all coordiantes whit the matrix/array coordiantes. So the game understand the user inputs.
            coordinate_x = 0
            coordinate_y = 1
            for coordinate in table_coordinates:
                if input_coordinate == coordinate:
                    self.position_token_x = coordinate_x
                    self.position_token_y = coordinate_y

                else:
                    if coordinate_y < 8:
                        coordinate_y = coordinate_y + 1
                    else:
                        coordinate_y = 1
                        coordinate_x = coordinate_x + 1

        except:
            pass

    def __instructions_black_for_model(self, direction): # resturns instruction for eat
        if direction == 'ld':
            # if token can eat returns instruction for each case
            if self.table[self.position_token_x + 1][self.position_token_y - 1] == '⭕' or self.table[self.position_token_x + 1][self.position_token_y - 1] == 'R':
                if self.table[self.position_token_x + 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x + 2), (self.position_token_y - 2), 'ld'
                # returns single intruction for single move
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

    def __instructions_red_for_model(self, direction): # resturns instruction for eat
        if direction == 'lu':
            # if token can eat returns instruction for each case
            if self.table[self.position_token_x - 1][self.position_token_y - 1] == '⚫' or self.table[self.position_token_x - 1][self.position_token_y - 1] == 'B':
                if self.table[self.position_token_x - 2][self.position_token_y - 2] == '⬛':
                    return self.position_token_x, self.position_token_y, (self.position_token_x - 2), (self.position_token_y - 2), 'lu'
                # returns single intruction for single move
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

    def __instructions_black_dame_for_model(self, direction): # returns black dame's instruction
        return self.__instructions_black_for_model(direction)

    def __instructions_red_dame_for_model(self, direction): # returns black dame's instruction
        return self.__instructions_red_for_model(direction)
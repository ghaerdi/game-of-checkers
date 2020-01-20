class Controller:
    def token(self, token, color, canEat = False, dame = False, empty = None): # 'Create' token
        self.token = token
        self.color = color
        self.canEat = canEat
        self.dame = dame
        self.empty = empty
    def take_token(self, position_initial_x, position_initial_y): # Select a token whit the actual position
        self.position_initial_x = position_initial_x
        self.position_initial_y = position_initial_y
    def is_dame(self): # If a token get the other side of the table becomes a dame
        if self.position_initial_y == 0:
            self.dame = True
    def left_up_diagonal_move(self): # Move forward diagonal left
        self.position_initial_x = self.position_inital_x - 1
        self.position_initial_y = self.position_initial_y - 1
    def rigth_up_diagonal_move(self): # Move forward diagonal rigth
        self.position_initial_x = self.position_initial_x + 1
        self.position_initial_y = self.position_initial_y - 1
    def left_down_diagonal_move(self): # Move backward diagonal left
        if self.dame == True:
            self.position_initial_x = self.position_initial_x - 1
            self.position_initial_y = self.position_initial_y + 1
    def right_down_diagonal_move(self): # Move backward diagonal rigth
        if self.dame == True:
            self.position_initial_x = self.position_initial_x + 1
            self.position_initial_y = self.position_initial_y + 1


# class Controller:
#     def __init__(self):
#         self.cord_x1 = None
#         self.cord_y1 = None
#         self.cord_x2 = None
#         self.cord_y2 = None
#         self.view = None
#         self.table = None
#         self.token = None
#     def get_moves_player(self, cord_x1 = 0, cord_y1 = 0, cord_x2 = 0, cord_y2 = 0):
#         self.cord_x1 = cord_x1
#         self.cord_x2 = cord_x2
#         self.cord_y1 = cord_y1
#         self.cord_y2 = cord_y2
#     def get_tokens(self, table):
#         self.table = table
#     def return_moves(self):
#         return self.cord_x1, self.cord_y1, self.cord_x2, self.cord_y2
#     def return_render_view(self):
#         return self.view
#     def get_view_to_render(self, view):
#         self.view = view
#     def move_diagonal_up_left(self):
#         pass
class Controller:
    def __init__(self):
        self.cord_x1 = None
        self.cord_y1 = None
        self.cord_x2 = None
        self.cord_y2 = None
        self.view = None
        self.table = None
        self.token = None
    def get_moves_player(self, cord_x1 = 0, cord_y1 = 0, cord_x2 = 0, cord_y2 = 0):
        self.cord_x1 = cord_x1
        self.cord_x2 = cord_x2
        self.cord_y1 = cord_y1
        self.cord_y2 = cord_y2
    def get_tokens(self, table):
        self.table = table
    def return_moves(self):
        return self.cord_x1, self.cord_y1, self.cord_x2, self.cord_y2
    def return_render_view(self):
        return self.view
    def get_view_to_render(self, view):
        self.view = view
    def move_diagonal_up_left(self):
        pass

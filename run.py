import os
import time
from controller import Controller
from model import Model
from view import View
class Game():
    def __init__(self):
        self.start = True
    def start_game(self):
        new_controller = Controller()
        new_model = Model()
        new_view = View(new_model.return_render_view())
        new_view.start_render_view(new_model.return_turn())
        while True:
            new_view.print_turn(new_model.return_turn())
            new_controller.get_table(new_model.return_raw_table())
            new_model.input_instructions(new_controller.move_token())
            new_view.render_view(new_model.return_model_view(), new_controller.handle_error(), new_model.return_error_move())
            if new_view.consult_dead_token() == 'black':
                time.sleep(1.5)
                os.system('clear')
                print('Black Win!!!')
                time.sleep(3)
                os.system('clear')
                break
            if new_view.consult_dead_token() == 'red':
                time.sleep(1.5)
                os.system('clear')
                print('Red Win!!!')
                time.sleep(3)
                os.system('clear')
                break
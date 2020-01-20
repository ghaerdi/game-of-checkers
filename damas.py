from controller import Controller
from model import Model
from view import View
import time
new_controller = Controller()
new_model = Model()
new_view = View()

for i in range(10):
    new_controller.get_moves_player(int(input('x1: ')), int(input('y1: ')), int(input('x2: ')), int(input('y2: ')))
    new_model.input_instructions(new_controller.return_moves())
    new_view.render_view(new_model.return_model_view())

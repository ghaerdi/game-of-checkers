from controller import Controller
from model import Model
from view import View
import time
new_controller = Controller()
new_model = Model()
new_view = View(new_model.return_render_view())
new_view.start_render_view()
for i in range(15):
    new_controller.get_table(new_model.return_raw_table())
    new_model.input_instructions(new_controller.move_token())
    new_view.render_view(new_model.return_model_view())
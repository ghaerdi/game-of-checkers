from controller import Controller
from model import Model
from view import View
new_controller = Controller()
new_model = Model()
new_view = View(new_model.return_render_view())
new_view.start_render_view(new_model.return_turn())

true = [1]
for i in true:
    true.append(1)
    new_controller.get_table(new_model.return_raw_table())
    new_model.input_instructions(new_controller.move_token())
    new_view.render_view(new_model.return_model_view(), new_controller.handle_error(), new_model.return_error_move())
    print(new_view.consult_dead_token())
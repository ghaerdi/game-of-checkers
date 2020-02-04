def search(cordenadas1, cordenadas2, direction):
    try:
        cordenadas1, cordenadas2 = int(cordenadas1), int(cordenadas2)
        stade = ((cordenadas1 <= 7) and (cordenadas1 >= 0)) and (((cordenadas2 <= 8) and (cordenadas2 >= 1)) and (cordenadas2 != 0))
        if stade:
            if direction == 'l':
                print(cordenadas1, cordenadas2)
                return cordenadas1, cordenadas2, search(cordenadas1 + 1, cordenadas2 - 1, 'r')
            if direction == 'r':
                print(cordenadas1, cordenadas2)
                return cordenadas1, cordenadas2, search(cordenadas1 + 1, cordenadas2 + 1, 'l')
        if not stade:
            print('no valid move')
            return cordenadas1, cordenadas2
            search(int(input(': ')), int(input(': ')), input('direction: '))
    except:
        print('no valid insert a number')
        return search(int(input(': ')), int(input(': ')), input('direction: ')), cordenadas1, cordenadas2
from controller import Controller
from model2 import Model
from view import View
new_controller = Controller()
new_model = Model()
new_view = View(new_model.return_render_view())
new_view.start_render_view('Black token')


def turnos():
    step = 2
    while True:
        if step == 1:
            new_controller.get_table(new_model.return_raw_table())
            new_model.input_instructions(new_controller.move_token())
            new_view.render_view(new_model.return_model_view(), 'Black token')
            step += 1
        if step == 2:
            new_controller.get_table(new_model.return_raw_table())
            new_model.input_instructions(new_controller.move_token())
            new_view.render_view(new_model.return_model_view(), 'Red token')
            step -= 1

turnos()
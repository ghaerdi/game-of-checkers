class Model:
    def __init__(self):
        self.Table = [
            ['1','⬜', '⚫', '⬜', '⚫', '⬜', '⚫', '⬜' ,'⚫', '\n'],
            ['2','⚫', '⬜', '⚫', '⬜', '⚫', '⬜', '⚫' ,'⬜', '\n'],
            ['3','⬜', '⚫', '⬜', '⚫', '⬜', '⚫', '⬜' ,'⚫', '\n'],
            ['4','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            ['5','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['6','⭕', '⬜', '⭕', '⬜', '⭕', '⬜', '⭕' ,'⬜', '\n'],
            ['7','⬜', '⭕', '⬜', '⭕', '⬜', '⭕', '⬜' ,'⭕', '\n'],
            ['8','⭕', '⬜', '⭕', '⬜', '⭕', '⬜', '⭕' ,'⬜', '\n'],
            ['',' ','A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', '\n']
        ]
        self.generated_table = []
        self.cache = ' '
        self.view = ''
    def input_instructions(self, controller_instructions):
        self.tokens_cache = self.Table[controller_instructions[0]][controller_instructions[1]]
        if self.tokens_cache == '⚪':
            self.Table[controller_instructions[0]][controller_instructions[1]] = '⬜'
            self.Table[controller_instructions[2]][controller_instructions[3]] = self.tokens_cache
        for j in self.Table:
            for i in j:
                self.generated_table.append(i)
        self.generated_table.insert(0, '')
        self.view = self.cache.join(self.generated_table)
    def return_model_view(self):
        return self.view
    def return_raw_table(self):
        return self.Table
    def render_table(self):
        print(len(self.view))
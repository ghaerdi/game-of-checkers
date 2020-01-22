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
        self.testing = None
    def input_instructions(self, instructions):
        print(instructions)
        try:
            self.tokens_cache = self.Table[instructions[0]][instructions[1]]
            if self.tokens_cache != '⬛' or self.tokens_cache != '⬜':
            # <-------------------------------------------------->
                if len(instructions) == 5:
                    if self.tokens_cache == '⚫':
                        if instructions[4] == 'r':
                            if self.Table[instructions[0] + 1][instructions[1] + 1] == '⭕' and self.Table[instructions[0] + 2][instructions[1] + 2] == '⬛':
                                self.Table[instructions[0]][instructions[1]] = '⬛'
                                self.Table[instructions[0] + 1][instructions[1] + 1] = '⬛'
                                self.Table[instructions[2]][instructions[3]] = self.tokens_cache
                        if instructions[4] == 'l':
                            if self.Table[instructions[0] + 1][instructions[1] - 1] == '⭕' and self.Table[instructions[0] + 2][instructions[1] - 2] == '⬛':
                                self.Table[instructions[0]][instructions[1]] = '⬛'
                                self.Table[instructions[0] + 1][instructions[1] - 1] = '⬛'
                                self.Table[instructions[2]][instructions[3]] = self.tokens_cache
                    if self.tokens_cache == '⭕':
                        print('input here')
                        if instructions[4] == 'r':
                            if self.Table[instructions[0] - 1][instructions[1] + 1] == '⚫' and self.Table[instructions[0] - 2][instructions[1] + 2] == '⬛':
                                self.Table[instructions[0]][instructions[1]] = '⬛'
                                self.Table[instructions[0] - 1][instructions[1] + 1] = '⬛'
                                self.Table[instructions[2]][instructions[3]] = self.tokens_cache
                        if instructions[4] == 'l':
                            if self.Table[instructions[0] - 1][instructions[1] - 1] == '⚫' and self.Table[instructions[0] - 2][instructions[1] - 2] == '⬛':
                                self.Table[instructions[0]][instructions[1]] = '⬛'
                                self.Table[instructions[0] - 1][instructions[1] - 1] = '⬛'
                                self.Table[instructions[2]][instructions[3]] = self.tokens_cache
                else:
                    self.Table[instructions[0]][instructions[1]] = '⬛'
                    self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            for j in self.Table:
                for i in j:
                    self.generated_table.append(i)
            self.generated_table.insert(0, '')
            self.view = self.cache.join(self.generated_table)
            self.testing = instructions
        except:
            print('error: model --> data faild')
    def return_model_view(self):
        return self.view
    def return_raw_table(self):
        return self.Table
    def tested(self):
        print(len(self.Table[4][0]))
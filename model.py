class Model:
    def __init__(self):
        self.Table = [
            ['1','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['2','⬛', '⬜', '⭕', '⬜', '⬛', '⬜', '⚫' ,'⬜', '\n'],
            ['3','⬜', '⭕', '⬜', '⭕', '⬜', 'R', '⬜' ,'⬛', '\n'],
            ['4','⬛', '⬜', 'B', '⬜', '⬛', '⬜', '⚫' ,'⬜', '\n'],
            ['5','⬜', '⭕', '⬜', '⭕', '⬜', 'B', '⬜' ,'⬛', '\n'],
            ['6','⬛', '⬜', '⬛', '⬜', 'B', '⬜', 'R' ,'⬜', '\n'],
            ['7','⬜', '⚫', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
            ['8','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
            [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', '\n']
        ]
        # self.Table = [
        #     ['1','⬜', '⚫', '⬜', '⚫', '⬜', '⚫', '⬜' ,'⚫', '\n'],
        #     ['2','⚫', '⬜', '⚫', '⬜', '⚫', '⬜', '⚫' ,'⬜', '\n'],
        #     ['3','⬜', '⚫', '⬜', '⚫', '⬜', '⚫', '⬜' ,'⚫', '\n'],
        #     ['4','⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛' ,'⬜', '\n'],
        #     ['5','⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜' ,'⬛', '\n'],
        #     ['6','⭕', '⬜', '⭕', '⬜', '⭕', '⬜', '⭕' ,'⬜', '\n'],
        #     ['7','⬜', '⭕', '⬜', '⭕', '⬜', '⭕', '⬜' ,'⭕', '\n'],
        #     ['8','⭕', '⬜', '⭕', '⬜', '⭕', '⬜', '⭕' ,'⬜', '\n'],
        #     [' ','A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', '\n']
        # ]
        self.generated_table = []
        self.cache = ' '
        self.view = ''
        self.testing = None
    def input_instructions(self, instructions):
        try:
            self.tokens_cache = self.Table[instructions[0]][instructions[1]]
            if self.tokens_cache != '⬛' or self.tokens_cache != '⬜':
            # <-------------------------------------------------->
                if len(instructions) == 5:
                    self.__token_black_instructions(instructions)
                    self.__token_red_instructions(instructions)
                    self.__token_red_dame_instructions(instructions)
                    self.__token_black_dame_instructions(instructions)
                else:
                    self.Table[instructions[0]][instructions[1]] = '⬛'
                    if self.tokens_cache == '⭕' and instructions[2] == 0: # Add instructions convert a red token to dame
                        self.Table[instructions[2]][instructions[3]] = 'R'
                    elif self.tokens_cache == '⚫' and instructions[2] == 7: # Same whit black token
                        self.Table[instructions[2]][instructions[3]] = 'B'
                    else:    
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
    def return_render_view(self):
        for j in self.Table:
            for i in j:
                self.generated_table.append(i)
        self.generated_table.insert(0, '')
        self.view = self.cache.join(self.generated_table)
        return self.view
    def __token_black_instructions(self, instructions):
        if self.tokens_cache == '⚫':
            if instructions[4] == 'r':
                if self.Table[instructions[0] + 1][instructions[1] + 1] == '⭕' or self.Table[instructions[0] + 1][instructions[1] + 1] == 'R':
                    if self.Table[instructions[0] + 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] + 1] = '⬛'
                        if instructions[2] == 7: # Add instrucction for convert to dame
                            self.Table[instructions[2]][instructions[3]] = 'B'
                        else:    
                            self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'l':
                if self.Table[instructions[0] + 1][instructions[1] - 1] == '⭕' or self.Table[instructions[0] + 1][instructions[1] - 1] == 'R':
                    if self.Table[instructions[0] + 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] - 1] = '⬛'
                        if instructions[2] == 7: # Add instrucction for convert to dame
                            self.Table[instructions[2]][instructions[3]] = 'B'
                        else:    
                            self.Table[instructions[2]][instructions[3]] = self.tokens_cache
    def __token_red_instructions(self, instructions):
        if self.tokens_cache == '⭕':
            if instructions[4] == 'r':
                if self.Table[instructions[0] - 1][instructions[1] + 1] == '⚫' or self.Table[instructions[0] - 1][instructions[1] + 1] == 'B':
                    if self.Table[instructions[0] - 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] + 1] = '⬛'
                        if instructions[2] == 0: # Add instrucction for convert to dame
                            self.Table[instructions[2]][instructions[3]] = 'R'
                        else:    
                            self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'l':
                if self.Table[instructions[0] - 1][instructions[1] - 1] == '⚫' or self.Table[instructions[0] - 1][instructions[1] - 1] == 'B': 
                    if self.Table[instructions[0] - 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] - 1] = '⬛'
                        if instructions[2] == 0: # Add instrucction for convert to dame
                            self.Table[instructions[2]][instructions[3]] = 'R'
                        else:    
                            self.Table[instructions[2]][instructions[3]] = self.tokens_cache
    def __token_black_dame_instructions(self, instructions):
        if self.tokens_cache == 'B':
            if instructions[4] == 'r' or instructions[4] == 'rd':
                if self.Table[instructions[0] + 1][instructions[1] + 1] == '⭕' or self.Table[instructions[0] + 1][instructions[1] + 1] == 'R':
                    if self.Table[instructions[0] + 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] + 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'l' or instructions[4] == 'ld':
                if self.Table[instructions[0] + 1][instructions[1] - 1] == '⭕' or self.Table[instructions[0] + 1][instructions[1] - 1] == 'R':
                    if self.Table[instructions[0] + 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] - 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'ru':
                if self.Table[instructions[0] - 1][instructions[1] + 1] == '⭕' or self.Table[instructions[0] - 1][instructions[1] + 1] == 'R':
                    if self.Table[instructions[0] - 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] + 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'lu':
                if self.Table[instructions[0] - 1][instructions[1] - 1] == '⭕' or self.Table[instructions[0] - 1][instructions[1] - 1] == 'R':
                    if self.Table[instructions[0] - 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] - 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
    def __token_red_dame_instructions(self, instructions):
        if self.tokens_cache == 'R':
            if instructions[4] == 'r' or instructions[4] == 'ru':
                if self.Table[instructions[0] - 1][instructions[1] + 1] == '⚫' or self.Table[instructions[0] - 1][instructions[1] + 1] == 'B':
                    if self.Table[instructions[0] - 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] + 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'l' or instructions[4] == 'lu':
                if self.Table[instructions[0] - 1][instructions[1] - 1] == '⚫' or self.Table[instructions[0] - 1][instructions[1] - 1] == 'B':
                    if self.Table[instructions[0] - 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] - 1][instructions[1] - 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'rd':
                if self.Table[instructions[0] + 1][instructions[1] + 1] == '⚫' or self.Table[instructions[0] + 1][instructions[1] + 1] == 'B':
                    if self.Table[instructions[0] + 2][instructions[1] + 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] + 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
            if instructions[4] == 'ld':
                if self.Table[instructions[0] + 1][instructions[1] - 1] == '⚫' or self.Table[instructions[0] + 1][instructions[1] - 1] == 'B':
                    if self.Table[instructions[0] + 2][instructions[1] - 2] == '⬛':
                        self.Table[instructions[0]][instructions[1]] = '⬛'
                        self.Table[instructions[0] + 1][instructions[1] - 1] = '⬛'
                        self.Table[instructions[2]][instructions[3]] = self.tokens_cache
# def eat_recursive(self, cordinate0, cordinate1, direction):
#         self.token = self.Table[cordinate0][cordinate1]
#         if self.token == '⚫' or self.token == 'B':
#             if direction == 'rd':
#                 if self.Table[cordinate0 + 1][cordinate1 + 1] == '⭕' or self.Table[cordinate0 + 1][cordinate1 + 1] == 'R':
#                     if self.Table[cordinate0 + 2][cordinate1 + 2] == '⬛':
#                         self.Table[cordinate0][cordinate1] = '⬛'
#                         self.Table[cordinate0 + 1][cordinate1 + 1] = '⬛'
#                         if (cordinate0 + 2) == 7:
#                             self.Table[cordinate0 + 2][cordinate1 + 2] = 'B'
#                             return ''
#                         else:
#                             self.Table[cordinate0 + 2][cordinate1 + 2] = self.token
#                         return self.eat_recursive((cordinate0 + 2), (cordinate1 + 2), 'rd')
#                     if self.Table[cordinate0 + 2][cordinate1 + 2] != '⬛':
#                         return self.eat_recursive((cordinate0), (cordinate1), 'ld')
#             if direction == 'ld':
#                 if self.Table[cordinate0 + 1][cordinate1 - 1] == '⭕' or self.Table[cordinate0 + 1][cordinate1 - 1] == 'R':
#                     if self.Table[cordinate0 + 2][cordinate1 - 2] == '⬛':
#                         self.Table[cordinate0][cordinate1] = '⬛'
#                         self.Table[cordinate0 + 1][cordinate1 - 1] = '⬛'
#                         if (cordinate0 + 2) == 7:
#                             self.Table[cordinate0 + 2][cordinate1 - 2] = 'B'
#                             return ''
#                         else:
#                             self.Table[cordinate0 + 2][cordinate1 - 2] = self.token
#                         return self.eat_recursive((cordinate0 + 2), (cordinate1 - 2), 'ld')
#                     if self.Table[cordinate0 + 2][cordinate1 - 2] != '⬛':
#                         return self.eat_recursive((cordinate0), (cordinate1), 'rd')
#                         # test <----------------------klk-------------------------->
#         if self.token == '⭕' or self.token == 'R':
#             if direction == 'ru':
#                 if self.Table[cordinate0 - 1][cordinate1 + 1] == '⚫' or self.Table[cordinate0 - 1][cordinate1 + 1] == 'B':
#                     if self.Table[cordinate0 - 2][cordinate1 + 2] == '⬛':
#                         self.Table[cordinate0][cordinate1] = '⬛'
#                         self.Table[cordinate0 - 1][cordinate1 + 1] = '⬛'
#                         if (cordinate0 - 2) == 7:
#                             self.Table[cordinate0 - 2][cordinate1 + 2] = 'R'
#                             return ''
#                         else:
#                             self.Table[cordinate0 - 2][cordinate1 + 2] = self.token
#                         return self.eat_recursive((cordinate0 - 2), (cordinate1 + 2), 'ru')
#                     if self.Table[cordinate0 - 2][cordinate1 + 2] != '⬛':
#                         return self.eat_recursive((cordinate0), (cordinate1), 'lu')
#             if direction == 'lu':
#                 if self.Table[cordinate0 - 1][cordinate1 - 1] == '⚫' or self.Table[cordinate0 - 1][cordinate1 - 1] == 'B':
#                     if self.Table[cordinate0 - 2][cordinate1 - 2] == '⬛':
#                         self.Table[cordinate0][cordinate1] = '⬛'
#                         self.Table[cordinate0 - 1][cordinate1 - 1] = '⬛'
#                         if (cordinate0 - 2) == 7:
#                             self.Table[cordinate0 - 2][cordinate1 - 2] = 'R'
#                             return ''
#                         else:
#                             self.Table[cordinate0 - 2][cordinate1 - 2] = self.token
#                         return self.eat_recursive((cordinate0 - 2), (cordinate1 - 2), 'lu')
#                     if self.Table[cordinate0 - 2][cordinate1 - 2] != '⬛':
#                         return self.eat_recursive((cordinate0), (cordinate1), 'rd')
#         else:
            # return ''

global s
n = int(input(': '))
triangle = []
stt = ' '
for i in range((n)):
    triangle.insert(i, '\n')
    s = 1
    for j in range(i+1):
        triangle.append(str(int(s)))
        s = s * (i - j) / (j + 1)
stt = stt.join(triangle)
print(stt)
# count1 = 0
# count2 = 0
# while
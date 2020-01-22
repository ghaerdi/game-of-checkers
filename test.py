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




# try:
#     print(int(k))
# except (runtime, typerror, namerror):
#     print(runtime, typerror, namerror)
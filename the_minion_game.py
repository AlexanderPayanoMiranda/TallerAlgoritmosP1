def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    _len = len(string)
    _list = list(string)

    stuart = 0
    kevin = 0

    for i, s in enumerate(_list):
        if s in vowels:
            kevin += (_len - i)
        else:
            stuart += (_len - i)

    if kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
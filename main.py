def esc(code):
    return f'\u001b[{code}m'


def flag_swiss():
    col = 21
    k = 3
    for i in range(7):
        if i == 1 or i == 6:
            print(f'{RED}{" " * col}{END}')
        if 1 <= i <= 2 or 4 <= i <= 5:
            s = int((col - k) / 2)
            print(f'{RED}{" " * s}{WHITE}{" " * k}{RED}{" " * s}{END}')
        if i == 3:
            print(f'{RED}{" " * 3}{WHITE}{" " * (col - 6)}{RED}{" " * 3}{END}')


def draw_symbol(repeat):
    half = 8
    col = half * 2
    space = "   "
    for i in range(col + 1):
        if i == 0 or i == col:
            line = f'{WHITE}{space * (half - 2)}{RED}{space * 4}{WHITE}{space * (half - 2)}'
            print(f'{line * repeat * 2}{END}')
            continue

        if half - 2 <= i <= half + 2:
            line = f'{RED}{space}{WHITE}{space * (col - 2)}{RED}{space}'
            print(f'{line * repeat * 2}{END}')
            continue

        if i <= half:
            k = half - i - 2
            line = f'{WHITE}{space * k}{RED}{space}{WHITE}{space * (col - k * 2 - 2)}{RED}{space}{WHITE}{space * k}'
            print(f'{line * repeat * 2}{END}')
        else:
            k = i - half - 2
            line = f'{WHITE}{space * k}{RED}{space}{WHITE}{space * (col - k * 2 - 2)}{RED}{space}{WHITE}{space * k}'
            print(f'{line * repeat * 2}{END}')


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

flag_swiss()
r = input('Колличество повторений узора: ')
draw_symbol(int(r))

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

print()
for i in range(10):
    result[i] = i / 3

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

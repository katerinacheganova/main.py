def open_file():
    """данная функция открывает считывает масив из файла."""
    file = open('text.txt')
    lst = file.readlines()
    del lst[0]
    lst = [[int(n) for n in x.split()] for x in lst]


def calculate(lst: list) -> int:
    """функция для вычисления количества несоприкасающихся единиц."""
    count = 0
    if len(lst) > 0:
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j] == 1:
                    if i == (int(len(lst) - 1)) or lst[i + 1][j] == 0:
                        if j == (int(len(lst[i]) - 1)) or lst[i][j + 1] == 0:
                            count += 1
    return count

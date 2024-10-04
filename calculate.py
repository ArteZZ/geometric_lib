import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    """
    Вычисляет заданную функцию (периметр или площадь) для указанной фигуры (круг или квадрат).

    Параметры:
    fig (str): Название фигуры ('circle' или 'square').
    func (str): Название функции ('perimeter' или 'area').
    size (list): Список размеров, необходимых для вычисления функции.

    Пример вызова:
    calc('circle', 'area', [5])  # Вычисляет площадь круга с радиусом 5
    calc('square', 'perimeter', [4])  # Вычисляет периметр квадрата со стороной 4

    Возвращает:
    None: Результат выводится на экран.
    """
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)

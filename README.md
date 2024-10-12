# Calculator Documentation

## General description of the solution
This project is a console calculator that allows you to calculate the area and perimeter of various figures, such as a circle and a square. The user enters the name of the figure, selects the function (area or perimeter) and enters the required dimensions. The calculator uses mathematical formulas to perform calculations and displays the result on the screen.

# How to use calculator:

1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Function Descriptions

### `calculate_area(figure, dimensions)`
Calculates the area of the specified figure based on the provided dimensions.

**Parameters:**
- `figure` (str): The name of the figure (e.g., "Circle", "Square").
- `dimensions` (float or list): The dimensions required for the calculation (e.g., radius for circle, side length for square).

**Returns:**
- float: The calculated area of the figure.

**Example Calls:**
```python
area_circle = calculate_area("Circle", 5)  # Returns the area of a circle with radius 5
area_square = calculate_area("Square", 4)  # Returns the area of a square with side length 4
```
### `calculate_perimeter(figure, dimensions)`
Calculates the perimeter of the specified figure based on the provided dimensions.

**Parameters:**
- `figure` (str): The name of the figure (e.g., "Circle", "Square").
- `dimensions` (float or list): The dimensions required for the calculation (e.g., radius for circle, side length for square).

**Returns:**
- float: The calculated perimeter of the figure.

**Example Calls:**
```python
perimeter_circle = calculate_perimeter("Circle", 5)  # Returns the perimeter of a circle with radius 5
perimeter_square = calculate_perimeter("Square", 4)  # Returns the perimeter of a square with side length 4
```
## Project change history

- **Commit Hash: 7b7124e** - Добавлена документация в `calculate.py`, `circle.py`, `square.py` и `triangle.py`.
- **Commit Hash: b5b0fae** - Обновлена документация для `calculate.py`.
- **Commit Hash: d76db2a** - Добавлен файл `calculate.py`.
- **Commit Hash: 51c40eb** - Обновлена документация для треугольника.
- **Commit Hash: d080c78** - Добавлен файл `triangle.py`.
- **Commit Hash: 86edb1c** - Обновлена документация. Добавлена информация о пользовательском соглашении.
- **Commit Hash: 438b89a** - Добавлено пользовательское соглашение.
- **Commit Hash: 6adb962** - Добавлены документы.
- **Commit Hash: 3049431** - Добавлен файл `rectangle.py`.
- **Commit Hash: d078c8d** - Добавлены документы.
- **Commit Hash: 8ba9aeb** - Добавлены круг и квадрат.



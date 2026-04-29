def diagonal_sums(matrix):
    """
    Возвращает сумму элементов главной и побочной диагонали матрицы.
    Для прямоугольной матрицы используются элементы, которые существуют
    в пределах размерности матрицы.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    main_sum = 0
    secondary_sum = 0

    limit = min(rows, cols)

    for i in range(limit):
        main_sum += matrix[i][i]
        secondary_sum += matrix[i][cols - 1 - i]

    return main_sum, secondary_sum


def determinant(matrix):
    """
    Вычисляет определитель квадратной матрицы рекурсивным методом.
    """
    n = len(matrix)

    if n == 0:
        raise ValueError("Матрица не должна быть пустой")

    for row in matrix:
        if len(row) != n:
            raise ValueError("Определитель можно найти только для квадратной матрицы")

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0

    for col in range(n):
        minor = []

        for i in range(1, n):
            row = []

            for j in range(n):
                if j != col:
                    row.append(matrix[i][j])

            minor.append(row)

        sign = (-1) ** col
        result += sign * matrix[0][col] * determinant(minor)

    return result


def minimum_element(matrix):
    """
    Находит минимальный элемент матрицы и его индексы.
    Индексы возвращаются с нуля.
    """
    min_value = matrix[0][0]
    min_row = 0
    min_col = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row = i
                min_col = j

    return min_value, min_row, min_col

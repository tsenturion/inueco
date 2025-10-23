#1 O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#2 O(n)
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total


#3
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


#4
def print_array(arr):
    for element in arr:
        print(element)


#5
def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

    
#6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#7
def print_all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"({arr[i]}, {arr[j]})")


#8 O(n^2)
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


#9
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


#10
def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


#11 O(1)
def get_element(arr, index):
    return arr[index]


#12
def append_to_list(lst, element):
    lst.append(element)


#13
def is_first_element_zero(arr):
    if arr[0] == 0:
        return True
    return False


#14
def get_length(arr):
    return len(arr)


#15
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


#16
def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


#17
def bubble_first_pass(arr):
    n = len(arr)
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


#18
def search_sorted_matrix(matrix, target):
    if not matrix:
        return False
        
    row = 0
    col = len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


#19
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total

    
#20
def find_common_element(arr1, arr2):
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2:
                return elem1
    return None


"""
Алгоритм 1: Линейный поиск
Последовательно проверяет каждый элемент массива до нахождения искомого значения.
Сложность: O(n) - в худшем случае необходимо проверить все n элементов массива.

Алгоритм 2: Сумма элементов массива
Вычисляет общую сумму всех числовых элементов в массиве.
Сложность: O(n) - требуется один последовательный проход по всем n элементам для их сложения.

Алгоритм 3: Поиск максимума в массиве
Находит наибольшее значение в массиве путем последовательного сравнения элементов.
Сложность: O(n) - необходимо сравнить между собой все n элементов массива.

Алгоритм 4: Печать всех элементов массива
Выводит каждый элемент массива на экран в отдельной строке.
Сложность: O(n) - выполняется ровно n операций вывода.

Алгоритм 5: Подсчет четных чисел
Считает количество четных чисел в массиве путем проверки каждого элемента.
Сложность: O(n) - каждая из n итераций включает проверку условия четности.

Алгоритм 6: Пузырьковая сортировка
Сортирует массив путем многократного прохода и попарного сравнения соседних элементов.
Сложность: O(n²) - два вложенных цикла дают n*(n-1)/2 сравнений в худшем случае.

Алгоритм 7: Вывод всех пар элементов
Генерирует и выводит все возможные пары элементов массива.
Сложность: O(n²) - для каждого из n элементов создается n пар, всего n² комбинаций.

Алгоритм 8: Поиск дубликатов в массиве
Проверяет наличие повторяющихся элементов путем попарного сравнения всех элементов.
Сложность: O(n²) - количество сравнений растет пропорционально n*(n-1)/2.

Алгоритм 9: Транспонирование матрицы
Создает новую матрицу, где строки становятся столбцами, а столбцы - строками.
Сложность: O(n*m) - обрабатывается каждый элемент матрицы размером n на m.

Алгоритм 10: Умножение матриц
Выполняет умножение двух матриц по правилу "строка на столбец".
Сложность: O(n³) - для квадратных матриц n×n требуется три вложенных цикла по n итераций.

Алгоритм 11: Доступ к элементу массива по индексу
Возвращает значение элемента массива по заданному индексу.
Сложность: O(1) - доступ по индексу выполняется за постоянное время.

Алгоритм 12: Вставка элемента в конец списка
Добавляет новый элемент в конец списка.
Сложность: O(1) - амортизированная сложность добавления в конец списка Python.

Алгоритм 13: Проверка первого элемента массива
Проверяет, равен ли первый элемент массива нулю.
Сложность: O(1) - выполняется единственная операция сравнения.

Алгоритм 14: Получение длины массива
Возвращает количество элементов в массиве.
Сложность: O(1) - длина хранится как свойство объекта и доступна мгновенно.

Алгоритм 15: Обмен значений двух переменных
Меняет местами значения двух переменных с использованием временной переменной.
Сложность: O(1) - выполняется фиксированное количество операций присваивания.

Алгоритм 16: Оптимизированная пузырьковая сортировка
Улучшенная версия пузырьковой сортировки с досрочным завершением при отсутствии обменов.
Сложность: O(n²) - в худшем случае сохраняется квадратичная сложность.

Алгоритм 17: Частичная пузырьковая сортировка
Выполняет только один проход пузырьковой сортировки, частично упорядочивая массив.
Сложность: O(n) - один проход по n-1 парам элементов.

Алгоритм 18: Поиск в отсортированной матрице
Ищет элемент в матрице, отсортированной по строкам и столбцам, начиная из правого верхнего угла.
Сложность: O(n + m) - в худшем случае выполняется n+m шагов по строкам и столбцам.

Алгоритм 19: Подсчет суммы элементов в матрице
Вычисляет сумму всех элементов двумерной матрицы.
Сложность: O(n × m) - необходимо обработать каждый элемент матрицы размером n на m.

Алгоритм 20: Поиск общего элемента в двух массивах
Находит первый общий элемент в двух массивах путем полного перебора всех пар.
Сложность: O(n × m) - каждый элемент первого массива сравнивается с каждым элементом второго.
"""
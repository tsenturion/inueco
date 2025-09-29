# 1
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
 # Последовательный поиск, проверяет каждый элемент по очереди O(n)

#2
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Вычисления суммы всех элементов в массиве O(n)

#3
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
# Ищет максимальное значение O(n)

#4
def print_array(arr):
    for element in arr:
        print(element)
# Вывод множество O(n)

#5
def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count
# Считает только четные числа O(n)
    
#6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Пузырьковая сортировка, о нем мы говорили O(n^2)

#7
def print_all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"({arr[i]}, {arr[j]})")
# Вывод все возможные комбинации заданых числе O(n)

#8
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
# Ищет повторяющиеся значения O(n)

#9
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
# Строки и столбцы меняются местами O(1)

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
# Матричное умножение по правилам выш.мата O(n^3)

#11
def get_element(arr, index):
    return arr[index]
# Импортирует элемент (относится к методам билбиотеки Selenium) O(1)

#12
def append_to_list(lst, element):
    lst.append(element)
# Метод Append для добавления элемента в конец списка O(1)

#13
def is_first_element_zero(arr):
    if arr[0] == 0:
        return True
    return False
# Список индексируется начиная с нуля O(1)

#14
def get_length(arr):
    return len(arr)
# Определяет длину - кол-во элементов объекта O(n)

#15
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b
# Меняет местами значение двух переменных O(1)

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
# Оптимизированная сортировка пузырьком. Если перестановки не было - алгоритм завершается досрочно. O(n^2)

#17
def bubble_first_pass(arr):
    n = len(arr)
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
#  Выполняет один проход пузырьковой сортировки

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
# Поиск элемента в отсортированной матрице O(n)

#19
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total
# Общая сумма всех элементов матрицы O(n)
    
#20
def find_common_element(arr1, arr2):
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2:
                return elem1
    return None
# Ищет общий элемент между двумя списками O(n)
# New branch work test
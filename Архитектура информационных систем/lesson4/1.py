# 1
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
Они ищет элемент arr в target, 
если она понимает что они совпадают ->  if arr[i] == target:, 
то возвращаем i, ели мы так и не нашли, то -1. Сложность как я понимаю O(n)

#2
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

Она вычисляет сумму всех чисел которые есть в списке, сложность O(n)

#3
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

Она проходится по списку, в начале проверяя есть ли в массиве что-то, 
если ничего нету, мы возвращаем max_val = arr[0] означает что мы начинаем с нуля,
потом каждое число num сравнивается с arr, если num > max_val, мы к max_val приравниваем num,
и потом возвращаем num_val, Сложность O(n)


#4
def print_array(arr):
    for element in arr:
        print(element)

Проходимся по arr и присваиваем в element и выводим их
Сложность O(n)

#5
def count_even_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

Принимает массив, если в массиве(num), есть число которое делится на 2 без остатка, мы в count записываем +1,
потом выозвращаем количество(count) Солжность O(n)

#6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

Функция сравнивает числа в массиве на каких они стоят местах, но arr[j] > arr[j + 1]: как я понимаю мы его нашли,
потом в конец его ставим arr[j], arr[j + 1] = arr[j + 1], arr[j] массива Сложность O(n²)

#7
def print_all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"({arr[i]}, {arr[j]})")
Дважды проходит по массиву, и выводит их Сложность O(n²)

#8
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

Проходимся по массиву, if arr[i] == arr[j]: если мы понимаем что два числа в массиве равных друг другу,
мы возвращаем True, если это не так, откидываем False Сложность O(n²)


#11
def get_element(arr, index):
    return arr[index]

Возвращает элемент по индексу Сложность O(1)

#12
def append_to_list(lst, element):
    lst.append(element)

Добавляет элемент в конец списка Сложность O(1)

#13
def is_first_element_zero(arr):
    if arr[0] == 0:
        return True
    return False

Если число arr[0] = 0 то мы откидываем true, если это не так, то False, Сложность O(1)

#14
def get_length(arr):
    return len(arr)

Просто возвращает длину массива Сложность O(1)


#15
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

Функция менят значение с a,b на b,a ( где b = a, a = b) Сложность O(1)



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
Это тоже сортировка, мы проходимся от начала массива,if arr[j] > arr[j + 1]: - меняем местами элементы если они не в том порядке,
swapped = True как я понимаю нужно чтобы проверить отсортирован ли массив, если это так то завершаем Сложность O(n)

#17
def bubble_first_pass(arr):
    n = len(arr)
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

Пооходит по всему массиву и опять смотрит элементы и меняет их местами если один элемент больше другого Сложность O(n)

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

ищет элемент target в массиве arr, если находим совпадение if arr[i] == target возвращает i,
если так и не нашли, возвращаем -1, сложность O(n)


#19
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total
Проходит по всему массиву и прибовляем element к total и возвращаем его Сложность O(n * m)


#20
def find_common_element(arr1, arr2):
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2:
                return elem1
    return None

Она ищет элементы в двух массивах, если они совпадают, то возвращаем elem1, если это не так, то откидываем none Сложность O(n * m)
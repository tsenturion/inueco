"""
бинарный поиск
"""

"""
по способу организации

внутренняя сортировка - в оперативке
внешняя - для больших данных, с записью во временные файлы
"""

"""
по устойчивости (стабильности)

стабильная сортировка- сохраняет порядок одинаковых элементов
нестабильная - может измениться
"""

"""
по принципу работы

обменные алгоритмы - пузырьковая - if else
выборочные - выбором - выбирается минимальный элемент
вставочные - вставками - новый элемент вставляется в отсортированную часть списка
разделяй и властвуй - быстрая, слиянием - рекурсия, части сортируются
"""

"""
.sort() - сортирует список на месте - изменяет его
sorted() - возвращает новый"""

"""numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort()
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

words = ['123', '1234', '12', '12334']
words.sort(key=len)
print(words)

students = [('иван', 20), ("анна", 18), ("петр", 22)]
students.sort(key=lambda x: x[1])
print(students)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort(reverse=True)
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)"""
"""
O(n)
n - размер входных данных (сколько элементов)
"""

"""
простые O(n^2)
пузырьковая, вставками, выбором
"""

"""
продвинутые O(n log n)
слиянием быстрая 
"""

"""
гибридные
timsort: вставками + слиянием
"""

"""
пузырьковая (bubble sort)
"""

"""
1 проход

[5, 3, 8, 4, 2] 5 3 8 4 2
5 > 3
3 5
[3, 5, 8, 4, 2]
5 < 8
[3, 5, 8, 4, 2]
8 > 4
4 8
[3, 5, 4, 8, 2]
8 > 2
2 8
[3, 5, 4, 2, 8]
"""

def bubble_sort_bad(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#[3, 2, 4, 5, 8]
#[2, 3, 4, 5, 8]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

#выбором (selection sort)

"""
min из неотсортированной части массива
меняем этот минимальный e с первым e неотсортированной части
повторяем
"""

"""
1 проход

[5, 3, 8, 4, 2]
2 <-> 5
[2, 3, 8, 4, 5]

2 проход

[2, 3, 8, 4, 5]
3 <-> 5
[2, 3, 8, 4, 5]

3 проход

[2, 3, 8, 4, 5]
4 <-> 8
[2, 3, 4, 8, 5]

"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index] ,arr[i]

"""numbers = [5, 3, 8, 4, 2]
selection_sort(numbers)
print(numbers)"""

def selection_sort(arr):
    n = len(arr)
    left, right = 0, n - 1
    while left < right:
        min_index = left
        max_index = right

        for i in range(left, right + 1):
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[min_index]:
                max_index = i

        arr[left], arr[min_index] = arr[min_index], arr[left]

        if max_index == left:
            max_index = min_index

        arr[right], arr[max_index] = arr[max_index], arr[right]

        left += 1
        right -= 1
"""
[]
[4, 2, 5, 1]
min 1
[1, 2, 5, 4]
[1]

[1]
[1, 2, 5, 4]
min 2
[1, 2, 5, 4]
[1, 2]

[1, 2]
[1, 2, 5, 4]
min 4
[1, 2, 4, 5]

"""





"""
левая уже отсортирована
правая нет

[5, 2, 4, 6, 1, 3]
2 < 5
[2, 5, 4, 6, 1, 3]
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key



"""
[4, 3, 2, 1]
3 4
3 
[3 4 2 1]
2 < 4 
4
[3 4 4 1]
2 < 3
[3 3 4 1]
[2 3 4 1]

[2 3 4 4]
[2 3 3 4]
[2 2 3 4]
[1 2 3 4]
"""

"""
1: выбираем шаг
2: сортируем с шагом
3: уменьшаем шаг
4: дойдя до 1 = обычная вставками

[5, 2, 9, 1, 5, 6]
первые элементы:
i = 0 3 6
[5, 1]
вторые элементы:
i = 1, 4
[2, 5]
третьи элементы:
i = 2, 5
[9, 6]

[1, 2, 6, 5, 5, 9]

хиббарда
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2

# массивы из numpy (они там на C)
"""
массив из 1 элемента - отсортирован
разделяем массив на две части
рекурсивно сортируем каждую из этих частей
сливаем в один массив

[1, 4, 6]
[2, 3, 5]

[8, 4, 5, 7, 1, 3, 6, 2]
[8, 4, 5, 7] [1, 3, 6, 2]
[8, 4] [5, 7] [1, 3] [6, 2]
[8] [4] [5] [7] [1] [3] [6] [2]
[8] [4] -> [4, 8]
[5] [7] -> [5, 7]
[4, 5, 7, 8]
[1, 2, 3, 6]

особенности/важно
стабилен
неинтерактивность
рекурсивность 
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

"""

max-heap: каждый родитель больше или равен своим детям
min-heap: каждый родитель меньше или равен своим детям
"""
"""
heap - вид бинарного дерева, частично упорядочена
max-heap (макси-куча): каждый родитель больше или равен своим детям (потомкам)
min-heap (мини-куча): каждый родитель меньше или равен своим детям (потомкам)

max-heap (макси-куча): на вершине максимальный элемент. Получаем минимальный элемент на O(1)
min-heap (мини-куча): на вершине наименьший элемент. Получаем минимальный элемент на O(1)

алгоритм Дейкстры 
heap sort
реализация приоритетной очереди
медиана потока данных
планировщики задач
системы обработки событий
сжатия данных

import heapq - минимальная куча на базе списка
"""
import heapq

numbers = [5, 3, 8, 1, 2]
heapq.heapify(numbers)  # на месте в мин кучу. numbers[0] - минимальный. Порядок остальных не гарантирован
print(numbers)

heapq.heappush(numbers, 0)  # добавляет item в heap и сохраняет ее свойства
print(numbers)

min_element = heapq.heappop(numbers)  # удаляет и возвращает наименьший элемент из кучи
print(min_element)
print(numbers)

#heapq.heappushpop(heap, item) добавляет item, возвращает наименьший элемент

numbers = [5, 3, 8, 1, 2]
#n самых больших или маленьких элементов
print(heapq.nlargest(2, numbers))
print(heapq.nsmallest(3, numbers))


#приоритетная очередь
tasks = []
heapq.heappush(tasks, (2, 'писать отчет'))
heapq.heappush(tasks, (1, 'проверить почту'))
heapq.heappush(tasks, (3, 'созвон с коллегами'))

while tasks:
    task = heapq.heappop(tasks)
    print(f'выполняется задача {task}')

# макси куча

numbers = [5, 3, 8, 1, 2]
max_heap = [-x for x in numbers]
heapq.heapify(max_heap)

max_value = -heapq.heappop(max_heap)
print(max_value)

heap = [1, 3, 5, 7, 9, 8]
"""
        1
      /   \
     3     5
    / \     \
   7   9     8
"""
"""
бинарная куча, каждый узел имеет не более двух детей

"""
"""

для любого элемента с i - индекс
левый потомок на позиции 2*i + 1
правый потомок на позиции 2*i + 2
родитель потомок на позиции (i - 1) // 2

        10              <- индекс 0
      /    \
     9      8           <- индексы 1 и 2
    / \    / \
   7   6  5   4         <- индексы 3,4,5,6
                                arr[3] = 7
                                
arr =[10, 9, 8, 7, 6, 5, 4]
""""""
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)"""

"""
+
экономия памяти
быстрота доступа
простота реализации
универсальность
"""

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

"""
[3, 9, 2, 1, 4, 5]
i = 2 (последний родитель): 2, 5 - переставлять не надо
i = 1: 9, 1, 4 (9 остается на месте)
i = 0: 3, 9, 2 (меняем 3 и 9)
[9, 3, 2, 1, 4, 5]
"""
"""
для любого элемента с i - индекс
левый потомок на позиции 2*i + 1
правый потомок на позиции 2*i + 2
родитель потомок на позиции (i - 1) // 2
i   родитель    левый   правый
0   -   1   2
1   0   3   4
2   0   5   6
3   1   7   8
4   1   9   10

"""
"""
heap sort (по возрастанию) (in-place)
1 массив в максимальную кучу
2 максимальный элемент в корне arr[0]
3 меняем местами с последним элементом в массиве и исключаем из обработки
4 heapify 
5 повторяем

1 построение кучи - проходим по массиву снизу вверх и восстанавливаем кучу от каждого элемента
2 сортировка 
2.1 берем максимум
2.2 меняем с последним неотсортированным элементом
2.3 уменьшаем границу кучи
2.4 heapify

+
O(nlogn)
не требует доп памяти
для больших объемов данных
-
не стабильная (одинаковые элементы могут поменять порядок)
сложная реализация
heapq

[4, 10, 3, 5, 1]
        10
      /    \
    5       3
  /           \
4              1
[1, 5, 3, 4, 10]
[1, 5, 3, 4]
"""

def heapify(arr, n, i, ascending):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if ascending:
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else:
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, ascending)


def heap_sort(arr, ascending=True):
    n = len(arr)

    #строим кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

    #сортируем, вытаскивая корень и уменьшая размер кучи
    for i in range(n - 1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, ascending)
"""
[4, 10, 3, 5, 1]
        10
       /  \
      5    3
     /
    4
[10, 5, 3, 4, 1]
меняем 10 и 1
[1, 5, 3, 4, 10]
heapigy([1, 5, 3, 4]) 
"""

"""
1 выбираем опорный элемент
2 переставляем. Слева все элементы меньше него, справа больше
3 рекурсивно применяем к левому и правому подмассивам
4 1/0 - базовый случай

[5, 3, 8, 4, 2, 7, 1, 7]
5
меньше [3, 4, 2, 1]
больше [8, 7, 6]

первый 
последний
случайный
середина
медиана 
"""
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high, ascending=True):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if (ascending and arr[j] <= pivot) or (not ascending and arr[j] >= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

"""
вставками, слиянием

run (прогоны) - отсортированная часть
[1, 2, 3, 7, 4, 5, 6, 10]
[1, 2, 3, 7]
[4, 5, 6, 10]

1 нахождение runs
2 вставками
3 слияние runs
4 merge policy условия слияния 
"""
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def timsort(arr):
    n = len(arr)
    RUN = 32  # длина минимального run

    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))

    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
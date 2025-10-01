from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())

if not stack:
    print("Стек пуст")

"""
append(x)     добавляет элемент x в конец стека
pop()         удаляет и возвращает последний элемент стека
if not stack  проверка, пуст ли стек
stack[-1]     Peek Просмотр верхнего элемента
clear()       очистка, не всегда
"""

"""
Дана строка, содержащая скобки различных типов: (), [], {}. 
Необходимо проверить, является ли скобочная последовательность корректной. 
Корректная последовательность означает, 
что каждой открывающей скобке соответствует закрывающая скобка того же типа, 
и скобки правильно вложены друг в друга.
"""

str1 = "()[]{}" # True
str2 = "([{}])" # True
str3 = "(]" # False
str4 = "([)]" # False

def is_valid_brackets(s):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map:
            if not stack or stack.pop() != brackets_map[char]:
                return False
    return not stack

print(is_valid_brackets(str1))
print(is_valid_brackets(str2))
print(is_valid_brackets(str3))
print(is_valid_brackets(str4))

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)

if not queue:
    print("Очередь пуста")

"""
реализовать class структуру данных очередь
добавление элемента в очередь enqueue
удаление элемента из очереди dequeue
получение максимального элемента в очереди get_max max
получение минимального элемента в очереди get_min min

использовать deque 
"""


class SimpleMinMaxQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def get_max(self):
        if not self.queue:
            return None
        return max(self.queue)

    def get_min(self):
        if not self.queue:
            return None
        return min(self.queue)

smq = SimpleMinMaxQueue()
smq.enqueue(3)
smq.enqueue(1)
smq.enqueue(5)
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
"""
добавление
append(x)
appendleft(x)

удаление
pop()
popleft()

методы
clear()  полностью очистить
extend(iterable) — добавляет все элементы из итерируемого объекта в конец deque
extendleft(iterable) — добавляет все элементы из итерируемого объекта в начало deque (элементы добавляются в обратном порядке)
rotate(n) — циклически сдвигает элементы deque на n шагов. Если n положительное, сдвиг происходит вправо, если отрицательное — влево
count(x)  возвращает количество элементов, равных x
remove(x)  удаляет первый найденный элемент, равный x

свойство
maxlen  максимальный размер deque (если задан). Если при добавлении элементов размер превышает maxlen, элементы с противоположного конца автоматически удаляются
"""
d = deque([1, 2, 3])
d.extend([4, 5, 6])  # Добавляем элементы в конец
print(d)  # deque([1, 2, 3, 4, 5, 6])

d = deque([4, 5, 6])
d.extendleft([1, 2, 3])  # Добавляем элементы в начало
print(d)  # deque([3, 2, 1, 4, 5, 6])

d = deque([1, 2, 3, 4, 5])
d.rotate(2)  # Сдвигаем вправо на 2 шага
print(d)  # deque([4, 5, 1, 2, 3])

d.rotate(-2)  # Сдвигаем влево на 2 шага
print(d)  # deque([1, 2, 3, 4, 5])

d = deque([1, 2, 3])
d.clear()  # Очищаем deque
print(d)  # deque([])

d = deque([1, 2, 2, 3, 2, 4])
print(d.count(2))  # 3 (элемент 2 встречается 3 раза)

d = deque([1, 2, 3, 2, 4])
d.remove(2)  # Удаляем первый элемент 2
print(d)  # deque([1, 3, 2, 4])

# Создаем deque с максимальным размером 3
d = deque([1, 2, 3], maxlen=3)
print(d)  # deque([1, 2, 3], maxlen=3)

# Добавляем новый элемент
d.append(4)  # Элемент 1 удаляется, так как maxlen=3
print(d)  # deque([2, 3, 4], maxlen=3)

# Добавляем несколько элементов
d.extend([5, 6])  # Элементы 2 и 3 удаляются
print(d)  # deque([4, 5, 6], maxlen=3)


"""
реализовать скользящее окно для массива чисел. 
для каждого окна размера k найти максимальный элемент."""

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
"""
[1, 3, -1]  3
[3, -1, -3]  3
[-1, -3, 5]  5
[-3, 5, 3]  5
[5, 3, 6]  6
[3, 6, 7]  7

[3, 3, 5, 5, 6, 7]"""

from collections import deque

def max_in_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    result = []
    d = deque()

    for i, num in enumerate(nums):
        while d and d[0] < i - k + 1:
            d.popleft()

        while d and nums[d[-1]] < num:
            d.pop()

        d.append(i)

        if i >= k - 1:
            result.append(nums[d[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_in_sliding_window(nums, k))
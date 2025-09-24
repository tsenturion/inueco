"""1 -> 2 -> 3 -> 4 -> None
1 -> None
 2 -> 3 -> 4 -> None
None <- 4 <-> 5 <-> 6 -> None"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def remove_from_head(self):
        if self.head:
            self.head = self.head.next

    def remove_by_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.remove_from_head()
            return
        if self.tail.data == data:
            self.remove_from_tail()
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Элемент {target_data} не найден в списке")

    def reverse(self):
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def clear(self):
        self.head = None

    def remove_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        if index == 0:
            self.remove_from_head()
            return
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of range")
            current = current.next
        if current and current.next:
            current.next = current.next.next
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        return " <-> ".join(str(item) for item in self) + " -> None"

    def __len__(self):
        return sum(1 for _ in self)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError("Index out of range")

    def __contains__(self, data):
        return any(item == data for item in self)

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __add__(self, other):
        new_list = LinkedList()
        for item in self:
            new_list.add_to_tail(item)
        for item in other:
            new_list.add_to_tail(item)
        return new_list

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __bool__(self):
        return self.head is not None

    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            if not sorted_head or sorted_head.data >= current.data:
                current.next = sorted_head
                if sorted_head:
                    sorted_head.prev = current
                sorted_head = current
                sorted_head.prev = None
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                if temp.next:
                    temp.next.prev = current
                temp.next = current
                current.prev = temp

            current = next_node

        self.head = sorted_head
        self.tail = sorted_head
        while self.tail and self.tail.next:
            self.tail = self.tail.next

    def merge_sort(self):
        if not self.head or not self.head.next:
            return

        def split(head):
            if not head or not head.next:
                return head, None
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            middle = slow
            second_half = middle.next
            middle.next = None

            if second_half:
                second_half.prev = None

            return head, second_half

        def merge(left, right):
            if not left: return right
            if not right: return left
            dummy = Node(0)
            current = dummy

            while left and right:
                if left.data < right.data:
                    current.next, left.prev, left = left, current, left.next
                else:
                    current.next, right.prev, right = right, current, right.next
                current = current.next

                if left:
                    current.next, left.prev = left, current
                elif right:
                    current.next, right.prev = right, current

                head = dummy.next
                head.prev = None
                return head

        def merge_sort_recursive(node):
            if not node or not node.next:
                return node
            left, right = split(node)
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)

            return merge(left, right)

        self.head = merge_sort_recursive(self.head)

        current = self.head
        while current.next:
            current = current.next
        self.tail = current


    def binary_search(self, target):
        if not self.head:
            return None

        length = len(self)
        left = self.head
        right = self.tail

        while left != right:
            mid = left
            steps = (length // 2) - 1
            for _ in range(steps):
                mid = mid.next

            if mid.data == target:
                return mid
            elif mid.data < target:
                left = mid.next
            else:
                right = mid.prev

            length = length // 2

        return None

ll1 = LinkedList()
ll1.add_to_tail(30)
ll1.add_to_tail(20)
ll1.add_to_tail(10)
ll1.merge_sort()
print(ll1)

"""ll1 = LinkedList()
ll1.add_to_tail(10)
ll1.add_to_tail(20)
ll1.add_to_tail(30)

ll2 = LinkedList()
ll2.add_to_tail(40)
ll2.add_to_tail(50)

print("Список 1:", ll1)
print("Длина списка 1:", len(ll1))
print("Элемент с индексом 1:", ll1[1])
print("Есть ли 20 в списке 1?", 20 in ll1)

print("Итерация по списку 1:")
for item in ll1:
    print(item, end=" ")
print()

ll3 = ll1 + ll2
print("Объединенный список:", ll3)

print("Списки 1 и 2 равны?", ll1 == ll2)
print("Список 1 пуст?", not ll1)

ll1.clear()
print("Список 1 после очистки:", ll1)
print("Список 1 пуст?", not ll1)"""
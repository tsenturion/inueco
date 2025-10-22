import pytest

"""stack = []
print(not stack)
stack.append(1)
stack.append(2)
stack.append(3)
print(not stack)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(not stack)"""

def test_stack():
    stack = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

"""def test_stack1():
    stack = []
    stack.append(1)
    stack.append(2)
    assert stack.pop() == 2

def test_stack2():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.pop()
    assert stack.pop() == 1"""

def test_emptiness():
    stack = []
    assert not stack
    stack.append(1)
    assert bool(stack)
    stack.pop()
    assert not stack

def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
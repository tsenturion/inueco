from typing import (Union, List, Optional, Dict, Any,
                        TypeVar, Generic, Callable, TypedDict,
                        Literal)
x = 10
x = 'hello'

def add(a: int, b: int) -> int:
    return a + b

def total(values: List[int]) -> int:
    return sum(values)

"""
Dict[key_type, value_type]
Tuple[type1, type2, ...]
Set[element_type]
Optional[type]
Union[]
Any
"""

def get_user_age(users: Dict[str, int], name: str) -> Optional[int]:
    return users.get(name)

def process(value: Union[int, str]) -> str:
    return str(value)

def print_data(data: Any) -> None:
    print(data)

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> List[T]:
        return self.items
    

def apple_operation(
        a: int, 
        b: int, 
        operation: Callable[[int, int], int]
        ) -> int:
    return operation(a, b)

class User(TypedDict):
    name: str
    age: int
    active: bool

def show_user(user: User) -> None:
    print(f"{user['name']} ({user['age']} лет), активен: {user['active']}")

def total(values: list[int]) -> int:
    return sum(values)

def set_status(status: Literal['active', 'inactive', 'banned']) -> None:
    print(f"Статус пользователя: {status}")
"""
pydash

includes()
size()
filter()
...(20)
"""

"""
scopes
function:  на каждую функцию, который ее использует. (по умолчанию)
class:  для каждого класса тестов, который ее использует.
module:  для каждого модуля тестов, который ее использует.
package:  для каждого пакета тестов, который ее использует.
session:  для всего сеанса тестирования.
"""
"""
фикстуры
Функциональная область видимости (function): Фикстура будет выполнена для каждой тестовой функции, в которой она используется. Это область видимости по умолчанию.
Классовая область видимости (class): Фикстура будет выполнена для каждого метода в классе, в котором она используется.
Модульная область видимости (module): Фикстура будет выполнена один раз для каждого модуля, в котором она используется.
Сессионная область видимости (session): Фикстура будет выполнена один раз для всей тестовой сессии.
Пакетная область видимости (package): Фикстура будет выполнена один раз для каждого пакета, в котором она используется.
"""
import time
import pytest
from pydash import collections

"""coll = ['One', "true", 3, 10, 'cat', {}, '', 10, False]

def test_includes():
    assert collections.includes(coll, 3) == True
    assert collections.includes(coll, 'dog') == False

def test_size():
    assert collections.size(coll) == 9"""


@pytest.fixture
def now():
    return int(time.time() * 1000)

def test_first_example(now):
    print(now)

def test_second_example(now):
    print(now)


@pytest.fixture
def coll():
    return [1, 2, 3, 4]

@pytest.fixture
def coll2():
    return [1, 2, 3, 4]

@pytest.fixture(autouse=True)
def setup_coll2(coll2):
    coll2[0] = 'a'

@pytest.fixture
def users():
    return [{'name': 'John'}, {'name': 'Tom'}]

@pytest.fixture
def admins():
    return [{'name': "Tomas"}, {'name': 'Peter'}]

@pytest.fixture
def all(users, admins):
    return users + admins

def test_third_example(coll):
    coll.append(5)
    assert coll == [1, 2, 3, 4, 5]

def test_fourth_example(coll):
    coll.pop()
    assert coll == [1, 2, 3]

def test_fifth_example(all, admins):
    expected_admins = get_admins(all, admins)
    assert admins == expected_admins

def get_admins(users, admins):
    admins_names = [admin['name'] for admin in admins]
    return [user for user in users if user['name'] in admins_names]

def test_sixth_example(coll2):
    assert coll2 == ['a', 2, 3, 4]

def test_seventh_example(coll2):
    assert coll2[0] == 'a'

"""
@pytest.fixture(scope='session')
def df():
    ...

@pytest.fixture()
def user():
    return {'id': 1, 'name': 'John'}

def test_example(df, user):
    save_to_db(df, user)
    expected_user = get_from_db(df, id=user['id'])
    assert expected_user == user
"""

"""
Встроенная фикстура capsys в Pytest!

capsys - это встроенная фикстура в Pytest, которая позволяет вам захватить и проверить вывод в консоль 
(stdout и stderr) вашего приложения или тестов.

Что такое capsys?

capsys - это сокращение от "capture sys", что означает "захватить системный вывод". 
Эта фикстура позволяет вам захватить вывод в консоль, который генерируется вашим приложением или тестами, 
и проверить его в тестах.

Как работает capsys?

Когда вы используете фикстуру capsys в тесте, Pytest создает специальный объект, 
который перехватывает вывод в консоль. Этот объект позволяет вам проверить вывод в консоль, 
который генерируется вашим приложением или тестами.
"""

def hello_world():
    print('Hello, world!')

def test_output(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'Hello, world!\n'


# import pytest

@pytest.fixture
def result():
    return sum([5, 9])

def test_sum(result):
    assert result == 14
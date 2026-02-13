class User: 
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    

# user = User("Вася")
# print(user.get_name())


import unittest

class TestUser(unittest.TestCase):
    def test_name(self):
        user = User("Вася")
        self.assertEqual(user.get_name(), "Вася")
        
        
class TestMath(unittest.TestCase):

    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)


class TestExample(unittest.TestCase):

    def setUp(self):
        self.value = 10

    def test_one(self):
        self.value += 5
        self.assertEqual(self.value, 15)

    def test_two(self):
        self.assertEqual(self.value, 10)


class TestFile(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        self.data.clear()

    def test_length(self):
        self.assertEqual(len(self.data), 3)



self.assertEqual(actual, expected)


suite = unittest.TestSuite()
suite.addTest(TestMath("test_addition"))


"""python -m unittest


python -m unittest discover



..
----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK
"""


class TestMath(unittest.TestCase):
    def setUp(self):
        self.value = 10
        
    def test_add(self):
        self.assertEqual(self.value + 5, 15)
        
    def test_sub(self):
        self.assertEqual(self.value - 5, 5)

    



























































if __name__ == "__main__":
    unittest.main()
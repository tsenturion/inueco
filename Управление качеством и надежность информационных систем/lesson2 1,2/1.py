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
    def setUp(self):
        self.value = 10
        
    def test_add(self):
        self.assertEqual(self.value + 5, 15)
        
    def test_sub(self):
        self.assertEqual(self.value - 5, 5)

    



























































if __name__ == "__main__":
    unittest.main()
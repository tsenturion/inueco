import unittest

class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def test_append(self):
        self.data.append(4)
        self.assertEqual(self.data, [1, 2, 3, 4])

def test_sum(self):
    data = [1, 2, 3]
    result = sum(data)
    self.assertEqual(result, 6)


def setUp(self):
    self.data = [1, 2, 3]

def test_sum(self):
    result = sum(self.data)
    self.assertEqual(result, 6)


class TestData(unittest.TestCase):

    def setUp(self):
        self.data = []

    def tearDown(self):
        self.data.clear()

    def test_add(self):
        self.data.append(1)
        self.assertEqual(self.data, [1])

def setUp(self):
    if some_condition:
        self.data = [1, 2]
    else:
        self.data = [3, 4]

class TestNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.values = [1, 2, 3]

    @classmethod
    def tearDownClass(cls):
        cls.values.clear()

    def test_sum(self):
        self.assertEqual(sum(self.values), 6)

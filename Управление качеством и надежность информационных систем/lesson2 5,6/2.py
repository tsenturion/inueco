def test_sum_case_1(self):
    self.assertEqual(sum([1, 2]), 3)

def test_sum_case_2(self):
    self.assertEqual(sum([3, 4]), 7)

def test_sum_case_3(self):
    self.assertEqual(sum([5, 6]), 11)


def test_sum_multiple_cases(self):
    cases = [
        ([1, 2], 3),
        ([3, 4], 7),
        ([5, 6], 11),
    ]

    for numbers, expected in cases:
        with self.subTest(numbers=numbers):
            self.assertEqual(sum(numbers), expected)


for numbers, expected in cases:
    self.assertEqual(sum(numbers), expected)


def check_sum(self, numbers, expected):
    self.assertEqual(sum(numbers), expected)

def test_sum_cases(self):
    cases = [
        ([1, 2], 3),
        ([3, 4], 7),
        ([5, 6], 11),
    ]

    for numbers, expected in cases:
        with self.subTest(numbers=numbers):
            self.check_sum(numbers, expected)


cases = [
    (10, 2, 5),
    (10, 0, ZeroDivisionError),
]


def test_even_numbers(self):
    for value in range(0, 100, 2):
        with self.subTest(value=value):
            self.assertEqual(value % 2, 0)


def create_test(value, expected):
    def test(self):
        self.assertEqual(sum(value), expected)
    return test

class TestDynamic(unittest.TestCase):
    pass

cases = [
    ([1, 2], 3),
    ([3, 4], 7),
]

for i, (value, expected) in enumerate(cases):
    setattr(
        TestDynamic,
        f"test_sum_case_{i}",
        create_test(value, expected)
    )

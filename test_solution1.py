import unittest
from solution1 import strict


class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)

    def test_incorrect_type_positional(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_incorrect_type_keyword(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_two(a=1, b="2")

    def test_no_default_values(self):
        @strict
        def sum_three(a: int, b: int, c: int) -> int:
            return a + b + c

        with self.assertRaises(TypeError):
            sum_three(1, 2)  # Недостающий аргумент 'c'


if __name__ == '__main__':
    unittest.main()

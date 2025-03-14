import unittest

from src.classes.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_sum_returns_result(self):
        a: int = 5
        b: int = 10
        self.calculator: Calculator = Calculator()

        result = self.calculator.sum(a, b)

        self.assertNotEqual(result, None)

    def test_store_saves_data(self):
        a: int = 5
        b: int = 10
        self.calculator: Calculator = Calculator()

        self.calculator.sum(a, b)
        result = self.calculator.history.data;

        self.assertEqual(result, ["5 + 10 = 15"])

    def test_sum_two_numbers(self):
        a: int = 10
        b: int = 12
        self.calculator: Calculator = Calculator()

        result: int = self.calculator.sum(a, b)

        self.assertEqual(result, 22)

    def test_sum_with_float(self):
        a: int = 10
        b: float = 2.0
        self.calculator: Calculator = Calculator()

        result: float = self.calculator.sum(a, b)

        self.assertEqual(result, 12.0)

    def test_sum_with_negative_number(self):
        a: int = 10
        b: int = -12
        self.calculator: Calculator = Calculator()

        result: int = self.calculator.sum(a, b)

        self.assertEqual(result, -2)

    def test_sum_with_float_and_negative_number(self):
        a: int = 10
        b: float = -2.0
        self.calculator: Calculator = Calculator()

        result: float = self.calculator.sum(a, b)

        self.assertEqual(result, 8.0)

    def test_sum_with_string(self):
        a: int = 10
        b: str = "100"
        self.calculator: Calculator = Calculator()

        with self.assertRaises(TypeError):
            self.calculator.sum(a, b)

    def test_sum_with_boolean(self):
        a: int = 10
        b: bool = True
        self.calculator: Calculator = Calculator()

        result = self.calculator.sum(a, b)

        self.assertEqual(result, 11)

    def test_sum_with_none(self):
        a: int = 10
        b: None = None
        self.calculator: Calculator = Calculator()

        with self.assertRaises(TypeError):
            self.calculator.sum(a, b)

    def test_sum_with_empty_values(self):
        a: None = None
        b: None = None
        self.calculator: Calculator = Calculator()

        with self.assertRaises(TypeError):
            self.calculator.sum(a, b)

    def test_sum_with_two_string(self):
        a: str = "10"
        b: str = "12"
        self.calculator: Calculator = Calculator()

        result = self.calculator.sum(a, b)

        self.assertNotEqual(result, 22)

    def test_sum_with_two_float(self):
        a: float = 10.02
        b: float = 12.0001
        self.calculator: Calculator = Calculator()

        result = self.calculator.sum(a, b)

        self.assertEqual(result, 22.0201)

    def test_sum_with_arithmetic_expression(self):
        a: int = 12 * 10
        b: int = 10 - 2
        self.calculator: Calculator = Calculator()

        result = self.calculator.sum(a, b)

        self.assertEqual(result, 128)

    def test_sum_with_collection(self):
        a: list = [1, 2, 3]
        b: int = 10
        self.calculator: Calculator = Calculator();

        with self.assertRaises(TypeError):
            self.calculator.sum(a, b)


if __name__ == '__main__':
    unittest.main()

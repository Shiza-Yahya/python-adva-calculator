import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize Calculator instance before each test"""
        self.calc = Calculator()
        # Disable print statements in memory methods for clean test output
        self.calc.memory_add = lambda x: setattr(self.calc, 'memory', self.calc.memory + x)
        self.calc.memory_subtract = lambda x: setattr(self.calc, 'memory', self.calc.memory - x)
        self.calc.memory_clear = lambda: setattr(self.calc, 'memory', 0)

    # -------- Basic Operations --------
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # -------- Advanced Operations --------
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-9)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(200, 10), 20)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(-3)

    def test_logarithm(self):
        self.assertAlmostEqual(self.calc.logarithm(100, 10), 2)
        with self.assertRaises(ValueError):
            self.calc.logarithm(-10)

    # -------- Trigonometry --------
    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(30), 0.5, places=5)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(60), 0.5, places=5)

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(45), 1, places=5)

    # -------- Memory Functions --------
    def test_memory_functions(self):
        self.calc.memory_add(50)
        self.assertEqual(self.calc.memory, 50)
        self.calc.memory_subtract(20)
        self.assertEqual(self.calc.memory, 30)
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory, 0)

if __name__ == '__main__':
    unittest.main()


import unittest

from BOMFinder.Parts.Parts import Value, Part


class DumyPart(Part):
    properties = {}


class TestValue(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        # unittest.TestCase.tearDown(self)
        pass

    def test_init(self):
        Value(100)
        Value(52.4)
        Value(0.123)

        Value("100,0")
        Value("100.0")

        Value("0.1")
        Value("0,1")

        Value("4k7")

        Value("0k47")
        Value("k47")
        Value("0.23k")

        Value("1p")
        Value("1n")
        Value("1u")
        Value("1m")
        Value("1")
        Value("1k")
        Value("1M")
        Value("1G")
        Value("1T")

        with self.assertRaises(ValueError):
            Value("100.0.0")

        with self.assertRaises(ValueError):
            Value("100,0.0")

        with self.assertRaises(ValueError):
            Value("100.G0")

        with self.assertRaises(ValueError):
            Value("4k7k")

        with self.assertRaises(ValueError):
            Value("1H")

        with self.assertRaises(ValueError):
            Value("test")

        with self.assertRaises(TypeError):
            Value([1, 2, 3])

        with self.assertRaises(TypeError):
            Value({"test": 2})

    def test_eq(self):
        test_value_1 = Value(100)
        test_value_2 = Value("100")

        test_value_3 = Value(4.7)
        test_value_4 = Value("4.7")
        test_value_5 = Value("4,7")

        test_value_6 = Value(4700)
        test_value_7 = Value("4k7")
        test_value_8 = Value("4.7k")
        test_value_9 = Value("4,7k")

        test_value_10 = Value("1p")
        test_value_11 = Value("1n")
        test_value_12 = Value("1u")
        test_value_13 = Value("1m")
        test_value_14 = Value("1")
        test_value_15 = Value("1k")
        test_value_16 = Value("1M")
        test_value_17 = Value("1G")
        test_value_18 = Value("1T")

        test_value_19 = Value("100,0")
        test_value_20 = Value("100.0")

        test_value_21 = Value("0.1")
        test_value_22 = Value("0,1")

        self.assertEqual(test_value_1, 100)
        self.assertEqual(test_value_2, test_value_1)

        self.assertEqual(test_value_3, 4.7)
        self.assertEqual(test_value_4, test_value_3)
        self.assertEqual(test_value_4, test_value_5)

        self.assertEqual(test_value_6, 4700)
        self.assertEqual(test_value_7, test_value_6)
        self.assertEqual(test_value_8, test_value_7)
        self.assertEqual(test_value_9, test_value_8)

        self.assertEqual(test_value_10, 0.000000000001)
        self.assertEqual(test_value_11, 0.000000001)
        self.assertEqual(test_value_12, 0.000001)
        self.assertEqual(test_value_13, 0.001)
        self.assertEqual(test_value_14, 1)
        self.assertEqual(test_value_15, 1000)
        self.assertEqual(test_value_16, 1000000)
        self.assertEqual(test_value_17, 1000000000)
        self.assertEqual(test_value_18, 1000000000000)

        self.assertEqual(test_value_19, 100)
        self.assertEqual(test_value_20, 100)

        self.assertEqual(test_value_21, 0.1)
        self.assertEqual(test_value_22, 0.1)

    def test_get_value(self):
        test_value_1 = Value(4700)
        self.assertEqual(test_value_1.get_value(), 4700)

        test_value_2 = Value("4k7")
        self.assertEqual(test_value_2.get_value(), 4700)

        test_value_3 = Value("4.7k")
        self.assertEqual(test_value_3.get_value(), 4700)

    def test_ammont_addition(self):
        init_amount = 10
        final_amount = 12

        part = DumyPart(Amount=init_amount)

        self.assertEqual(part.amount, init_amount)

        part.amount = final_amount

        self.assertEqual(part.amount, final_amount)
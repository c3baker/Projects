import unittest


class CollatzTestAnalyzer(unittest.TestCase):

    def test_function_runs(self):
        collatz(1)

    def test_base_case(self):
        self.assertEqual(collatz(1), 0)

    def test_value_exception(self):
        with self.assertRaises(ValueError):
            collatz(-1)

    def test_more_advanced_case(self):
        self.assertEqual(collatz(5), 5)



def collatz(n):
    """
    :param n: A number >= 1
    :return: The number of steps needed to reduce n to 1 according to the rules:
    :raises ValueError: When input n < 1
    """

    if n < 1:
        raise ValueError("n must be number >= 1")
    step = 0
    while n > 1:
        if n % 2 == 0: #Even
            n = n / 2
        else: #Odd
            n = (n * 3) + 1
        step += 1
    return step


def main():
    print("n = 1: {}".format(collatz(1)))
    print("n = 12: {}".format(collatz(12)))
    print("n = 2: {}".format(collatz(2)))



if __name__ == "__main__":
    unittest.main()

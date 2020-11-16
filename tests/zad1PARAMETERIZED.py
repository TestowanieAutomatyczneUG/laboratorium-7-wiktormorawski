import unittest
from sample.zad1 import *
class RomanPARAMETERIZED(unittest.TestCase):
    def test(self):
        file = open("data/zad1_tests_parameterized")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                input, function_return = int(data[0]), data[1].strip("\n")
                self.assertEqual(roman(input), function_return)
        file.close()

if __name__ == "__main__":
    unittest.main()
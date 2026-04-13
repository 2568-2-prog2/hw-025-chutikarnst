from dice import BiasedDice
import unittest

def test(prob):
    try:
        BiasedDice(prob)
        print("pass")
    except Exception as e:
        print(e)

class ProgrammingTest(unittest.TestCase):
    def test1(self):
        prob = [0]
        test(prob)

    def test2(self):
        prob = [0,0,0,0,0,0]
        test(prob)

    def test3(self):
        prob = [0.1,0.1,0.1,0.1,0.3,0.4]
        test(prob)

    def test4(self):
        prob = [0.1,0.1,0.1,0.1,0.2,0.4]
        test(prob)

if __name__ == '__main__':
    unittest.main()
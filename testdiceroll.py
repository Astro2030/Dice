import unittest
import dice


class MyTest(unittest.TestCase):

    def test(self):
        randrange = [1,2,3,4,5,6,7,8]
        for i in randrange:
            return i
        result = dice.dicegame()
        self.assertEqual(result, i )
       

if __name__ == "__main__":
    unittest.main()


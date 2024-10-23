import unittest
import cal

class TestCal(unittest.TestCase):
    def test_add_integer(self):
        result = cal.add2value(2,6)
        self.assertEqual(result,8.0)

    def test_add_floats(self):
        result = cal.add2value('12.5',6.5)
        self.assertEqual(result,19.0)

if __name__=='__main__':
    unittest.main()
import unittest
from task import validate_date,validate_time

class TestInformation(unittest.TestCase):
    def test_date(self):
         self.assertEqual(validate_date("30.05.2022"),True)
         self.assertEqual(validate_date("35.05.2022"),False)

    def test_time(self):
         self.assertEqual(validate_time("20:30"),True)
         self.assertEqual(validate_time("20:70"),False)
              




if __name__ == '__main__':
    unittest.main()
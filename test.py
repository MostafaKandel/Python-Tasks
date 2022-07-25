import unittest
from task import print_result, validate_date,validate_time,print_result

class TestInformation(unittest.TestCase):
    def test_date(self):
         self.assertEqual(validate_date("30.05.2022"),True)
         self.assertEqual(validate_date("35.05.2022"),False)

    def test_time(self):
         self.assertEqual(validate_time("20:30"),True)
         self.assertEqual(validate_time("20:70"),False)

    def test_print(self):
          self.assertEqual(print_result(1),"The first data has been reached" ) 
          self.assertNotEqual(print_result(2),"The 5 data has been reached")   
              




if __name__ == '__main__':
    unittest.main()
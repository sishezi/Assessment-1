import unittest
from assess import *

class TestCase(unittest.TestCase):
    
    def test_grade_ave(self):
        self.assertEqual(grade_average([1,2,3,4,5]), 3, "Unexpected output")
        self.assertEqual(grade_average([46, 78, 32, -5, 6]), 40.5, "Incorrect output")
        self.assertEqual(grade_average([-56, 94, -3, 0]), 47, "Unexpected output")
        self.assertEqual(grade_average([-2, -45, -82]), 0, "Unexpected output")
        self.assertEqual(grade_average([]), 0.0, "Unexpected ouput")


    def test_primes(self):
        self.assertIsInstance(find_prime_factors(5), [5], "Unexpected output")
        self.assertEqual(find_prime_factors(78), [2, 3, 13], "Unexpected output")    


    def test_interest(self):
        self.assertEqual(calculate_interest(650,0.07,3),150.92)


    def test_code_word(self):
        self.assertEqual(code_word([3,1,20]), "cat", "Unexpected output")
        self.assertEqual(code_word([16,25,20,8,15,14]), "python", "Unexpected output")
        self.assertEqual(code_word([14,1,20,21,18,5]), "nature", "Unexpected output")
        self.assertEqual(code_word([9,0,3,1,14,0,4,15,0,9,20]), "i can do it", "Unexpected output")


    def test_triangles(self):
        self.assertIsInstance(triangles(5), str, "Expected a string")
        self.assertEqual(triangles(3), "*\n**\n***", "Unexpected output")
        self.assertEqual(triangles(6), "*\n**\n***\n****\n*****\n******", "Unexpected output")
        self.assertEqual(triangles(7), "*\n**\n***\n****\n*****\n******\n*******", "Unexpected output")
        

    def test_hollow_triangles(self):
            self.assertIsInstance(hollow_triangle(5), str, "Expected a string")
            self.assertEqual(hollow_triangle(3), "*\n**\n***", "Unexpected output")
            self.assertEqual(hollow_triangle(6), "*\n**\n* *\n*  *\n*   *\n******", "Unexpected output")
            self.assertEqual(hollow_triangle(7), "*\n**\n* *\n*  *\n*   *\n*    *\n*******", "Unexpected output")

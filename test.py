import unittest
import re
from lab import solve
from math import pi, cos, sin

class TestStringMethods(unittest.TestCase):

  def test_solve1(self):
    self.assertEqual(solve(0,0), None)

  def test_solve2(self):
    self.assertEqual(solve(1,0), 0)

  def test_solve3(self):
    self.assertEqual(solve(0,1), pi/2)
    
  def test_solve4(self):
    self.assertEqual(solve(1,1), pi/4)

  def test_solve5(self):
    self.assertEqual(solve(-1,1), 3*pi/4)

  def test_solve6(self):
    self.assertEqual(solve(-1,-1), 5*pi/4)

  def test_solve7(self):
    self.assertEqual(solve(1,-1), 7*pi/4)

  def test_solve8(self):
    self.assertTrue(abs(1 - 5**(0.5)*cos(solve(1,2))) < 1e-9)
   
  def test_solve9(self):
    self.assertTrue(abs(-1 - 5**(0.5)*cos(solve(-1,-2))) < 1e-9)
    
  def test_solve10(self):
    self.assertTrue(abs(1 - 5**(0.5)*cos(solve(1,-2))) < 1e-9)

  def test_solve11(self):
    self.assertTrue(abs(-1 - 5**(0.5)*cos(solve(-1,2))) < 1e-9)

  def test_solve12(self):
    self.assertTrue(abs(2 - 5**(0.5)*sin(solve(1,2))) < 1e-9)
   
  def test_solve13(self):
    self.assertTrue(abs(-2 - 5**(0.5)*sin(solve(-1,-2))) < 1e-9)
    
  def test_solve14(self):
    self.assertTrue(abs(-2 - 5**(0.5)*sin(solve(1,-2))) < 1e-9)

  def test_solve15(self):
    self.assertTrue(abs(2 - 5**(0.5)*sin(solve(-1,2))) < 1e-9)



if __name__ == '__main__':
    unittest.main()
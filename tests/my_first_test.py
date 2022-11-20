from app.calc import Calculator
import pytest

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_multiply(self):
       assert self.calc.multiply(self, 3,3) == 9

   def test_division(self):
       assert (self).calc.division(self, 10, 2) == 5

   def test_substracton(self):
       assert (self).calc.subtraction(self, 3, 1) == 2

   def test_adiing(self):
       assert (self).calc.adding(self, 2, 4) == 6
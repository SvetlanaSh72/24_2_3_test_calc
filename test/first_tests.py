import pytest
from app import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2,2) == 4

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,12345679,9) == 111111111
        print('  Точно рабочий=)')

    def test_division_calculate_correctly(self):
        assert self.calc.division(self,6,2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self,10,3) == 7

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self,2,3) == 5

    def test_multiply_calculate_failed(self):
        try:
            self.calc.division(self, 1, 0)
        except ZeroDivisionError:
            print('   Error: ZeroDivisionError!')
import time

from src.calculator import Calculator
from contextlib import nullcontext as not_raise

import allure
import pytest
import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1


class TestCalculatorPositive:

    @allure.title('Checking additional function.')
    @pytest.mark.parametrize('num1, num2, result, expectation',
                             [(0, 0, 0, not_raise()), (1, 101, 102, not_raise()),
                              (-1, 1, 0, not_raise()), (10000, 10000, 20000, not_raise()),
                              (1, '1', 2, pytest.raises(TypeError))])
    def test_additional(self, num1, num2, result, expectation):
        with expectation:
            assert Calculator.addition(num1, num2) == result

    @allure.title('Checking minus function.')
    @pytest.mark.parametrize('num1, num2, result',
                             [(0, 0, 0), (1, 101, -100), (-1, 1, -2), (10000, 10000, 0)])
    def test_minus(self, num1, num2, result):
        assert Calculator.minus(num1, num2) == result

    @allure.title('Checking multiplication function.')
    @pytest.mark.parametrize('num1, num2, result, expectation',
                             [(0, 0, 0, not_raise()), (2, 3, 6, not_raise()),
                              (1, -10, -10, not_raise()), (-32, 3, -96, not_raise()),
                              (-11, -5, 55, not_raise()), (0.123, 987, 121.401, not_raise())])
    def test_multiplication(self, num1, num2, result, expectation):
        with expectation:
            assert Calculator.multiplication(num1, num2) == result


class TestCalculatorNegative:

    @staticmethod
    @allure.title('Checking division with negative result.')
    @pytest.mark.negative
    @pytest.mark.parametrize('num1, num2, result',
                             [(10, 1, 1), (1, 1, 0), (10, -1, 10)
                                 , (123, 123, 2), (999999, 1, 1), (MAX_INT, MAX_INT, 2)])
    def test_division(num1, num2, result):
        assert Calculator.division(num1, num2) != result


# @pytest.mark.skipif('config.getoption("--browser") == "false"')
def test_slow():
    time.sleep(10)
    assert 1 == 1

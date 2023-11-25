from src.calculator import Calculator
from contextlib import nullcontext as not_raise
import allure
import pytest

class TestCalculator:

    @allure.title('Checking additional function.')
    @pytest.mark.parametrize('num1, num2, result, expectation',
                             [(0, 0, 0, not_raise()), (1, 101, 102, not_raise()),
                              (-1, 1, 0, not_raise()), (10000, 10000, 20000, not_raise()),
                              (1, '1', 2, pytest.raises(TypeError))])
    def test_additional(self, num1, num2, result, expectation):
        with expectation:
            assert Calculator.addition(num1, num2) == result

    @allure.title('Checking minus function.')
    @pytest.mark.parametrize('num1, num2, result, ',
                             [(0, 0, 0), (1, 101, -100), (-1, 1, -2), (10000, 10000, 0)])
    def test_minus(self, num1, num2, result):
        assert Calculator.minus(num1, num2) == result

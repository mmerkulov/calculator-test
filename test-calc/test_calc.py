from src.calculator import Calculator
import allure
import pytest


class TestCalculator:

    @allure.title('Checking additional function.')
    @pytest.mark.parametrize('num1, num2, result',
                             [(0, 0, 0), (1, 101, 102), (-1, 1, 0), (10000, 10000, 20000)])
    def test_additional(self, num1, num2, result):
        assert Calculator.addition(num1, num2) == result

    @allure.title('Checking minus function.')
    @pytest.mark.parametrize('num1, num2, result',
                             [(0, 0, 0), (1, 101, -100), (-1, 1, -2), (10000, 10000, 0)])
    def test_minus(self, num1, num2, result):
        assert Calculator.minus(num1, num2) == result

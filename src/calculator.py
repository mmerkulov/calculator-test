from typing import Union


class Calculator:

    @staticmethod
    def __check_type(*args):
        for i in args:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError('Only int and float are allowed.')

    @staticmethod
    def addition(num1: Union[int | float], num2: Union[int | float]) -> int | float:
        Calculator.__check_type(num1, num2)
        return num1 + num2

    @staticmethod
    def minus(num1: Union[int | float], num2: Union[int | float]) -> int | float:
        Calculator.__check_type(num1, num2)
        return num1 - num2

    @staticmethod
    def division(num1: Union[int | float], num2: Union[int | float]) -> int | float:
        Calculator.__check_type(num1, num2)
        if num2 == 0:
            # allure log
            raise ZeroDivisionError("Сan't divide by zero, check Num2.")

        return round(num1 / num2, 2)

    @staticmethod
    def multiplication(num1: Union[int | float], num2: Union[int | float]) -> int | float:
        Calculator.__check_type(num1, num2)
        return num1 * num2

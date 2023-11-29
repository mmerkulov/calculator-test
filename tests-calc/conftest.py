from src.config import settings
import pytest
import allure


# Чистить и создавать данные => fixtur


@pytest.fixture(scope="session", autouse=True)
def checking_work_mode():
    assert settings.WORK_MODE == 'TEST'


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        default='chrome',
        choises=('chrome', 'opera', 'firefox')
    )


def pytest_addoption(parser):
    parser.addoption(
        '--run-slow',
        default='false',
        choises=('true', 'false')
    )


@pytest.fixture
def browser(requets):
    return requets.config.getoption('--browser')

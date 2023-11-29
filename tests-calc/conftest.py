from src.config import settings
import pytest
import allure
# Чистить и создавать данные => fixtur


@pytest.fixture(scope="session", autouse=True)
def checking_work_mode():
    assert settings.WORK_MODE == 'TEST'

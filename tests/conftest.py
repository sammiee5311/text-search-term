from __future__ import annotations

from pathlib import Path
from typing import Generator

import pytest

TEST_FILE = "./tests/test.txt"
RESULT_FILE = "./tests/result.txt"


@pytest.fixture()
def test_data() -> list[str]:
    result = []

    if Path(TEST_FILE).is_file():
        with open(TEST_FILE) as file:
            for line in file:
                result.append(line.strip())

    return result


@pytest.fixture(scope="session", autouse=True)
def clean_up() -> Generator[None, None, None]:
    yield
    result_file = Path(RESULT_FILE)
    if result_file.exists():
        result_file.unlink()


def get_test_result_data() -> list[str]:
    result = []

    if Path(RESULT_FILE).is_file():
        with open(RESULT_FILE) as file:
            for line in file:
                result.append(line.strip())

    return result

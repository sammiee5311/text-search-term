from __future__ import annotations

from pathlib import Path

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


def get_test_result_data() -> list[str]:
    result = []

    if Path(RESULT_FILE).is_file():
        with open(RESULT_FILE) as file:
            for line in file:
                result.append(line.strip())

    return result

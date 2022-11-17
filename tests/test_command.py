from __future__ import annotations

from click.testing import CliRunner
from tests.conftest import get_test_result_data

from main import search

TEST_FILE = "./tests/test.txt"
RESULT_FILE = "./tests/result.txt"


def test_search_command() -> None:
    runner = CliRunner()
    result = runner.invoke(search, args=["--directories", "./tests", "--term", "wow"])
    test_result_data = get_test_result_data()

    assert result.exit_code == 0
    assert test_result_data == ["wow", "asdfsdafasfwowasdgas"]

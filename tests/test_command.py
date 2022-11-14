from __future__ import annotations

from click.testing import CliRunner

from main import search

TEST_FILE = "./tests/test.txt"
RESULT_FILE = "./tests/result.txt"


def test_search_command(test_result_data: list[str]) -> None:
    runner = CliRunner()
    result = runner.invoke(search, args=["--directories", "./tests", "--term", "wow"])

    assert result.exit_code == 0
    assert test_result_data == ["wow", "asdfsdafasfwowasdgas"]

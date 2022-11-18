""" search term in files """

__version__ = "0.1.0"

import os
import re
from pathlib import Path

import click

from config import load_env
from logs.logging import logger

load_env()

RESULT_FILE = os.environ.get("RESULT_FILE", "./result.txt")


@click.group()
def cli() -> None:
    """Search term"""


@click.command("search")
@click.option("--type", default="txt", help="File Type to search")
@click.option(
    "--directories",
    default="./",
    help="Directory to search (devide with `:`, for instance, `./test:./prod`",
)
@click.option("--term", help="Search term")
def search(type: str, directories: str, term: str) -> None:
    if not term:
        print("Please, provide a search term.")
        return

    result_file = open(RESULT_FILE, "w")

    for path in directories.split(":"):
        files = Path(path).glob(f"*.{type}")
        try:
            for file in files:
                if file.is_file():
                    logger.info(f"Processing {file}...")
                    with open(file) as f:
                        for line in f:
                            result = re.findall(term, line)

                            if result:
                                result_file.write(line)
        except Exception as e:
            logger.error(f"An error is occured. error: {e}")

    result_file.close()


if __name__ == "__main__":  # pragma: no cover
    cli.add_command(search)
    cli()

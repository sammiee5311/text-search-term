""" search term in files """

__version__ = "0.1.0"

import os
import re
from pathlib import Path

import click

from config import load_env

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
        print("Please, provide search term.")
        return

    result_file = open(RESULT_FILE, "w")

    for path in directories.split(":"):
        files = Path(path).glob(f"*.{type}")

        for file in files:
            print(f"Processing {file}...")
            with open(file) as f:
                for line in f:
                    result = re.findall(term, line)

                    if result:
                        result_file.write(line)

    result_file.close()


if __name__ == "__main__":
    cli.add_command(search)
    cli()

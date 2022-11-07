import re
from pathlib import Path

import click


@click.group()
def cli():
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

    for path in directories.split(":"):
        files = Path(path).glob(f"*.{type}")

        for file in files:
            print(f"Processing {file}...")
            with open(file) as f:
                for line in f:
                    result = re.findall(term, line)

                    if result:
                        print(file, line)


if __name__ == "__main__":
    cli.add_command(search)
    cli()

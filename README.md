# text search term
[![CI](https://github.com/sammiee5311/text-search-term/actions/workflows/CI.yaml/badge.svg)](https://github.com/sammiee5311/text-search-term/actions/workflows/CI.yaml) [![python](./imgs/python-version.svg)]() [![](./imgs/coverage.svg?dummy=8484744)]()

search term in text or log files and save the result.

## prerequisites
- <= python 3.7

## how to use
1. type environment variables in `.env` file.
    - `RESULT_FILE` is a file name where you want to save the result.
2. create virtual python environment
    - `python -m venv venv`
    - or `virtualenv venv -ppy< python version(ex, 310) >` (if you have installed virtualenv)
3. activate python venv
    - mac
        - `source venv/bin/activate`
    - window
        - `./venv/Scripts/activate`
    - linux
        - `. venv/bin/activate`
4. install dependencies
    - `pip install -r requirements.txt`
5. use `search` command with `python main.py`
    - example : `python main.py search`

## command
- search
    - argument:
        - `--type`
            - ex) `python main.py search --type txt`
            - file type to search (default: txt)
        - `--directories`
            - ex) `python main.py convert --directories ./tests`
            - Directory to search (devide with `:`, for instance, `./test:./prod`
        - `--term`
            - ex) `python main.py search --term test`
            - search term
    - search term in specific file type of files and save the result.

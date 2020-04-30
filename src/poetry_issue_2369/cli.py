# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from __main__ later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m poetry_issue_2369` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `poetry_issue_2369.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `poetry_issue_2369.__main__` in `sys.modules`.

"""Module that contains the command line application."""

import argparse


def get_parser():
    """Return the CLI argument parser."""
    return argparse.ArgumentParser(prog="poetry-issue-2369")


def main(args=None):
    """The main function, which is executed when you type `poetry_issue_2369` or `python -m poetry_issue_2369`."""
    parser = get_parser()
    opts = parser.parse_args(args=args)
    print(opts)
    return 1

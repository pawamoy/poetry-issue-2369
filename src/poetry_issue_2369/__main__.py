"""
Entry-point module, in case you use `python -m poetry_issue_2369`.

Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

import sys

from poetry_issue_2369.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

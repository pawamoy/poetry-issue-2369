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


def main(args=None):
    return 1

r"""Rule module.

This module and sub-modules contain all the rules that can be applied
to the commit messages.


>>> good_message = '''fix(kgb): Make kgb reliable
...
... We used docstrings to keep the tests as close as possible to the codes.
... Look! That line was exactly 72 characters long!!!
... Yes I know that came at the price of an extra s at code.
... '''

>>> bad_message = '''fixes(k g b): Make it quick and dirty, make it bads
... We try to make explanations as understandable as possible but we have some
... \tissues with code consistency.'''

>>> len(apply_checks(good_message))
0
>>> len(apply_checks(bad_message))
5
"""

import re
from inspect import getmembers, isfunction
from . import line_rules
from . import raw_rules
from . import status_rules


def _get_rules(module):
    """Get all functions from a module."""
    return [tup[1] for tup in getmembers(module, isfunction)
            if tup[0][0] != "_"]

_LINE_RULES = _get_rules(line_rules)
_RAW_RULES = _get_rules(raw_rules)
_STATUS_RULES = _get_rules(status_rules)


def split_lines(commit_message):
    """Split lines of the commit (windows or linux)."""
    return re.split('\r?\n', commit_message)


def _is_merge(commit):
    """Check if the commit is a merge commit from github.

    Merges from github always contain a number."""
    return commit.startswith("Merge pull request #")


def apply_checks(commit_message):
    """Apply all rules to the commit message."""
    if _is_merge(commit_message):
        return []

    errors = []
    for rule in _RAW_RULES:
        err = rule(commit_message)
        if err is not None:
            errors.append(err)
    commit_lines = split_lines(commit_message)
    for rule in _STATUS_RULES:
        err = rule(commit_lines[0])
        if err is not None:
            errors.append(err)
    for check in _LINE_RULES:
        err = check(commit_lines)
        if err is not None:
            errors.append(err)
    return errors

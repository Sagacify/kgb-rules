"""Default parameters for rules.

These can be overridden by environment parameters
"""

from os import environ as env


MAX_STATUS_LENGTH = int(env.get("MAX_STATUS_LENGTH") or 50)
MAX_LINE_LENGTH = int(env.get("MAX_LINE_LENGTH") or 72)

_DEFAULT_TYPES = ",".join([
    "doc",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
    "version"])
TYPES = frozenset((env.get("AUTHORIZED_TYPES") or _DEFAULT_TYPES).split(","))

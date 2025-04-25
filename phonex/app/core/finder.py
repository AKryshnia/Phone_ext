import re
from typing import Final

__all__ = ["PhoneFinder"]

_CANDIDATE_RE: Final[re.Pattern[str]] = re.compile(
    r"""
    (?P<prefix>\+7|8)
    (?:[\s().\-]*\d){10,14}
    """,
    re.VERBOSE,
)


class PhoneFinder:
    def find(self, text: str) -> list[str]:
        return [match.group() for match in _CANDIDATE_RE.finditer(text)]

import re
from typing import Final

__all__ = ["PhoneNormalizer"]

_DIGIT_RE: Final[re.Pattern[str]] = re.compile(r"\d")


class PhoneNormalizer:
    def normalize(self, candidate: str) -> str | None:
        digits = "".join(_DIGIT_RE.findall(candidate))
        if len(digits) != 11 or digits[0] not in {"7", "8"}:
            return None
        digits = "7" + digits[1:]
        yyy, xxx, xx1, xx2 = digits[1:4], digits[4:7], digits[7:9], digits[9:]
        return f"+7({yyy}){xxx}-{xx1}-{xx2}"

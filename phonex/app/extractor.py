import re
from collections import OrderedDict
from typing import Final
from pathlib import Path

from loguru import logger


_DIGIT_RE: Final = re.compile(r"\d")
_CANDIDATE_RE: Final = re.compile(
    r"""
    (?P<prefix>\+7|8)                # российский префикс
    (?:[\s().\-]*\d){10,14}          # минимум 10 цифр с шумом
    """,
    re.VERBOSE,
)


class PhoneExtractor:
    """Извлекает уникальные телефоны и приводит их к формату +7(YYY)XXX-XX-XX."""

    def __init__(self) -> None:
        self._seen: OrderedDict[str, None] = OrderedDict()

    def feed_text(self, text: str) -> None:
        """Анализирует строку и добавляет валидные номера в коллекцию."""
        for match in _CANDIDATE_RE.finditer(text):
            phone = self._normalize(match.group())
            if phone:
                logger.debug(f"Найден номер: {phone}")
                self._seen.setdefault(phone, None)

    def feed_file(self, path: Path | str, encoding: str = "utf-8") -> None:
        """Считывает весь файл синхронно и обрабатывает."""
        text = Path(path).read_text(encoding=encoding, errors="ignore")
        self.feed_text(text)

    async def feed_file_async(self, path: Path | str, encoding: str = "utf-8") -> None:
        """Асинхронное чтение построчно."""
        import aiofiles
        async with aiofiles.open(path, mode="r", encoding=encoding, errors="ignore") as f:
            async for line in f:
                self.feed_text(line)

    def result(self) -> list[str]:
        """Возвращает уникальные телефоны в порядке появления."""
        return list(self._seen)

    @staticmethod
    def _normalize(candidate: str) -> str | None:
        """Приводит телефон к формату +7(YYY)XXX-XX-XX."""
        digits = "".join(_DIGIT_RE.findall(candidate))
        if len(digits) != 11 or digits[0] not in {"7", "8"}:
            return None
        digits = "7" + digits[1:]
        yyy, xxx, xx1, xx2 = digits[1:4], digits[4:7], digits[7:9], digits[9:]
        return f"+7({yyy}){xxx}-{xx1}-{xx2}"

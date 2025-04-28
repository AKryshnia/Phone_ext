from pathlib import Path

from app.core.finder import PhoneFinder
from app.core.normalizer import PhoneNormalizer
from app.core.storage import PhoneStorage
from loguru import logger

__all__ = ["PhoneExtractor"]


class PhoneExtractor:
    def __init__(self) -> None:
        self.finder = PhoneFinder()
        self.normalizer = PhoneNormalizer()
        self.storage = PhoneStorage()

    def feed_text(self, text: str) -> None:
        for raw in self.finder.find(text):
            phone = self.normalizer.normalize(raw)
            if phone:
                logger.debug(f"Найден номер: {phone}")
                self.storage.add(phone)

    def feed_file(self, path: Path | str, encoding: str = "utf-8") -> None:
        text = Path(path).read_text(encoding=encoding, errors="ignore")
        self.feed_text(text)

    async def feed_file_async(self, path: Path | str, encoding: str = "utf-8") -> None:
        import aiofiles
        async with aiofiles.open(path, mode="r", encoding=encoding, errors="ignore") as f:
            async for line in f:
                self.feed_text(line)

    def result(self) -> list[str]:
        return self.storage.get_all()

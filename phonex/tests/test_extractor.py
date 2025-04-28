import asyncio
from pathlib import Path
from click.testing import CliRunner
import pytest

from app.extractor import PhoneExtractor
from app.core.normalizer import PhoneNormalizer
from app.cli import main


@pytest.mark.parametrize("text, expected", [
    (
        "Позвоните +7 912-345-67-89 или 8 (495) 123 45 67",
        ["+7(912)345-67-89", "+7(495)123-45-67"]
    ),
    (
        "+7(903) 456 78 90, 8-900-111-22-33, +7 (999) 888.77.66",
        ["+7(903)456-78-90", "+7(900)111-22-33", "+7(999)888-77-66"]
    ),
    (
        "Невалидные: +74991234ABCD, 12345",
        []
    ),
    (
        "+7 912-345-67-89 и ещё раз +7 912-345-67-89",
        ["+7(912)345-67-89"]
    ),
])
def test_extractor_variants(text, expected):
    extractor = PhoneExtractor()
    extractor.feed_text(text)
    assert extractor.result() == expected


def test_extractor_order():
    text = "8 (800) 555 35 35 и +7 900-000-00-00"
    extractor = PhoneExtractor()
    extractor.feed_text(text)
    assert extractor.result() == ["+7(800)555-35-35", "+7(900)000-00-00"]


def test_normalizer_valid_invalid():
    normalizer = PhoneNormalizer()
    assert normalizer.normalize("8 (495) 123 45 67") == "+7(495)123-45-67"
    assert normalizer.normalize("+74991234ABCD") is None


def test_feed_file(tmp_path: Path):
    file = tmp_path / "sample.txt"
    file.write_text("+7 912-345-67-89")
    extractor = PhoneExtractor()
    extractor.feed_file(file)
    assert extractor.result() == ["+7(912)345-67-89"]


def test_async_file_read(tmp_path: Path):
    file = tmp_path / "async.txt"
    file.write_text("8 (900) 123 45 67")
    extractor = PhoneExtractor()
    asyncio.run(extractor.feed_file_async(file))
    assert extractor.result() == ["+7(900)123-45-67"]


def test_cli_runner(tmp_path: Path):
    file = tmp_path / "phones.txt"
    file.write_text("Позвоните +7 912-345-67-89")
    result = CliRunner().invoke(main, [str(file)])
    assert result.exit_code == 0
    assert "+7(912)345-67-89" in result.output

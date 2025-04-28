import asyncio
from pathlib import Path

import click
from loguru import logger

from app.extractor import PhoneExtractor


@click.command()
@click.argument("filename", type=click.Path(exists=True, path_type=Path))
@click.option("--async", "use_async", is_flag=True, help="Асинхронное чтение файла")
@click.option("--log", default="INFO", help="Уровень логирования: DEBUG, INFO, WARNING")
def main(filename: Path, use_async: bool, log: str) -> None:
    logger.remove()
    logger.add(lambda msg: click.echo(msg, nl=False), level=log.upper())

    extractor = PhoneExtractor()

    if use_async:
        asyncio.run(extractor.feed_file_async(filename))
    else:
        extractor.feed_file(filename)

    phones = extractor.result()

    click.secho(f"\nНайдено номеров: {len(phones)}", fg="green", bold=True)
    for phone in phones:
        click.echo(phone)


if __name__ == "__main__":
    main()

# Phone Number Extractor

Извлечение всех уникальных номеров телефонов из текстового файла с нормализацией формата к виду:  
**`+7(YYY)XXX-XX-XX`**

Проект написан на **Python 3.12**, с соблюдением принципов **OOP, SOLID, DRY, KISS**  
Поддерживает **CLI-интерфейс**, логирование через **loguru**, асинхронную обработку, покрыт тестами.

---

## Пример работы

```
Текст: "Позвоните по номеру +7 912-345-67-89 или 8 (495) 123 45 67."
→ Результат:
+7(912)345-67-89
+7(495)123-45-67
```

---

## Установка и запуск

```bash
# Клонируйте проект
git clone https://github.com/your-username/phone-extractor.git
cd phone-extractor

# Создайте и активируйте виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows

# Установите зависимости
pip install -r requirements.txt
```

---

## Запуск CLI

```bash
cd phonex
python -m app.cli app/phones.txt --log DEBUG
```

---

## Тестирование

```bash
pytest tests/ -v
pytest --cov=. --cov-report=term-missing
```

Примеры:

```bash
tests/test_extractor.py ..........
-------------------------------------- coverage ---------------------------------------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
app\__init__.py               0      0   100%
app\cli.py                   22      2    91%   21, 33
app\core\__init__.py          0      0   100%
app\core\finder.py            7      0   100%
app\core\normalizer.py       12      0   100%
app\core\storage.py           9      0   100%
app\extractor.py             27      0   100%
tests\__init__.py             0      0   100%
tests\test_extractor.py      50      0   100%
-------------------------------------------------------
TOTAL                        77      2    98%
```

---

## Структура проекта

```
phonex/
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── extractor.py
│   ├── phones.txt
│   └── core/
│       ├── __init__.py
│       ├── finder.py
│       ├── normalizer.py
│       └── storage.py
├── tests/
│   ├── __init__.py
│   └── test_extractor.py 
├── .gitignore
├── README.md
├── requirements.txt

```
---

# requirements.txt (если формируется вручную)
```
click==8.1.*
loguru==0.7.*
aiofiles==23.*
pytest==8.*
pytest-cov==4.*
```
---

## Используемые технологии

- Python 3.12
- `click` — CLI-интерфейс
- `loguru` — удобное логирование
- `aiofiles` — асинхронное чтение файлов
- `pytest` — модульное тестирование

---

## Принципы

Код построен по принципам:

- Single Responsibility — каждый класс делает только одно
- Open/Closed — легко расширяется
- KISS / DRY — минимум лишнего и повторений
- Тестируемость — вся логика покрыта unit-тестами

---

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
Вы можете свободно использовать, копировать, изменять и распространять код с указанием авторства.


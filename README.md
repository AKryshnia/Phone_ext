# 📎 Phone Number Extractor

Извлечение всех уникальных номеров телефонов из текстового файла с нормализацией формата к виду:  
**`+7(YYY)XXX-XX-XX`**

Проект написан на **Python 3.11+**, с соблюдением принципов **OOP, SOLID, DRY, KISS**  
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
python -m app.cli <путь_к_файлу> [--async] [--log DEBUG]
```

Примеры:

```bash
python -m app.cli app/phones.txt
python -m app.cli app/phones.txt --log DEBUG
python -m app.cli app/phones.txt --async
```

---

## Тестирование

```bash
pytest tests/ -v
pytest --cov=. --cov-report=term-missing
```

---

## Структура проекта

```
phonex/
├── app/
│   ├── cli.py
│   ├── extractor.py
│   └── core/
│       ├── finder.py
│       ├── normalizer.py
│       └── storage.py
├── tests/
│   └── test_extractor.py
├── phones.txt
├── .gitignore
└── README.md
```

---

## 📚 Используемые технологии

- Python 3.11+
- `click` — CLI-интерфейс
- `loguru` — удобное логирование
- `aiofiles` — асинхронное чтение файлов
- `pytest` — модульное тестирование

---

## 🧐 Принципы

Код построен по принципам:

- ✅ Single Responsibility — каждый класс делает только одно
- ✅ Open/Closed — легко расширяется
- ✅ KISS / DRY — минимум лишнего и повторений
- ✅ Тестируемость — вся логика покрыта unit-тестами

---

## 📋 Лицензия

Проект предоставляется "как есть" для демонстрации навыков.


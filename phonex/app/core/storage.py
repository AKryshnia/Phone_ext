from collections import OrderedDict

__all__ = ["PhoneStorage"]


class PhoneStorage:
    def __init__(self) -> None:
        self._phones: OrderedDict[str, None] = OrderedDict()

    def add(self, phone: str) -> None:
        self._phones.setdefault(phone, None)

    def get_all(self) -> list[str]:
        return list(self._phones)

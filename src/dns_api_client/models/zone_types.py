from enum import Enum


class ZoneTypes(str, Enum):
    NATIVE = "NATIVE"
    SLAVE = "SLAVE"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RecordTypes(str, Enum):
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    MX = "MX"
    NS = "NS"
    SOA = "SOA"
    SRV = "SRV"
    TXT = "TXT"
    CAA = "CAA"

    def __str__(self) -> str:
        return str(self.value)

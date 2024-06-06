from enum import Enum, auto


class ATM(Enum):
    SHOW_BALANCE = auto()
    DEPOSIT = auto()
    WITHDRAW = auto()
    EXIT = auto()

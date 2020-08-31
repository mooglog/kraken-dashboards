from dataclasses import *

from datetime import datetime


@dataclass()
class OpenPosition:
    """
    An object and methods for open positions
    """
    ordertxid: str
    posstatus: str
    pair: str
    time: float
    type: str
    ordertype: str
    cost: float
    fee: float
    vol: float
    vol_closed: float
    margin: float
    value: float
    net: float
    terms: str
    rollovertm: float
    misc: str
    oflags: str
    pl: float = 0

    def __post_init__(self):
        # enforce typing
        for f in fields(self):
            value = getattr(self, f.name)
            if not isinstance(value, f.type):
                setattr(self, f.name, f.type(value))
        # calculate profit and loss
        self.pl = round(self.net / self.cost * 100)



from dataclasses import dataclass
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
